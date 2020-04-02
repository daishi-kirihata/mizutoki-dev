# -*- coding:utf-8 -*-
from module.interface.IMeCab import IMeCab
from pathlib import Path
import MeCab
import pandas
import re
import subprocess

class MeCabBase(IMeCab):
    MECAB_DICT_INDEX = r'c:\Program Files\MeCab\bin\mecab-dict-index.exe'
    MECAB_IPADIC = r'c:\Program Files\MeCab\dic\ipadic'
    HEADER = '表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音'

    def __init__(self):
        '''
        コンストラクタ MeCabBase
        '''
        self.__userDicName = None
        self.__pdUserDic = None
        self.__tagger = MeCab.Tagger()

    def __del__(self):
        '''
        デストラクタ MeCabBase
        '''
        self.__tagger = None
        self.__pdUserDic = None
        self.__userDicName = None

    def SetTagger(self, userDicName=None):
        '''
        Taggerを切り替える 

        @param: userDicName
        @type:  str
        @rtype: bool
        '''
        result = True
        taggerOption = None
        if userDicName:
            # TODO: ファイル存在チェック
            self.__userDicName = userDicName
            taggerOption = r'-u dic\{0}.dic'.format(self.__userDicName)

        if taggerOption:
            self.__tagger = MeCab.Tagger(taggerOption)
        else:
            self.__tagger = MeCab.Tagger()
        return result

    def GetParses(self, text):
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

    def CreateUserDictionary(self, fileName):
        '''
        ユーザ辞書を作成する

        @param: fileName
        @type:  str
        @rtype: bool
        '''
        # TODO: csvファイルの存在判定

        # TODO: self.__userDicNameの更新
        self.__userDicName = fileName

        # TODO: csvファイルの作成（ヘッダーの出力）
        file = open(r'csv\{0}.csv'.format(self.__userDicName), mode='w', encoding='utf-8')
        file.write('{0}\n'.format(self.HEADER))
        file.close()

        # TODO: dicファイルへのコンパイル処理
        return self.__CompileUserDictionary()

    def UpdateUserDictionary(self):
        '''
        ユーザ辞書を更新する

        @rtype: bool
        '''
        # TODO: csvファイルへの追記
        # TODO: dicファイルへのコンパイル処理
        # self.__pdUserDic = pandas.read_csv(self.__csvUerDic)
        # return self.__pdUserDic
        return self.__CompileUserDictionary()
        
    def __CompileUserDictionary(self):
        '''
        ユーザ辞書をcsvからdicへコンパイルする
        
        @rtype: bool
        '''
        result = True
        commands = list()
        commands.append(r'"{0}" -d "{1}" -u {2}.dic -f utf-8 -t utf-8 {2}.csv'.format(self.MECAB_DICT_INDEX, self.MECAB_IPADIC, self.__userDicName))
        commands.append(r'move {0}.dic .\dic'.format(self.__userDicName))
        for command in commands:
            # print(command)
            process = subprocess.run(
                command, 
                cwd=r'{0}\csv'.format(r'c:\Users\hajime\ipynb'), 
                shell=True, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE, 
                timeout=10)
            # print('({0})'.format(process.stdout.decode('cp932')))
            # print('({0})'.format(process.stderr.decode('cp932')))
        return result