# -*- coding:utf-8 -*-
from abc import ABCMeta, abstractmethod

class IScraper(metaclass = ABCMeta):
    @abstractmethod
    def SaveWebText(self, html):
        '''
        @param:
        @type:
        @rtype: bool
        '''
        pass