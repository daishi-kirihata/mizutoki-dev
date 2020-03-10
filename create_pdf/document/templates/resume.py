# -*- coding: utf-8 -*-
from .templateBase import templateBase
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.pagesizes import A4, portrait
from reportlab.platypus import Table, TableStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from datetime import datetime, date, time, timedelta

class Resume(templateBase):
    def __init__(self):
        super(Resume, self).__init__()
        self.createDate = datetime.today()
        self.profile = {
            'nameSyllabaries':{
                'familyName':'family',
                'personalName':'name'
            },
            'name':{
            'familyName':'Family',
            'personalName':'Name'
            },
            'gender':True,
            'birthDate':date(1, 1, 1),
            'photo':None
        }
        self.contacts = [
            {
                'postalCode':'000-0000',
                'addressSyllabaries':'address syllabaries',
                'address':'address',
                'telephoneNumber':'0000-00-0000',
                'mailAddress':'sample@test.com'
            }
        ]
        self.histories = [
            {
                'yearAndMonth':date(1, 1, 1),
                'comment':None
            }
        ]
        self.licenses = [
            {
                'yearAndMonth':date(1, 1, 1),
                'comment':None
            }
        ]
        self.other = {
            'motivation':None,
            'commute':time(0, 0, 0),
            'dependentsNumber':0,
            'hasSpouse':False,
            'hasDutyToSupport':False,
            'request':None
        }
        
    def print_string(self):
        # フォント登録
        pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))
        # 用紙サイズ定義（この場合はA4）
        # width, height = A4

        self.createTitle(self.createDate)
        self.createProfile(self.profile)
        self.createContacts(self.contacts)
        self.createHistoriesAndLicenses(self.histories, self.licenses)
        self.createOther(self.other)
    
    def createTitle(self, createDate):
        # (1)履歴書 タイトル
        font_size = 24 # フォントサイズ
        self.pdf_canvas.setFont('HeiseiKakuGo-W5', font_size)
        self.pdf_canvas.drawString(60, 770, '履  歴  書') # 書き出し(横位置, 縦位置, 文字)

        # (2)作成日
        font_size = 10
        self.pdf_canvas.setFont('HeiseiKakuGo-W5', font_size)
        self.pdf_canvas.drawString(285, 770,  '{0}年 {1}月 {2}日現在'.format(createDate.year, createDate.month, createDate.day))

    def createProfile(self, profile):
        # (3) プロフィール
        data = [
            ['ふりがな', '{0} {1}'.format(profile['nameSyllabaries']['familyName'], profile['nameSyllabaries']['personalName']),'男  ・  女'],
            ['氏名', '', ''],
            ['', '{0} {1}'.format(profile['name']['familyName'], profile['name']['personalName']), ''],
            ['生年月日', '{0}年 {1}月 {2}日生　（満 {3} 歳）'.format(profile['birthDate'].year, profile['birthDate'].month, profile['birthDate'].day, self.calculateAge(profile['birthDate'])), '']
        ]
        table = Table(data, colWidths=(20*mm, 80*mm, 20*mm), rowHeights=(7*mm, 5*mm, 15*mm, 7*mm))
        table.setStyle(TableStyle([
            ('FONT', (0, 0), (-1, -1), 'HeiseiKakuGo-W5', 8),
            ('FONT', (1, 2), (1, 2), 'HeiseiKakuGo-W5', 16),
            ('BOX', (0, 0), (-1, -1), 1, colors.black),
            ('LINEBEFORE', (2, 0), (2, 2), 1, colors.black),
            ('LINEABOVE', (0, 1), (1, 1), 1 , colors.black),
            ('LINEABOVE', (0, 3), (2, 3), 1, colors.black),
            ('SPAN',(1, 3), (2, 3)),
            ('SPAN',(2, 0), (2, 2)),
            ('VALIGN', (0, 0), (2, 3), 'MIDDLE'),
            ('VALIGN', (0, 1), (0, 1), 'TOP'),
            ('ALIGN', (1, 0), (1, 2), 'CENTER'),
            ('ALIGN', (2, 0), (2, 2), 'CENTER'),
            ('ALIGN', (1, 3), (2, 3), 'RIGHT'),
        ]))
        table.wrapOn(self.pdf_canvas, 20*mm, 232*mm)
        table.drawOn(self.pdf_canvas, 20*mm, 232*mm)
        self.checkSelection(345, 705, profile['gender'])

        # (4)証明写真
        # tableを作成
        data = [['    証明写真'],]
        table = Table(data, colWidths=30*mm, rowHeights=40*mm) # tableの大きさ
        table.setStyle(TableStyle([                              # tableの装飾
            ('FONT', (0, 0), (0, 0), 'HeiseiKakuGo-W5', 12), # フォントサイズ
            ('BOX', (0, 0), (0, 0), 1, colors.black),        # 罫線
            ('VALIGN', (0, 0), (0, 0), 'MIDDLE'),            # フォント位置
        ]))
        table.wrapOn(self.pdf_canvas, 145*mm, 235*mm) # table位置
        table.drawOn(self.pdf_canvas, 145*mm, 235*mm)
        
    def createContacts(self, contacts):
        # (5)住所
        data = list()
        for i in range(2):
            if i < len(contacts):
                data.append(['ふりがな', contacts[i]['addressSyllabaries'], '電話 {0}'.format(contacts[i]['telephoneNumber'])])
                data.append(['連絡先（〒　{0}　）'.format(contacts[i]['postalCode']), '', 'E-mail'])
                data.append(['', contacts[i]['address'], contacts[i]['mailAddress']])
            else:
                data.append(['ふりがな', '', '電話'])
                data.append(['連絡先（〒　{0}　）'.format('　　-　　　'), '', 'E-mail'])
                data.append(['', '', ''])
        table = Table(data, colWidths=(20*mm, 100*mm, 40*mm), rowHeights=(7*mm, 5*mm, 15*mm, 7*mm, 5*mm, 15*mm))
        table.setStyle(TableStyle([
            ('FONT', (0, 0), (-1, -1), 'HeiseiKakuGo-W5', 9),
            ('BOX', (0, 0), (-1, -1), 1, colors.black),
            ('LINEABOVE', (0, 1), (2, 1), 1, colors.black),
            ('LINEABOVE', (0, 3), (2, 3), 1, colors.black),
            ('LINEABOVE', (0, 4), (2, 4), 1, colors.black),
            ('LINEBEFORE', (2, 0), (2, 5), 1, colors.black),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('VALIGN', (0, 1), (1, 1), 'TOP'),
            ('VALIGN', (0, 4), (1, 4), 'TOP'),
        ]))
        table.wrapOn(self.pdf_canvas, 20*mm, 178*mm)
        table.drawOn(self.pdf_canvas, 20*mm, 178*mm)

    def createHistoriesAndLicenses(self, histories, licenses):
        # (6)学歴・職歴
        index = 0
        data = list()
        data.append(['年', '月', '学歴・職歴'])
        for row in range(20):
            if index < len(histories):
                data.append([histories[index]['yearAndMonth'].year, histories[index]['yearAndMonth'].month, histories[index]['comment']])
                index += 1
            else:
                data.append(['', '', ''])
        table = Table(data, colWidths=(25*mm, 14*mm, 121*mm), rowHeights=7.5*mm)
        table.setStyle(TableStyle([
            ('FONT', (0, 0), (-1, -1), 'HeiseiKakuGo-W5', 11),
            ('BOX', (0, 0), (-1, -1), 1, colors.black),
            ('INNERGRID', (0, 0), (-1, -1), 1, colors.black),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('ALIGN', (0, 0), (1, -1), 'CENTER'),
            ('ALIGN', (2, 0), (2, 0), 'CENTER'),
        ]))
        table.wrapOn(self.pdf_canvas, 20*mm, 20*mm)
        table.drawOn(self.pdf_canvas, 20*mm, 20*mm)

        # 1枚目終了
        self.pdf_canvas.showPage()

        # (7)学歴・職歴、免許・資格
        data = list()
        data.append(['年', '月', '学歴・職歴'])
        for row in range(9):
            if index < len(histories):
                data.append([histories[index]['yearAndMonth'].year, histories[index]['yearAndMonth'].month, histories[index]['comment']])
                index += 1
            else:
                data.append(['', '', ''])
        index = 0
        data.append(['年', '月', '免許・資格'])
        for row in range(7):
            if index < len(licenses):
                data.append([licenses[index]['yearAndMonth'].year, licenses[index]['yearAndMonth'].month, licenses[index]['comment']])
                index += 1
            else:
                data.append(['', '', ''])

        table = Table(data, colWidths=(25*mm, 14*mm, 121*mm), rowHeights=7.5*mm)
        table.setStyle(TableStyle([
            ('FONT', (0, 0), (-1, -1), 'HeiseiKakuGo-W5', 11),
            ('BOX', (0, 0), (-1, -1), 1, colors.black),
            ('INNERGRID', (0, 0), (-1, -1), 1, colors.black),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('ALIGN', (0, 0), (1, -1), 'CENTER'),
            ('ALIGN', (2, 0), (2, 0), 'CENTER'),
            ('ALIGN', (2, 10), (2, 10), 'CENTER'),
        ]))
        table.wrapOn(self.pdf_canvas, 20*mm, 132*mm)
        table.drawOn(self.pdf_canvas, 20*mm, 132*mm)

    def createOther(self, other):
        # (8)そのほか
        data = [
            ['志望の動機、自己PR、趣味、特技など', '通勤時間', ''],
            ['', '約　{0}　時間　{1}　分'.format(other['commute'].hour, other['commute'].minute), ''],
            ['', '扶養家族（配偶者を除く）', ''],
            ['', '{0}　人'.format(other['dependentsNumber']), ''],
            ['', '配偶者', '配偶者の扶養義務'],
            ['', '有  ・  無', '有  ・  無'],
            ['本人希望記入欄（特に待遇・職種・勤務時間・その他についての希望などがあれば記入）', '', ''],
            ['', '', '']
        ]
        table = Table(data, colWidths=(90*mm, 35*mm, 35*mm), rowHeights=(8*mm, 10*mm, 8*mm, 10*mm, 8*mm, 10*mm, 8*mm, 50*mm))
        table.setStyle(TableStyle([
            ('FONT', (0, 0), (-1, -1), 'HeiseiKakuGo-W5', 10),
            ('BOX', (0, 0), (-1, -1), 1, colors.black),
            ('LINEBEFORE', (1, 0), (1, 5), 1, colors.black),
            ('LINEBEFORE', (2, 4), (2, 5), 1, colors.black),
            ('LINEABOVE', (1, 2), (2, 2), 1, colors.black),
            ('LINEABOVE', (1, 4), (2, 4), 1, colors.black),
            ('LINEABOVE', (0, 6), (2, 6), 1, colors.black),
            ('LINEABOVE', (0, 7), (2, 7), 1, colors.black),
            ('SPAN', (1, 1), (2, 1)),
            ('SPAN', (1, 3), (2, 3)),
            ('SPAN', (0, -1), (-1, -1)),
            ('VALIGN', (0, 0), (-1, 5), 'TOP'),
            ('VALIGN', (0, 6), (-1, 6), 'MIDDLE'),
            ('ALIGN', (1, 1), (2, 1), 'RIGHT'),
            ('ALIGN', (1, 3), (2, 3), 'RIGHT'),
            ('ALIGN', (1, 5), (2, 5), 'CENTER'),
        ]))
        table.wrapOn(self.pdf_canvas, 20*mm, 20*mm)
        table.drawOn(self.pdf_canvas, 20*mm, 20*mm)
        font_size = 24
        self.pdf_canvas.setFont('HeiseiKakuGo-W5', font_size)
        self.checkSelection(335, 230, other['hasSpouse'])
        self.checkSelection(432, 230, other['hasDutyToSupport'])
        #self.pdf_canvas.drawString(335, 230, '〇')
        #self.pdf_canvas.drawString(430, 230, '〇')
        
        # 2枚目終了
        self.pdf_canvas.showPage()

    def calculateAge(self, birthDate):
        age = self.createDate.year - birthDate.year
        if (self.createDate.month, self.createDate.day) < (birthDate.month, birthDate.day):
            age -= 1
        return age

    def checkSelection(self, hposition, vposition, isChecked):
        font_size = 24
        self.pdf_canvas.setFont('HeiseiKakuGo-W5', font_size)
        if not isChecked:
            hposition += 28
        self.pdf_canvas.drawString(hposition, vposition, '〇')

