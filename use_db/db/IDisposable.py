# -*- coding:utf-8 -*-
from abc import ABCMeta, abstractmethod

class IDisposable(metaclass = ABCMeta):
    @abstractmethod
    def Dispose(self):
        pass
    