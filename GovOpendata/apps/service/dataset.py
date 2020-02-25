from ..model.dataset import Dataset
from ...apps import db


def getDatasetQueryList(gov_id=None, pageIndex=None, pageSize=None):
    """
    # 获取query对应的数据结果
    :param gov_id:
    :param pageIndex:
    :param pageSize:
    :return:
    """
    
    result = dict()
    data_info = list()
    
    # 获取搜索结果总数
    nums = db.session.query(db.func.count(Dataset.gov_id)).filter(Dataset.gov_id == gov_id).scalar()
    
    # 根据pageIndex、pageSize参数分页显示数据结果，查询-》筛选—》排序-》分页显示
    data_page_info = db.session.query(Dataset).\
        filter(Dataset.gov_id == gov_id).\
        order_by(Dataset.date_created.desc()).\
        paginate(pageIndex, pageSize, False).items
    
    for data in data_page_info:
        data_info.append(obj2dict(data))
    
    # 将输出结果返回
    result['nums'] = str(nums)
    result['data_page_info'] = data_info
    return result


def getDatasetSearchList(keyWord=None, pageIndex=None, pageSize=None):
    """
	 # 获取search对应的数据结果
	 :param gov_id:
	 :param pageIndex:
	 :param pageSize:
	 :return:
	 """

    result = dict()
    data_info = list()

    # 获取搜索结果总数
    nums = db.session.query(Dataset).filter(Dataset.path.like("%"+keyWord+"%")).count()

    data_page_info = db.session.query(Dataset).\
        filter(Dataset.path.like("%"+keyWord+"%")).\
        order_by(Dataset.date_created.desc()).\
        paginate(pageIndex, pageSize, False).items
    
    for data in data_page_info:
        data_info.append(obj2dict(data))
    
    # 将输出结果返回
    result['nums'] = str(nums)
    result['data_page_info'] = data_info

    return result




def obj2dict(obj):
    """
    列表信息转字典
    :param obj:
    :return:
    """
    dic = {}
    for column in obj.__table__.columns:
        dic[column.name] = str(getattr(obj, column.name))
    return dic
