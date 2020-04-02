# -*- coding:utf-8 -*-
from abc import ABCMeta, abstractmethod
from urllib import parse
from urllib.request import urlopen

class ICrawler(metaclass = ABCMeta):
    @abstractmethod
    def GetHTML(self):
        '''
        @param: 
        @type: 
        @rtype: 
        '''
        pass
