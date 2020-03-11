# -*- coding: utf-8 -*-
from document.templates import resume
from datetime import datetime, date, time

file = resume.Resume()
file.createDate = datetime.today()
file.profile = {
    'nameSyllabaries':{
        'familyName':'きりはた',
        'personalName':'だいし'
    },
    'name':{
        'familyName':'桐畑',
        'personalName':'大志'
    },
    'gender':True,
    'birthDate':date(1991, 2, 3),
    'photo':None
}qui
file.contacts = [
    {
        'postalCode':'529-0523',
        'addressSyllabaries':'しがけんながはましよごちょうかわなみ',
        'address':'滋賀県長浜市余呉町川並620番地',
        'telephoneNumber':'0749-86-3118',
        'mailAddress':'hajime.jizo@gmail.com'
    }
]
file.histories = [
    {
        'yearAndMonth':date(2009, 3, 1),
        'comment':'滋賀県立伊香高等学校 卒業'
    },
    {
        'yearAndMonth':date(2009, 4, 1),
        'comment':'京都産業大学 理学部 数理科学科 入学'
    },
    {
        'yearAndMonth':date(2013, 3, 1),
        'comment':'京都産業大学 理学部 数理科学科 卒業'
    },
    {
        'yearAndMonth':date(2013, 4, 1),
        'comment':'金沢大学大学院 自然科学研究科 数物科学専攻 入学'
    },
    {
        'yearAndMonth':date(2015, 3, 1),
        'comment':'金沢大学大学院 自然科学研究科 数物科学専攻 修了'
    },
    {
        'yearAndMonth':date(2015, 4, 1),
        'comment':'株式会社トライグループ 入社'
    },
    {
        'yearAndMonth':date(2020, 3, 1),
        'comment':'株式会社トライグループ 退社'
    }
]
file.licenses = [
    {
        'yearAndMonth':date(2013, 3, 1),
        'comment':'高等学校教諭一種免許状（情報）取得'
    },
    {
        'yearAndMonth':date(2015, 3, 1),
        'comment':'中学校教諭専修免許状（数学）取得'
    },
    {
        'yearAndMonth':date(2015, 3, 1),
        'comment':'高等学校教諭専修免許状（数学）取得'
    },
]
file.other = {
            'motivation':'',
            'commute':time(0, 30, 0),
            'dependentsNumber':0,
            'hasSpouse':False,
            'hasDutyToSupport':False,
            'request':''
}

file.make(file.profile['name']['familyName'] + file.profile['name']['personalName'])
