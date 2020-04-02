# -*= coding:utf-8 -*-
from module.interface.IScraper import IScraper
from bs4 import BeautifulSoup

class ScraperBase(IScraper):
    def __init__(self):
        '''
        outline: 
        '''
        print('{0} : {1} 呼び出し'.format('ScraperBase', 'init'))
    
    def __del__(self):
        '''
        outline: 
        '''
        print('{0} : {1} 呼び出し'.format('ScraperBase', 'del'))
    
    def SaveWebText(self, html):
        '''
        outline: 
        '''
        print('{0} : {1} 呼び出し'.format('ScraperBase', 'SaveWebText'))
    
