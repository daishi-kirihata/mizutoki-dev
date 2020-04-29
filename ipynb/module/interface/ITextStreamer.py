# -*- coding:utf-8 -*-
from abc import ABCMeta, abstractmethod
from module.interface.IDisposable import IDisposable

class ITextStreamer(IDisposable, metaclass = ABCMeta):
    @abstractmethod
    def readlines(self):
        pass

    @abstractmethod
    def write(self, text):
        pass

