# -*- coding:utf-8 -*-
from abc import ABCMeta, abstractmethod

class IMeCab(metaclass=ABCMeta):
    @abstractmethod
    def sent_tokenize(self, text):
        '''
        outline:
        '''
        pass

    @abstractmethod
    def word_tokenize(self, text):
        '''
        outline:
        '''
        pass
    
    @abstractmethod
    def get_parses(self, text):
        '''
        outline:
        '''
        pass

    @abstractmethod
    def new_user_dic(self, file_name):
        '''
        outline:
        '''
        pass

    @abstractmethod
    def update_user_dic(self):
        '''
        outline:
        '''
        pass

    @abstractmethod
    def delete_user_dic(self, file_name):
        '''
        outline:
        '''
        # TODO: インスタンスが参照中の辞書が指定されている場合はエラーを返す

        pass

    @abstractmethod
    def append_user_word(self):
        '''
        outline:
        '''
        pass

    @abstractmethod
    def remove_user_word(self):
        '''
        outline:
        '''
        pass
