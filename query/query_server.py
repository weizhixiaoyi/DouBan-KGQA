# -*- coding:utf-8 -*-

import web
import hashlib
from weixin import receive, reply
from query_main import Query

query = Query()

class Handle(object):
    def __init__(self):
        # 初始化query
        #  self.query = Query()
        pass

    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            # 和公众平台官网-->基本配置中信息填写相同
            token = "douban_kgqa"

            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print("handle/GET func: hashcode, signature: ", hashcode, signature)
            if hashcode == signature:
                return echostr
            else:
                return "I don't Know"
        except Exception as err:
            print('ERROR: ' + str(err))
            return err

    def POST(self):
        try:
            webData = web.data()
            # 后台打印日志
            print('Handle Post webdata is ', webData)
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.MsgType == 'text':
                    # result = "彩虹屁屁"
                    question = recMsg.Content
                    result = query.parse(question)
                    replyMsg = reply.TextMsg(toUser, fromUser, result)
                    return replyMsg.send()
                if recMsg.MsgType == 'image':
                    mediaId = recMsg.MsgId
                    replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                    return replyMsg.send()
                else:
                    return reply.Msg().send()
            else:
                print('暂且不处理')
            return reply.Msg().send()
        except Exception as err:
            print('ERROR: ' + str(err))
            return err


urls = (
    '/douban_kgqa', 'Handle'
)

if __name__ == '__main__':
    douban_kgqa_web = web.application(urls, globals())
    douban_kgqa_web.run()
