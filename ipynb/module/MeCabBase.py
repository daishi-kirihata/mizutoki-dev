# -*- coding:utf-8 -*-
from module.interface.IMeCab import IMeCab
from pathlib import Path
import MeCab
import re
import subprocess

class MeCabBase(IMeCab):
    MECAB_DICT_INDEX = r'c:\Program Files\MeCab\bin\mecab-dict-index.exe'
    MECAB_IPADIC = r'c:\Program Files\MeCab\dic\ipadic'
    PATTERN_DIC_PATH = r'dic\{0}.dic'
    PATTERN_CSV_PATH = r'csv\{0}.csv'
    HEADER = '表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音'

    @property
    def user_dic(self):
        return self.__user_dic

    @user_dic.setter
    def user_dic(self, user_dic):
        self.__set_user_dic(user_dic)

    def __set_user_dic(self, user_dic):
        if user_dic is None:
            # user_dicがNoneを指定された場合はTaggerインスタンスの設定値は設定しない
            self.__user_dic = None
            self.__tagger = MeCab.Tagger()
        else:
            # user_dicに指定がされている場合はファイルの存在を確認し、Taggerインスタンスの設定値に追加する
            file = Path(self.PATTERN_DIC_PATH.format(user_dic)).absolute()
            if file.is_file():
                self.__user_dic = str(file)
                self.__tagger = MeCab.Tagger('-u {0}'.format(self.__user_dic))

    def __str__(self):
        '''
        文字列取得

        @rtype: str
        '''
        return self.__class__.__name__

    def __init__(self):
        '''
        コンストラクタ MeCabBase
        '''
        self.__user_dic = None
        self.__tagger = MeCab.Tagger()

    def __del__(self):
        '''
        デストラクタ MeCabBase
        '''
        self.__user_dic = None
        self.__tagger = None
    
    def new_user_dic(self, user_dic):
        '''
        指定したユーザ辞書を作成する

        @param: user_dic
        @type:  str
        '''
        file = Path(self.PATTERN_CSV_PATH.format(user_dic)).absolute()
        #TODO: csvファイルの存在判定
        assert not file.is_file(), '指定したファイルはすでに存在しています。ファイル名: {0}'.format(file.relative_to(Path.cwd()))

        #TODO: csvファイルを作成
        file.touch()

        #TODO: csvに追記する内容を定義する(初期値の単語の登録)
        append_text = ['%INIT_USER_DIC%', '%LEFT_ID%', '%RIGHT_ID%', '%COST%', '%WORD_CLASS%', '%SUBCLASS1%', '%SUBCLASS2%', '%SUBCLASS3%', '%DERIVATION_CLASS%', '%DERIVATION%', '%STEM%', '%SPELL%', '%PRONOUNCIATION%']

        #TODO: csvに追記する
        self.__write_csv(file.stem, ','.join(append_text))
        
        #TODO: dicファイルへのコンパイル処理
        self.update_user_dic(user_dic)

        #TODO: csvファイルの内容をクリアする
        file.write_text('')

    def update_user_dic(self, user_dic):
        '''
        指定したユーザ辞書をcsvからdicへコンパイルする
        
        @param: user_dic
        @type:  str
        '''
        files =list()
        files.append(Path(self.PATTERN_DIC_PATH.format(user_dic)).absolute())
        files.append(Path(self.PATTERN_CSV_PATH.format(user_dic)).absolute())

        #TODO: インスタンスが参照しているユーザ辞書を退避する
        ref_user_dic = None
        if self.__user_dic is not None:
            ref_user_dic = str(Path(self.__user_dic).stem)
            self.__set_user_dic(user_dic=None)

        #TODO: インスタンスが参照中の辞書が指定されている場合はエラーを返す
        #assert not self.__user_dic == str(files[0]), '対象のファイルは現在参照中のため、更新できません。ファイル名:\t{0}'.format(files[0].relative_to(Path.cwd()))

        #TODO: 既存のdicファイルを削除する
        if files[0].is_file():
            files[0].unlink()

        #TODO: csvファイルを最適化する
        self.__optimize_user_word(user_dic)

        #TODO: コンパイル処理の開始
        command = r'"{0}" -d "{1}" -u {2} -f utf-8 -t utf-8 {3}'.format(
            self.MECAB_DICT_INDEX, 
            self.MECAB_IPADIC,
            files[0].relative_to(Path.cwd()),
            files[1].relative_to(Path.cwd()))
        process = subprocess.run(
            command,
            cwd=Path.cwd(),
            shell=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            timeout=10)
        
        #TODO: 退避したユーザ辞書へのtaggerのインスタンスを設定する。
        if ref_user_dic is not None:
            self.__set_user_dic(user_dic=ref_user_dic)
        
        #TODO: 処理結果を報告
        if len(process.stderr.decode('cp932'))>0:
            print('エラーが発生しました。内容を確認してください。\n{0}'.format(process.stderr.decode('cp932')))
        else:
            print('ユーザ辞書を更新しました。user_dic:\t{0}'.format(files[0].relative_to(Path.cwd())))

    def delete_user_dic(self, user_dic):
        '''
        指定したユーザ辞書を削除する

        @param: user_dic
        @type:  str
        '''
        files = list()
        files.append(Path(self.PATTERN_DIC_PATH.format(user_dic)).absolute())
        files.append(Path(self.PATTERN_CSV_PATH.format(user_dic)).absolute())
        
        #TODO: インスタンスが参照中の辞書が指定されている場合はエラーを返す
        assert not self.__user_dic == str(files[0]), '対象のファイルは現在参照中のため、削除できません。ファイル名:\t{0}'.format(files[0].relative_to(Path.cwd()))
        
        #TODO: dic, csvファイルを削除する
        report = list()
        for file in files:
            if file.is_file():
                report.append(file.name)
                file.unlink()
        #TODO: 処理結果を報告
        print('ユーザ辞書を削除しました。ファイル:\t{0}'.format(', '.join(report)))
    
    def __write_csv(self, file_name, append_text):
        '''
        指定csvファイルに1行追記する

        @param: file_name, append_text
        @type:  str
        '''
        file = Path(self.PATTERN_CSV_PATH.format(file_name)).absolute()
        assert file.is_file(), '指定ファイルは存在しません。file_name: {0}'.format(file_name)

        with file.open(mode='a', encoding='utf-8') as f:
            f.write('{0}\n'.format(append_text))
    
    def append_user_word(self, word=None, left_id='1', right_id='1', cost='1', word_class=None, subclass1=None, subclass2='*', subclass3='*', derivation_class='*', derivation='*', stem=None, spell=None, pronounciation=None):
        '''
        ユーザ辞書csvにwordを追加する

        @param: word, word_class, subclass1, stem, spell, pronounciation
        @type:  str
        '''
        #TODO: self.__user_dicがNoneの場合の処理
        assert self.__user_dic is not None, 'ユーザ辞書が設定されていないため、追記できません'
        file = Path(self.PATTERN_CSV_PATH.format(Path(self.__user_dic).stem)).absolute()
        
        #TODO: csvファイルへの追記処理
        append_text = [word, left_id, right_id, cost, word_class, subclass1, subclass2, subclass3, derivation_class, derivation, stem, spell, pronounciation]
        
        #TODO: 追記内容内にNoneの存在をチェックする
        for part in append_text:
            assert part is not None, 'Noneの要素が含まれています'

        #TODO: csvファイルに追記する
        self.__write_csv(file.stem, ','.join(append_text))
        
        #TODO: 処理結果を報告
        print('ユーザ辞書に追記しました。ユーザ辞書:\t{0}'.format(file.stem))

    def remove_user_word(self, word):
        '''
        ユーザ辞書csvからwordを削除する

        @param: word
        @type:  str
        '''
        #TODO: self.__user_dicがNoneの場合の処理
        assert self.__user_dic is not None, 'ユーザ辞書が設定されていないため、追記できません'
        file = Path(self.PATTERN_CSV_PATH.format(Path(self.__user_dic).stem)).absolute()

        self.__optimize_user_word(str(file.stem))

        #TODO: 処理結果を報告
        print('ユーザ辞書から削除しました。ユーザ辞書:{0}'.format(self.__user_dic))

    def __optimize_user_word(self, user_dic):
        '''
        ユーザ辞書csvの内容を最適化する

        @param: user_dic
        @type:  str
        @rtype: bool
        '''
        file = Path(self.PATTERN_CSV_PATH.format(user_dic))
        if file.is_file():
            with file.open(mode='r', encoding='utf-8') as f:
                lines = f.readlines()

            line_set = set()
            for line in lines:
                line_set.add(line)

            lines_sorted = sorted(list(line_set))
            for append_text in lines_sorted:
                self.__write_csv(file.stem, append_text.strip())

    def get_parses(self, text):
        '''
        形態素解析結果を返す

        @param: text
        @type:  str
        @rtype: list
        '''
        rowParses = list()
        rowParses.append(self.HEADER)
        parses = self.__tagger.parse(text)
        rowParses.extend(parses.split('\n'))
        return [re.split(r'[\t,]', parse) for parse in rowParses if len(re.split(r'[\t,]', parse)) == 10]

    def sent_tokenize(self, text):
        '''
        文章のリストを返す

        @param: text
        @type:  str
        @rtype: list
        '''
        result = list()
        return result

    def word_tokenize(self, text):
        '''
        単語のリストを返す

        @param: text
        @type:  str
        @rtype: list(str)
        '''
        return [parse[0] for parse in self.get_parses(text)[1:]]
