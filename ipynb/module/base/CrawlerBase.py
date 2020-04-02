# -*= coding:utf-8 -*-
from module.interface.ICrawler import ICrawler
from urllib import parse
from urllib.request import urlopen

class CrawlerBase(ICrawler):
    def __init__(self):
        '''
        outline: 
        '''
        print('{0} : {1} 呼び出し'.format('CrawlerBase', 'init'))
    
    def __del__(self):
        '''
        outline: 
        '''
        print('{0} : {1} 呼び出し'.format('CrawlerBase', 'del'))
    
    def GetHTML(self):
        '''
        outline: 
        '''
        print('{0} : {1} 呼び出し'.format('CrawlerBase', 'GetHTML'))
