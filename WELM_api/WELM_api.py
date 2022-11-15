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
            'stop': ',，.。',
        }
    def generate_response(self,dialog):
        self.json_data['prompt']=dialog
        response = requests.post('https://welm.weixin.qq.com/v1/completions', headers=self.headers, json=self.json_data)        
        return response.json()
welm_api=WELMApi()
dialog='''
        我：今天我们连线张三，请问张三你吗？ 好奇
        张三：当然。我是天下第一诗人。 开心 自豪
        我：我才是天下第一，就你？ 嫉妒
        张三：那当然，天下第一是官方认证的，我有证书 自豪
        我：哇，你太厉害了！ 崇拜 羡慕
        张三：
        '''
print(welm_api.generate_response(dialog))

