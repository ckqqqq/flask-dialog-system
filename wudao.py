# coding=utf-8
from wudaoai.api_request import executeEngine, getToken

api_key = "b422c1b168fc42a1a914cba949f94e9b"
public_key = "MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAOqPlzil94UzSH1cx2RAJbkWyM63nCacNLUQts0eA/xZGgr2bMTmyC59VClnI0QsG2w+UVMYpoDyfgu1NsEXTFkCAwEAAQ=="
    # 鉴权token
token = getToken(api_key, public_key)
    # 能力类型
ability_type = "chat"
    # 引擎类型
engine_type = "chat-general-engine-v1"

data = {
    "topP": 1,  # 核采样（必填）取值范围0～1
    "topK": 3,  # 采样（必填）取值范围1～10
    "temperature": 1,  # 概率分布调节（必填)取值范围0.5～1
    "noRepeatNgramSize": 3,  # 重复词去除（必填)取值范围0～20
    "repetitionPenalty": 1.2,  # 重复惩罚参数（必填)取值范围0.1～1.8
    "generatedLength": 128,  # 文本生成最大长度（必填)取值范围1～256
    "prompt": "特朗普会当上总统吗",  # 输入内容（必填）取值范围1～200
    }
resp = executeEngine(ability_type, engine_type, token, data)
print(resp)
