from ...apps import restful_api
from ..controller.government import Gov
from ..controller.dataset import DatasetController


def regist_router():
    restful_api.add_resource(Gov, '/')
    restful_api.add_resource(DatasetController, '/dataset')