 # 發送位置: https://notify-api.line.me/api/notify
 # token : 3X9wgC5R38xMLpMKhkYyDYZe1B6OYlR62CvmZqmKQgV (到這裡genarate token : https://notify-bot.line.me/my/)

import requests

if __name__ == '__main__':
    url = 'https://notify-api.line.me/api/notify'
    token = '3X9wgC5R38xMLpMKhkYyDYZe1B6OYlR62CvmZqmKQgV'
    headers = {
        "Authorization": "Bearer " + token
    }
#
    message = input('請輸入文字訊息內(1000字內):')
    params = {
        "message": message
    }

    resp = requests.post(url, headers=headers, params=params)
    print(resp)  # 若看到200代表回應 成功; 404 帶鰾 not found; 401 代表授權失敗
