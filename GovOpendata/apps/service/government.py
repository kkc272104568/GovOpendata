from ..model.government import Government
from ...apps import db
from sqlalchemy import func


def dataStatistics(pageIndex=None, pageSize=None):
    # 对数据集求和
    dataset_num = db.session.query(func.sum(Government.dataset_num)).scalar()
    # 对文件求和
    file_num = db.session.query(func.sum(Government.file_num)).scalar()
    # 对文件大小求和
    file_size = db.session.query(func.sum(Government.file_size)).scalar()
    # 分组统计
    governmentList = db.session.query(Government.name, Government.path, Government.id).group_by(Government.path).all()
    data = dict()
    data['dataset_num'] = int(dataset_num)
    data['file_num'] = int(file_num)
    data['file_size'] = int(file_size)
    data['governmentList'] = governmentList
    return data
