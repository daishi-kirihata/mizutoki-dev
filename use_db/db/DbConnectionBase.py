# -*- coding:utf-8 -*-
from .IDbConnection import IDbConnection
import configparser
import MySQLdb

class DbConnectionBase(IDbConnection):
    def __init__(self, ConfigName):
        self.__conn = None
        self.__cur = None
        self.ConfigName = ConfigName
        self.__config = configparser.ConfigParser()
        self.__config.read('config.ini', encoding = 'utf-8')
        self.__configSection = self.__config[self.ConfigName]
        ConnectionString = self.__configSection.get('connectionString')
        if ConnectionString is None:
            raise NameError('ConnectionString の取得値が取得できません。ConfigName:{0}'.format(self.ConfigName))
        self.ConnectionString = self.__TryParseToDict(ConnectionString)

    def __del__(self):
        self.Dispose()

    def Dispose(self):
        if self.__cur is not None:
            self.__cur.close()
            self.__cur = None
        if self.__conn is not None:
            try:
                self.__conn.close()
            except:
                pass
            self.__conn = None
    
    def Connect(self):
        if self.__conn is not None:
            raise Exception('既にDBへ接続済です。接続切断後に実行して下さい。')
        try:
            self.__conn = MySQLdb.connect(**self.ConnectionString)
            self.__conn.autocommit(True)
            self.__cur = self.__conn.cursor(MySQLdb.cursors.DictCursor)
        except:
            raise Exception('DBへの接続に失敗しました。')

    def BeginTransaction(self):
        try:
            self.__conn.autocommit(False)
            self.__conn.begin()
        except:
            raise Exception('既にトランザクションが開始済です。CommitTransaction かRollbackTransaction 後に実行して下さい。')

    def CommitTransaction(self):
        try:
            self.__conn.commit()
            self.__conn.autocommit(True)
        except:
            raise Exception('トランザクションが開始されていません。BeginTransaction 後に実行して下さい。')

    def RollbackTransaction(self):
        try:
            self.__conn.rollback()
            self.__conn.autocommit(True)
        except:
            raise Exception('トランザクションが開始されていません。BeginTransaction 後に実行して下さい。')

    def ExecuteDataSet(self, command):
        self.__cur.execute(command)
        return self.__cur

    def ExecuteNonQuery(self, command):
        self.__cur.execute(command)

    def ReadDataReader(self):
        pass

    def GetColumnNames(self):
        pass

    def GetCurrentValues(self):
        pass

    def __TryParseToDict(self, configString):
        result = dict()
        for part in configString.replace(' ', '').split(','):
            pair = part.split('=')
            result[pair[0]] = pair[1]
        return result
