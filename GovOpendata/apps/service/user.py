#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   user.py    
@Auther  :  will_kkc 
@data    :  2020/2/27 9:44
@descr   :
'''

from ..model.user import User
from ...apps import db
from sqlalchemy import func,or_,and_



def userRegister(user_info =None):
	'''
	监测用户信息是否存在，同时新增用户信息
	:param user_info:
	:return:
	'''
	
	data = dict()
	query = User.query.filter(User.login_name == user_info['login_name']).count()
	if query == 0:
		new_user = User(login_name=user_info['login_name'],
		                login_password=user_info['login_password'],
		                real_name=user_info['real_name'],
		                phone_number=user_info['phone_number'],
		                email=user_info['email'],
		                career=user_info['career'])
		db.session.add(new_user)
		db.session.commit()
		
		data['result'] = '注册成功！'
	else:
		data['result'] = '用户名重复，注册失败！'

	return data
	
	

def userLogin(user_info =None):
	'''
	监测用户账号正确性，同时登陆用户账号
	:return:
	'''
	data = dict()
	query = User.query.filter(and_(User.login_name == user_info['login_name'],
	                          User.login_password == user_info['login_password'])).first()
	if query:
		data['result'] = 'success,登陆成功！'
	else:
		data['result'] = 'false,账号或密码错误！'
	return data
