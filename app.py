#  coding=utf-8

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
# CORS(app,  )   # 允许所有域名跨域
app=Flask(__name__)#实例化Flask
CORS(app,resources={r"/*": {"origins": "*"}})#跨域请求
CORS().init_app(app)# 防止跨域的错误
CORS(app, supports_credentials=True)
# @app.route('/')
# def printMsg():
#     app.logger.warning('testing warning log')
#     app.logger.error('testing error log')
#     app.logger.info('testing info log')
#     return"Check your console"

class DialogApi(MethodView):
    def __init__(self):
        self.wudao_api = WudaoApi()
    def get(self, book_id):
        pass

#   {'code': 200, 'msg': '操作成功', 'data': 
#   {'prompt': '据了解来看', 'promptDesc': None, 'outputText': '这个可以,我喜欢', 'inputTokenNum': 4, 'outputTokenNum': 8, 'totalTokenNum': 12, 'taskOrderNo': '1007481580151932671102976', 'taskStatus': 'SUCCESS', 'requestTaskNo': '1007481580151932671102976'}, 'success': True}
#   '''
    # 跨域
    def post(self):
        
        user_message = request.json.get('user_message')
        # ai_response=jsonify(self.wudao_api.generate_response(user_message))
        # resp=make_response(jsonify(ai_response),200)#状态码
        # resp.status="Success"
        # resp.headers["Access-Control-Allow-Origin"]="*"
        # resp.headers["content-type"]="application/json"
        # print(resp.headers)
        return self.wudao_api.generate_response(user_message)
    # def post(self):#封装POST
    #     print("POST")
    #     user_message = request.json.get('user_message')
    #     ai_response=self.wudao_api.generate_response(user_message)
    #     http_response=Response(json.dumps(ai_response), mimetype='application/json')
    #     http_response.status='success'
    #     http_response.headers["Access-Control-Allow-Origin"]="*"
    #     # http_response.headers['Access-Control-Allow-Origin'] = '*'
    #     # http_response.headers["Access-Control-Allow-Headers"]="Origin, X-Requested-With, Content-Type, Accept"
    #     http_response.status_code="200"
    #     http_response.status="Success"
    #     print(http_response.content_type)         #获取内容（文本和字符编码）
    #     print("http_response.headers",http_response.headers)              #响应头
    #     print("http_response.status_code",http_response.status_code)        # 200  状态码
    #     print("http_response.status",http_response.status)

        return http_response

dialog_api=DialogApi.as_view("dialog_api")
app.add_url_rule('/dialog/wudao/',view_func=dialog_api,methods=['POST',])

if __name__ == '__main__':
    app.debug=True
    print("开始跑了")
    app.run(host="172.17.0.4",port=5000)
    
    #使用。env文件中的配置信息要 pip install python-dotenv
