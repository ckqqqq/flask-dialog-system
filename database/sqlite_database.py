# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
'''一条对话信息'''
class Dialog(db.Model):
    __tablename__ = 'Dialog'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dialog_id = db.Column(db.String(255))
    speaker = db.Column(db.String(255))
    utterance = db.Column(db.String(255))
    emotion = db.Column(db.String(255))
    dialog_action = db.Column(db.String(255))
    user_id = db.Column(db.String(255))
    model_name=db.Column(db.String(255))
    '''静态的创建命令'''
    @staticmethod
    def init_db():
        rets = [
            (1, '对话ID', '对话者', '对话', '情感标签', '对话行为','账号','模型名称')
        ]
        for ret in rets:
            dialog = Dialog()
            dialog.id = ret[0]
            dialog.dialog_id = ret[1]
            dialog.speaker = ret[2]
            dialog.utterance = ret[3]
            dialog.emotion = ret[4]
            dialog.dialog_action = ret[5]
            dialog.user_id=ret[6]
            dialog.model_name=ret[7]
            db.session.add(dialog)
        db.session.commit()
    # @staticmethod
    def add_data(self,rets):
        # rets = [
        #     (2, '对话ID', 'ckq', '对话', '情感标签', '对话行为','ckq'),
        #     (66, '202256', 'WELMAPI', '你好', 'AI情感', 'ai对话行为', '202256')
        # ]
        # rets的一个范本，注意id不会添加
        for ret in rets:
            dialog = Dialog()
            # dialog.id = ret[0]
            dialog.dialog_id = ret[1]
            dialog.speaker = ret[2]
            dialog.utterance = ret[3]
            dialog.emotion = ret[4]
            dialog.dialog_action = ret[5]
            dialog.user_id=ret[6]
            dialog.model_name=ret[7]
            db.session.add(dialog)
        db.session.commit()
        