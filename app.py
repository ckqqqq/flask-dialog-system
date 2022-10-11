from flask import Flask
from flask import request
from flask_cors import CORS
from flask_cors import cross_origin
from wudao_api.wudao_api import WudaoApi
from flask.views import MethodView #作为接口的输入
app=Flask(__name__)#实例化Flask
CORS(app, supports_credentials=True)#跨域请求
CORS().init_app(app)# 防止跨域的错误
CORS(app, supports_credentials=True)
class DialogApi(MethodView):
    def __init__(self):
        self.wudao_api = WudaoApi()
    def get(self, book_id):
        pass

    #跨域
    @cross_origin()
    def post(self,wudao_api=None):#封装POST
        print("POST")
        user_message = request.json.get('user_message')
        print(user_message)
        fake_response="这个是生成的回复"
        fake_response=self.wudao_api.generate_response(user_message)
        return {
            'status': 'success',
            'message': '已发送请求',
            'ai_response':fake_response
        }

dialog_api=DialogApi.as_view("dialog_api")
app.add_url_rule('/dialog/wudao/',view_func=dialog_api,methods=['POST',])

if __name__ == '__main__':
    app.run()
    #使用。env文件中的配置信息要 pip install python-dotenv
