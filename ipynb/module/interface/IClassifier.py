# -*- coding:utf-8 -*-
from abc import ABCMeta, abstractmethod
from module.interface.IDisposable import IDisposable

class IClassifier(metaclass=ABCMeta):
    @abstractmethod
    def fit(self):
        pass

    @abstractmethod
    def visualize_classifier(self, title=''):
        pass
