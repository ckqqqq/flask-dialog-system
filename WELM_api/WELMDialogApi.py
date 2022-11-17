from flask.views import MethodView #作为接口的输入
from flask import request
from database.sqlite_database import Dialog
from WELM_api.WELM_api import WELMApi
# from app import db

class WELMDialogApi(MethodView):
    '''绑定get之流的'''
    def __init__(self,db):
        self.welm_api = WELMApi()
        
    def get(self):
        print(request.args.get("speaker")) 
        print(request.args.get("dialog_id"))
        # print(request.args.get("model_name"))
        r_dialog_id=str(request.args.get("dialog_id"))
        r_speaker=request.args.get("speaker")
        r_model_name=request.args.get("model_name")
        if r_dialog_id=="all":
            #https://blog.csdn.net/zhongjianboy/article/details/110818577
            dialogs: [Dialog] = Dialog.query.filter_by(user_id=r_speaker,model_name=r_model_name).all()
            # .query.filter_by(s_age=22).all()
        else:
            dialogs:[Dialog]= Dialog.query.filter_by(user_id=r_speaker,dialog_id=r_dialog_id,model_name=r_model_name).all()
        results = [
            {
                'id': dialog.id,
                'dialog_id': dialog.dialog_id,
                'speaker': dialog.speaker,
                'utterance': dialog.utterance,
                'emotion': dialog.emotion,
                'dialog_action': dialog.dialog_action,
                'user_id':dialog.user_id,
                'model_name':dialog.model_name
            } for dialog in dialogs
        ]
        return {
            'status': 'success',
            'message': '数据查询成功',
            'results': results
        }
    def post(self):
        self.db_handler=Dialog()
        #解包
        r_user_message = request.json.get('user_message')
        r_user_name=request.json.get("speaker")
        r_dialog_id=request.json.get("dialog_id")
        r_model_name=request.json.get("model_name")
        #存入用户数据
        # (2, '对话ID', '区分说话人', '对话', '情感标签', '对话行为','r_user_name(登陆账号)')
        user_tuple=(10086, r_dialog_id , r_user_name,r_user_message, '用户情感', '用户对话行为',r_user_name,r_model_name)
        #生成对话
        ai_response=self.welm_api.generate_response(r_user_message)
        # print(res['data']['outputText'])
        #ai数据存入数据库
        ai_tuple=(6666666, r_dialog_id,"WELM_API",ai_response, 'AI情感', 'ai对话行为',r_user_name,r_model_name)
        print([user_tuple,ai_tuple])
        self.db_handler.add_data([user_tuple,ai_tuple])
        print("WELM回复",ai_response)       
        return {'code': 200, 
                'msg': '操作成功', 
                'data': 
                    {'prompt': '爱了爱了',
                     'promptDesc': None, 
                     'outputText': ai_response,
                     'inputTokenNum': 4,
                     'outputTokenNum': 13, 
                     'totalTokenNum': 17, 
                     'taskOrderNo': '1007481583819836075675648',
                     'taskStatus': 'SUCCESS', 
                     'requestTaskNo': '1007481583819836075675648'},
                'success': True}