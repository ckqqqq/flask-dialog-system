
from wudaoai.api_request import executeEngine, getToken
class WudaoApi():
    def __init__(self):
        self.api_key = "19465a4a8b81447e9fcdc83f1ef0c90f"
        self.public_key = "MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAOXDzzp81ron667QB57B1ce1WcVkhtlJ8Fk2Y+qLfGBN76CA3/H8EkQd7kVExkGSNnKlRuIv4Rwj2ambgbFqddECAwEAAQ=="
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
        resp = executeEngine(ability_type, engine_type, token, data)
        if resp!=None:#python 的not 和!=None
            print(resp)
            return resp
        else:
            print(resp,"寄了")
            return {"寄了":"寄"}

wudao=WudaoApi()
wudao.generate_response("爱了爱了")