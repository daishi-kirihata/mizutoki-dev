# -*- coding:utf-8 -*-
from db import DbConnectionBase
import MySQLdb

db = DbConnectionBase.DbConnectionBase('TEST')
db.Connect()

db.BeginTransaction()
sql = 'TRUNCATE TABLE TEST'
db.ExecuteNonQuery(sql)
db.CommitTransaction()

db.BeginTransaction()
sql = 'INSERT INTO TEST VALUES(5, \'youmu\')'
db.ExecuteNonQuery(sql)
db.RollbackTransaction()

db.BeginTransaction()
sql = 'INSERT INTO TEST VALUES(1, \'reimu\'), (2, \'marisa\'), (3, \'youmu\')'
db.ExecuteNonQuery(sql)
db.CommitTransaction()

sql = 'SELECT id, name FROM TEST'
cur = db.ExecuteDataSet(sql)
result = cur.fetchall()
print(result)

db.Dispose()