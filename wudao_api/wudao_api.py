#  coding=utf-8
import json
from wudaoai.api_request import executeEngine, getToken
class WudaoApi():
    def __init__(self):
        self.api_key = "1b44c7b1f5d84bec9f63aebb5c20bc4b"
        self.public_key = "MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAKJn4nDFNVmzRAofQwhKyCi3D7ujmzwPUrtb6r0JBdh928grXT7UF69UGJOuTC7tvYxzXz/go1JBY+/hZCFGTZECAwEAAQ=="
    def update_key(self,api_k,public_k):
        self.api_key=api_k
        self.public_key=public_k
    def generate_response(self,dialog):
        data = {
            "topP": 1,  # 核采样（必填）取值范围0～1
            "topK": 3,  # 采样（必填）取值范围1～10
            "temperature": 1,  # 概率分布调节（必填)取值范围0.5～1
            "noRepeatNgramSize": 3,  # 重复词去除（必填)取值范围0～20
            "repetitionPenalty": 1.2,  # 重复惩罚参数（必填)取值范围0.1～1.8
            "generatedLength": 128,  # 文本生成最大长度（必填)取值范围1～256
            "prompt": dialog,  # 输入内容（必填）取值范围1～200
        }
        # 鉴权token
        token = getToken(self.api_key, self.public_key)
        # 能力类型
        ability_type = "chat"
        # 引擎类型
        engine_type = "chat-general-engine-v1"
        try:
            resp = executeEngine(ability_type, engine_type, token, data)
            if resp!=None:#python 的not 和!=None
                print(resp)
        except Exception as e:
            print(e,"<-WUDAOapi 错误")
            return {"dada":{"outputText":str(e)}}
        else:
            return resp
            

wudao=WudaoApi()
res=wudao.generate_response("爱了爱了")
# print(res['data']['outputText'])
'''
{'code': 200, 'msg': '操作成功', 'data': {'prompt': '爱了爱了', 'promptDesc': None, 'outputText': '我的天啊,这也太美了吧!', 'inputTokenNum': 4, 'outputTokenNum': 13, 'totalTokenNum': 17, 'taskOrderNo': '1007481583819836075675648', 'taskStatus': 'SUCCESS', 'requestTaskNo': '1007481583819836075675648'}, 'success': True}
'''
# /https://open.wudaoai.com/additionalinformation