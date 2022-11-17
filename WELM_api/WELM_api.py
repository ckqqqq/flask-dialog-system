#  coding=utf-8
# curl -H 'Content-Type: application/json' -H 'Authorization: Bearer your_api_token'  -d \
# ''
'''
curl -H 'Content-Type: application/json' -H 'Authorization: cchi48mv9mc753cgtfrg' https://welm.weixin.qq.com/v1/completions -d \
'{
    "prompt":"测试",
    "model":"xl",
    "max_tokens":16,
    "temperature":0.0,
    "top_p":0.0,
    "top_k":10,
    "n":1,
    "echo":false,
    "stop":",，.。"
}'
'''
import requests
class WELMApi():
    def __init__(self):
        self.headers = {
        # Already added when you pass json= but not when you pass data=
        # 'Content-Type': 'application/json',
        'Authorization': 'cchi48mv9mc753cgtfrg',
        }
        self.json_data = {
            'prompt': '',
            'model': 'xl',
            'max_tokens': 16,
            'temperature': 0,
            'top_p': 0,
            'top_k': 10,
            'n': 1,
            'echo': False,
            'stop': '\n',
        }
        self.history_dialog='''
李四，WELM生成模型。
张三，对话平台用户，具有多年机器学习研究经验。
张三：你好啊，我来试用对话大模型。
李四：欢迎欢迎。
张三：让我们开始对话吧。
李四：好呀！你是做什么工作的？
张三: 我是深度学习领域的研究者。
张三：你好可爱啊，我好喜欢。
李四：谢谢夸奖。你也很可爱。
'''
    def new_dialog():
        self.history_dialog=''''''
    def print_history(self):
        print("历史",self.history_dialog)
    def generate_response(self,message):
        self.history_dialog+="张三："+message+"\n"
        self.history_dialog+="李四："
        self.json_data['prompt']=self.history_dialog
        response = requests.post('https://welm.weixin.qq.com/v1/completions', headers=self.headers, json=self.json_data).json()       
        self.history_dialog+=response['choices'][0]['text']+"\n"
        return response['choices'][0]['text']
# 
# {'id': '91172ea1-649b-11ed-899b-525400637b45', 'object': 'text_generation', 'created': 1668485483, 'model': 'xl', 'choices': [{'text': '谢谢夸奖。', 'index': 0, 'logprobs': 0, 'finish_reason': 'finished'}]}
# welm_api=WELMApi()
# while(1):
#     print(welm_api.generate_response(input("输入对话：")))
#     welm_api.print_history()


