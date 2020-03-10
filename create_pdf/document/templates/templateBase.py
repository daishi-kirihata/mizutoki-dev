# -*- coding: utf-8 -*-
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.pagesizes import A4, portrait
from reportlab.platypus import Table, TableStyle
from reportlab.lib.units import mm
from reportlab.lib import colors

class templateBase():
    def __init__(self):
        self.pdf_canvas = None

    def make(self, filename="newfile"):
        self.pdf_canvas = self.set_info(filename)
        self.print_string()
        self.pdf_canvas.save()

    def set_info(self, filename):
        pdf_canvas = canvas.Canvas("./{0}.pdf".format(filename), pagesize=portrait(A4))
        pdf_canvas.setAuthor("") # 作者
        pdf_canvas.setTitle("") # 表題
        pdf_canvas.setSubject("") # 件名
        return pdf_canvas
    
    def print_string(self):
        # フォント登録
        pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))
        # 用紙サイズ定義（この場合はA4）
        width, height = A4
        # フォントサイズ定義（この場合は24）
        font_size = 24
        self.pdf_canvas.setFont('HeiseiKakuGo-W5', font_size)
        # 書き出す(横位置, 縦位置, 文字)を指定
        self.pdf_canvas.drawString(60, 770, 'サンプルドキュメント') 
        # 1枚目終了
        self.pdf_canvas.showPage()
