#coding:utf-8
import requests
import json

host = "http://192.168.1.12"

def login(user,psw):
    # 拼接请求地址
    url = host + "/park-user-service/park/admin_user/login"
    # 设置请求头header信息
    h = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
        "Accept":"*/*",
        "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding":"gzip, deflate",
        "Content-Type":"application/json",
        "Content-Length":"54",
        "Connection":"keep-alive"
		}
    # 设置请求体参数
    body = {
        "userName": user,
        "password": psw
        }
    # 将请求体转换成json格式
    json_body = json.dumps(body)

    r1 = requests.post(url, data=json_body, headers=h)
    return [r1.content.decode("utf-8"), r1.encoding, r1.headers, r1.url] # 字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩


# def is_login_sucess(res):
#     if "账号不存在或密码错误" in res:
#         return False
#     elif "账户密码不能为空" in res:
#         return False
#     elif "操作成功" in res:
#         return True
#     else:
#         return False


if __name__  == "__main__":
    a = login("guochunhua","123456")
    #result = is_login_sucess(a)
    #print("测试结果：%s" %result)
    print("响应结果:{0}".format(a[0]))
    print("编码格式:{0}".format(a[1]))
    print("服务器响应头信息:{0}".format(a[2]))
    print("请求url:{0}".format(a[3]))



