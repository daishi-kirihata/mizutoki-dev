# -*- coding:utf-8 -*-
from module.interface.IDisposable import IDisposable
import openpyxl

class ExcelBase(IDisposable):
    def __init__(self):
        '''
        outline: 
        '''
        self.Book = None
        self.Sheet = None
        self.BookName = self.GetFileName('newExcel')

    def __del__(self):
        '''
        outline: 
        '''
        self.Dispose()

    def Dispose(self):
        '''
        outline:
        '''
        self.Sheet = None
        self.Book = None 
    
    def NewFile(self, fileName):
        '''
        outline: 
        '''
        self.BookName = self.GetFileName(fileName)
        self.Book = openpyxl.Workbook()
        self.Book.save(self.BookName)

    def OpenFile(self, fileName):
        '''
        outline: 
        '''
        self.BookName = self.GetFileName(fileName)
        self.Book = openpyxl.load_workbook(self.BookName)

    def SaveFile(self, fileName):
        '''
        outline: 
        '''
        self.Book.save(self.BookName)
    
    def GetFileName(self, fileName):
        '''
        outline: 
        '''
        return r'xlsx\{0}.xlsx'.format(fileName)
