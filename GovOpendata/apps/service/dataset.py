from ..model.dataset import Dataset


def getDatasetList(gov_id=None, pageIndex=None, pageSize=None):
    data = dict()
    # 统计指定所属地区的数据集数量
    data_num = Dataset.query.filter_by(gov_id=gov_id).count()
    return data