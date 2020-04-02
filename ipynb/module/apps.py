# -*- coding:utf-8 -*-
from pathlib import Path
from docx import Document

class DocxApp():
    def __init__(self):
        self.__name = r'docx\{0}.docx'.format('newFile')
    
    def NewFile(self):
        document = Document()
        document.save(self.__name)
        print('作成しました。ファイル名: {0}'.format(self.__name))
