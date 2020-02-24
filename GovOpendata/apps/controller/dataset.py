from flask import Blueprint, request
import json
from .. import app
from ...apps.service.dataset import *
from flask_restful import Resource
dataSetBp = Blueprint('dataSet', __name__)


class DatasetController(Resource):
    def get(self):
        """
        查询
        :return:
        """
        pageIndex = request.args.get('pageIndex', None)
        pageSize = request.args.get('pageSize', None)
        gov_id = request.args.get('gov_id', None)
        data = getDatasetList(gov_id=gov_id, pageIndex=pageIndex, pageSize=pageSize)
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