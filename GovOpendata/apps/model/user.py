#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   user.py    
@Auther  :  will_kkc 
@data    :  2020/2/26 17:45
@descr   :
'''

from ...apps import Base, db

class User(Base):
    __tablename__ = 'user'
    login_name = db.Column(db.String(255), comment="用户登陆名")
    login_password = db.Column(db.String(255), comment="用户登陆密码")
    real_name = db.Column(db.String(255), comment="真实姓名")
    phone_number = db.Column(db.String(255), comment="手机号码")
    email = db.Column(db.String(255), comment="电子邮箱")
    id_card = db.Column(db.String(255), comment="身份证号码")
    career = db.Column(db.String(255), comment="职业")
    
    
