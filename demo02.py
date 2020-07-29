import requests
import base64
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

api_key = 'IMxY9nt4Nv3UCWw228tn2Dcg'
secret_key = '5CZ6t7pXGjN8p2mq4yQ3Keft3M7P685B'
url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + str(api_key) + '&client_secret=' + str(secret_key)
res = requests.get(url).text
a = eval(res)

access_token = a['access_token']
animal = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/car?access_token=' + str(access_token)
hearder = {'Content-Type':'application/x-www-form-urlencoded'}
data = {}
with open('2.png','rb') as f:
    image = base64.b64encode(f.read())
    data["image"] = str(image, 'utf-8')
    res2 = requests.post(url=animal,data=data,headers=hearder).text
    print(res2)
    print(eval(res2))
    print('颜色:', eval(res2)['color_result'])
    print('车型预测')
    for each in eval(res2)['result']:
        print(each['name'], '\t相似度：', each['score'])
    # plt.imshow(mpimg.imread(f))
plt.show()

