# -*- coding:utf-8 -*-

class appForTestModule():
    def __init__(self):
        '''
        outline: 
        '''
        self.name = None
    
    def call(self, name):
        '''
        outline: 
        '''
        self.name = name
        print('hello! {0}'.format(self.name))
