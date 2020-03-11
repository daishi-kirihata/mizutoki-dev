# -*- coding:utf-8 -*-
from abc import ABCMeta, abstractmethod
from .IDisposable import IDisposable

class IDbConnection(IDisposable, metaclass = ABCMeta):
    @abstractmethod
    def Connect(self):
        pass

    @abstractmethod
    def BeginTransaction(self):
        pass

    @abstractmethod
    def CommitTransaction(self):
        pass

    @abstractmethod
    def RollbackTransaction(self):
        pass

    @abstractmethod
    def ExecuteDataSet(self, sql):
        pass

    @abstractmethod
    def ExecuteNonQuery(self, sql):
        pass

    @abstractmethod
    def ReadDataReader(self):
        pass

    @abstractmethod
    def GetColumnNames(self):
        pass

    @abstractmethod
    def GetCurrentValues(self):
        pass
