#!/usr/bin/env python
# encoding: utf-8
# Author: FlyWen

import urllib2
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#获取微信企业号的token
def get_token(id, secrect):
    #id = wx1009c4a861b4b621
    #secrect = bSW9BMiUbOywdfzOqAuGXUBSIEmUeP0BOaoP3x9S0lvsnICFaAz1FLsaBxK3FC3d
    geturl = urllib2.urlopen('https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s' %(id, secrect))
    getjson = json.loads(geturl.read())
    return getjson['access_token']

#组装信息内容并发送到微信企业号
def info2wechat(token, touser, content):
    data = {
        "touser": touser,
        "msgtype": "text",
        "agentid": 1,
        "text": {
            "content": content
        }
    }
    #使用ensure_ascii，否则中文转json时会变ascii
    jdata = json.dumps(data, ensure_ascii=False)
    req = urllib2.Request('https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s' %token, jdata)
    resp = urllib2.urlopen(req)
    return resp.read()

#企业号中定义的id等
id = 'wx1009c4a861b4b621'
secrect = 'bSW9BMiUbOywdfzOqAuGXUBSIEmUeP0BOaoP3x9S0lvsnICFaAz1FLsaBxK3FC3d'
token = get_token(id, secrect)
#获取zabbix传来的参数，2是标题，不需要使用
touser = sys.argv[1]
content = sys.argv[3]
info2wechat(token, touser, content)

