# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Dialog(db.Model):
        
    __tablename__ = 'Dialog'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dialog_id = db.Column(db.String(255))
    speaker = db.Column(db.String(255))
    utterance = db.Column(db.String(255))
    emotion = db.Column(db.String(255))
    dialog_action = db.Column(db.String(255))
    user_id = db.Column(db.String(255))
    @staticmethod
    def init_db():
        rets = [
            (1, '对话ID', 'ckq', '对话', '情感标签', '对话行为','ckq')
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
            db.session.add(dialog)
        db.session.commit()