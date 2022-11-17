#  coding=utf-8  
#  设定允许中文 
import sys# 在控制台打印
import json
from flask import Flask
# from flask import jsonify
from flask import request
from flask import Response,make_response
from flask_cors import CORS
from flask_cors import cross_origin
## 数据库模块
from database.sqlite_database import db,Dialog
from WELM_api.WELMDialogApi import WELMDialogApi
# CORS(app,  )   # 允许所有域名跨域
app=Flask(__name__)#实例化Flask,Flask类接受一个参数__name__
CORS(app,resources={r"/*": {"origins": "*"}})#跨域请求
CORS().init_app(app)# 防止跨域的错误
CORS(app, supports_credentials=True)
## 数据库模块
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dialog.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
@app.cli.command()## 绑定命令
def create():
    '''创建数据库'''
    db.drop_all()
    db.create_all()
    Dialog.init_db()#静态变量初始化
#装饰器的作用是将路由映射到视图函数index,这里‘/’代表根目录
@app.route('/')
def index():
    return 'helloworld'
# wudao_dialog_api=WudaoDialogApi.as_view("dialog_api")
# app.add_url_rule('/dialog/wudao/',view_func=wudao_dialog_api,methods=['POST','GET',])
welm_dialog_api=WELMDialogApi.as_view("dialog_api",db)
# welm_dialog_api.get_db(db)
app.add_url_rule('/dialog/welm/',view_func=welm_dialog_api,methods=['POST','GET',])

## Flask应用程序的run方法启动web服务器
if __name__ == '__main__':
    
    app.debug=True## 重要的是这些东西，而不是app run了
    print("开始跑了")
    app.run(host="0.0.0.0",port=5000)
    
    #使用。env文件中的配置信息要 pip install python-dotenv 重要的是这些东西
