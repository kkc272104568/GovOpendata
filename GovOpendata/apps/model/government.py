from ...apps import Base, db


class Government(Base):
    __tablename__ = 'governmment'
    acquire_date = db.Column(db.DateTime, comment="采集时间")
    dataset_num = db.Column(db.Integer, comment="数据集数量")
    file_num = db.Column(db.Integer, comment="文件数量")
    file_size = db.Column(db.Integer, comment="文件总大小")
    name = db.Column(db.String(255), comment="信息所属行政区域， 如贵阳市")
    path = db.Column(db.String(255), comment="数据文件路径，用于查找文件及下载")