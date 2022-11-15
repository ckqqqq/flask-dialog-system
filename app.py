#  coding=utf-8
# 设定允许中文
import sys# 在控制台打印
import json
from flask import Flask
from flask import jsonify
from flask import request
from flask import Response,make_response
from flask_cors import CORS
from flask_cors import cross_origin
from wudao_api.wudao_api import WudaoApi
from flask.views import MethodView #作为接口的输入
from WELM_api import WELMApi
## 数据库模块
from sqlite_database import db
from sqlite_database import Dialog
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
    Dialog.init_db()
    
#装饰器的作用是将路由映射到视图函数index,这里‘/’代表根目录
@app.route('/')
def index():
    return 'helloworld'

class WudaoDialogApi(MethodView):
    def __init__(self):
        self.wudao_api = WudaoApi()
    def get(self):
        print(request.args.get("speaker"))
        print(request.args.get("dialog_id"))
        r_dialog_id=str(request.args.get("dialog_id"))
        r_speaker=request.args.get("speaker")
        if r_dialog_id=="all":
            #https://blog.csdn.net/zhongjianboy/article/details/110818577
            dialogs: [Dialog] = Dialog.query.filter_by(user_id=r_speaker).all()
            # .query.filter_by(s_age=22).all()
        else:
            dialogs:[Dialog]= Dialog.query.filter_by(user_id=r_speaker,dialog_id=r_dialog_id).all()
        results = [
            {
                'id': dialog.id,
                'dialog_id': dialog.dialog_id,
                'speaker': dialog.speaker,
                'utterance': dialog.utterance,
                'emotion': dialog.emotion,
                'dialog_action': dialog.dialog_action,
                'user_id':dialog.user_id
            } for dialog in dialogs
        ]
        return {
            'status': 'success',
            'message': '数据查询成功',
            'results': results
        }
    def post(self):
        #解包
        r_user_message = request.json.get('user_message')
        r_speaker=request.json.get("speaker")
        r_dialog_id=request.json.get("dialog_id")
        #存入用户数据
        user_dialog=Dialog()
        user_dialog.dialog_id=r_dialog_id
        user_dialog.speaker= r_speaker
        user_dialog.utterance=r_user_message
        user_dialog.emotion="用户情感"
        user_dialog.dialog_action="用户对话行为"
        user_dialog.user_id=r_dialog_id
        db.session.add(user_dialog)
        db.session.commit()
        #生成对话
        res=self.wudao_api.generate_response(r_user_message)
        # print(res['data']['outputText'])
        #ai数据存入数据库
        ai_response=Dialog()
        ai_response.dialog_id=r_dialog_id
        ai_response.speaker= "Wudao_API"
        if res['data']['outputText']!=None:
            ai_response.utterance=res['data']['outputText']
        else:
            ai_response.utterance=res['data']['outputText']="故障"
        ai_response.emotion="AI情感"
        ai_response.dialog_action="AI对话行为"
        ai_response.user_id=r_dialog_id
        db.session.add(ai_response)
        db.session.commit()
        return res
class WELMDialogApi(MethodView):
    def __init__(self):
        self.welm_api = WELMApi()
    def get(self):
        print(request.args.get("speaker"))
        print(request.args.get("dialog_id"))
        r_dialog_id=str(request.args.get("dialog_id"))
        r_speaker=request.args.get("speaker")
        if r_dialog_id=="all":
            #https://blog.csdn.net/zhongjianboy/article/details/110818577
            dialogs: [Dialog] = Dialog.query.filter_by(user_id=r_speaker).all()
            # .query.filter_by(s_age=22).all()
        else:
            dialogs:[Dialog]= Dialog.query.filter_by(user_id=r_speaker,dialog_id=r_dialog_id).all()
        results = [
            {
                'id': dialog.id,
                'dialog_id': dialog.dialog_id,
                'speaker': dialog.speaker,
                'utterance': dialog.utterance,
                'emotion': dialog.emotion,
                'dialog_action': dialog.dialog_action,
                'user_id':dialog.user_id
            } for dialog in dialogs
        ]
        return {
            'status': 'success',
            'message': '数据查询成功',
            'results': results
        }
    def post(self):
        #解包
        r_user_message = request.json.get('user_message')
        r_speaker=request.json.get("speaker")
        r_dialog_id=request.json.get("dialog_id")
        #存入用户数据
        user_dialog=Dialog()
        user_dialog.dialog_id=r_dialog_id
        user_dialog.speaker= r_speaker
        user_dialog.utterance=r_user_message
        user_dialog.emotion="用户情感"
        user_dialog.dialog_action="用户对话行为"
        user_dialog.user_id=r_dialog_id
        db.session.add(user_dialog)
        db.session.commit()
        #生成对话
        res=self.wudao_api.generate_response(r_user_message)
        # print(res['data']['outputText'])
        #ai数据存入数据库
        ai_response=Dialog()
        ai_response.dialog_id=r_dialog_id
        ai_response.speaker= "Wudao_API"
        if res['data']['outputText']!=None:
            ai_response.utterance=res['data']['outputText']
        else:
            ai_response.utterance=res['data']['outputText']="故障"
        ai_response.emotion="AI情感"
        ai_response.dialog_action="AI对话行为"
        ai_response.user_id=r_dialog_id
        db.session.add(ai_response)
        db.session.commit()
        return res
    
wudao_dialog_api=WudaoDialogApi.as_view("dialog_api")
app.add_url_rule('/dialog/wudao/',view_func=wudao_dialog_api,methods=['POST','GET',])
## Flask应用程序的run方法启动web服务器
if __name__ == '__main__':
    
    app.debug=True## 重要的是这些东西，而不是app run了
    print("开始跑了")
    app.run(host="0.0.0.0",port=5777)
    
    #使用。env文件中的配置信息要 pip install python-dotenv 重要的是这些东西
