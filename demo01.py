# coding:utf-8
# 这是一个微信自动回复小程序
from PyWeChatSpy import WeChatSpy
import requests

def get_reply(data):
    url = f"http://api.douqq.com/?key=TE90PXVRMG5rMXlmN1lnV29QZT1XbmJoU2h3QUFBPT0&msg={data}"  # key获取地址http://xiao.douqq.com/
    resp = requests.get(url)
    return resp.text

def my_parser(data):

    if data['type'] == 100:
        print('socket连接成功')

    if data['type'] == 200:
        print('Spy正在监听...')

    # 联系人详情
    if data['type'] == 2:
        pass

    # 联系人列表
    if data['type'] == 3:
        pass

    # 群成员列表
    if data['type'] == 4:
        pass

    # 微信消息
    if data['type'] == 5:
        for item in data['data']:   #{"self":0,"msg_type":1,"wxid1":"","wxid2":"","head":"","content":""}
            if item['self'] == 0:   #消息由他人发出
                if item['wxid2'] is None and item['msg_type'] == 1:   # 消息来源是联系人好友，且消息类型是文本
                    who = item['wxid1']
                    what = get_reply(item['content'])
                    # wcp.send_text(who,what)
            if item['self'] == 1:   #消息由当前登录账号发出
                pass


    # 联系人最新信息
    if data['type'] == 6:
        pass

    # 联系人状态
    if data['type'] == 7:
        print("联系人状态")
        
    if data['type'] == 8:
        pass

wcp = WeChatSpy(parser=my_parser)
wcp.run()
