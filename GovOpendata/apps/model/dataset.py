from ...apps import Base, db

class Dataset(Base):
    __tablename__ = 'dataset'
    gov_id = db.Column(db.Integer, comment="数据集所属得开放平台id")
    source = db.Column(db.String(255), comment="信息来源")
    subject = db.Column(db.String(255), comment="主题分类")
    update_date = db.Column(db.DateTime, comment="更新时间")
    acquire_date = db.Column(db.DateTime, comment="采集时间")
    abstract = db.Column(db.Text, comment="数据简介")
    view_num = db.Column(db.Integer, comment="浏览量")
    download_num = db.Column(db.Integer, comment="下载量")
    collect_num = db.Column(db.Integer, comment="收藏量")
    exract_info = db.Column(db.Text, comment="基础信息")
    field_info = db.Column(db.Text, comment="字段信息")
    path = db.Column(db.String(255), comment="数据文件子路径，用于查找文件及下载")

