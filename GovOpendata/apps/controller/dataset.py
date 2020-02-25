from flask import Blueprint, request
import json
from .. import app
from ...apps.service.dataset import *
from flask_restful import Resource
dataSetBp = Blueprint('dataSet', __name__)


class DatasetQueryController(Resource):
    def get(self):
        """
        点击省份查询数据信息
        :return:
        """
        pageIndex = int(request.args.get('pageIndex'))
        pageSize = int(request.args.get('pageSize'))
        gov_id = request.args.get('gov_id')
        data = getDatasetQueryList(gov_id=gov_id, pageIndex=pageIndex, pageSize=pageSize)
        return {'code': 200, 'data': data}
            
            
    def post(self):
        """
        新增
        :return:
        """
        pass

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


class DatasetSearchController(Resource):
    def get(self):
        """
        搜索关键词获取数据信息
        :return:
        """
        pageIndex = int(request.args.get('pageIndex'))
        pageSize = int(request.args.get('pageSize'))
        keyWord = request.args.get('keyWord')

        data = getDatasetSearchList(keyWord=keyWord, pageIndex=pageIndex, pageSize=pageSize)
        return {'code': 200, 'data': data}
    
    def post(self):
        """
        新增
        :return:
        """
        pass
    
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