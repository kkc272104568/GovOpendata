#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   user.py    
@Auther  :  will_kkc 
@data    :  2020/2/26 18:14
@descr   :
'''

from flask import Blueprint, request
import json
from .. import app
from ...apps.service.user import *
from flask_restful import Resource
userInfo = Blueprint('userinfo', __name__)


class UserRegister(Resource):

	def get(self):
		"""
		查询
		:return:
		"""

	def post(self):
		"""
		新增用户信息
		:return:
		"""
		user_info = dict()
		user_info['login_name'] = request.args.get('login_name', None)
		user_info['login_password'] = request.args.get('login_password', None)
		user_info['real_name'] = request.args.get('real_name', None)
		user_info['phone_number'] = request.args.get('phone_number', None)
		user_info['email'] = request.args.get('email', None)
		user_info['career'] = request.args.get('career', None)
		
		data = userRegister(user_info=user_info)
		
		return {'code': 200, 'data': data}
	
	
	def put(self, sid):
		"""
		更新
		:return:
		"""
		pass
	
	
	def delete(self, sid):
		"""
		删除
		:param todo_id:
		:return:
		"""
		pass


class UserLogin(Resource):
	def get(self):
		"""
		查询
		:return:
		"""
	
	def post(self):
		"""
		新增用户信息
		:return:
		"""
		user_info = dict()
		user_info['login_name'] = request.args.get('login_name', None)
		user_info['login_password'] = request.args.get('login_password', None)
		data = userLogin(user_info=user_info)
		return {'code': 200, 'data': data}
	
	def put(self, sid):
		"""
		更新
		:return:
		"""
		pass
	
	def delete(self, sid):
		"""
		删除
		:param todo_id:
		:return:
		"""
		pass