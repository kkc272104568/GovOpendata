import logging
import os
from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .. import config
from flask_login import LoginManager
from flask_restful import Api



app = Flask(__name__)
restful_api = Api(app)
app.config.from_object(config)

# 允许跨域请求
cors = CORS(app, resources=r'/*', supports_credentials=True)

# 显示中文
app.config['JSON_AS_ASCII'] = False

login_manager = LoginManager()  # 初始化flask_login
login_manager.session_protection = 'strong'  # 设置登录安全级别
login_manager.login_view = 'login'  # 指定了未登录时跳转的页面
login_manager.init_app(app)

# Logging
log = logging.getLogger()
log.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
app.logger.setLevel(app.config.get('LOG_LEVEL', "INFO"))
app.logger.addHandler(handler)

db = SQLAlchemy(app, session_options=dict(autocommit=False, autoflush=True))

@app.teardown_request
def teardown_request(exception):
    if exception:
        db.session.rollback()
        db.session.remove()
    db.session.remove()

'''
数据库的Base基类
定义了一些基础字段
'''
class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='favicon.icon')
# 创建数据库
from .model.government import *

# 蓝本注册
from .controller.government import governmentBp
app.register_blueprint(governmentBp)

from .controller.dataset import dataSetBp
app.register_blueprint(dataSetBp)

from .controller.user import userInfo
app.register_blueprint(userInfo)

def init_database():
    db.init_app(app)
    db.create_all()

from .router.router import regist_router
def initialize():
    '''
    app初始化, 初始化各个功能模块
    :return:
    '''
    init_database()
    regist_router()
