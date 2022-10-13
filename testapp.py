#  coding=utf-8
#导入Flask类
from flask import Flask

#Flask类接受一个参数__name__
app = Flask(__name__)

#装饰器的作用是将路由映射到视图函数index,这里‘/’代表根目录
@app.route('/')
def index():
    return 'helloworld'

# Flask应用程序的run方法启动web服务器
if __name__ == '__main__':
    app.run(host='172.17.0.4',port=5000)

