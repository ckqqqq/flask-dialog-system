from flask.views import MethodView #作为接口的输入
from flask import request
from ..database.sqlite_database import Dialog
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
        # {'code': 200, 'msg': '操作成功', 'data': {'prompt': '爱了爱了', 'promptDesc': None, 'outputText': '我的天啊,这也太美了吧!', 'inputTokenNum': 4, 'outputTokenNum': 13, 'totalTokenNum': 17, 'taskOrderNo': '1007481583819836075675648', 'taskStatus': 'SUCCESS', 'requestTaskNo': '1007481583819836075675648'}, 'success': True}
        return res