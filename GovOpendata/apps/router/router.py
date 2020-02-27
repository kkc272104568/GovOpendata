from ...apps import restful_api
from ..controller.government import Gov
from ..controller.dataset import DatasetQueryController, DatasetSearchController
from ..controller.user import UserRegister,UserLogin


def regist_router():
    restful_api.add_resource(Gov, '/government')
    restful_api.add_resource(DatasetQueryController, '/dataset')
    restful_api.add_resource(DatasetSearchController, '/datasetSearch')
    restful_api.add_resource(UserRegister, '/register')
    restful_api.add_resource(UserLogin, '/login')