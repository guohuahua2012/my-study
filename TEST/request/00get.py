#coding:utf-8
import requests

# 请求百度首页，方法get请求
r = requests.get('http://www.baidu.com')

print(r.url) # 获取url
print(r.status_code) # 响应状态码
print(r.content) # 字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩
print(r.headers) # 以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
# print(r.json)
# print(r.encoding)
# print(r.cookies)
# print(r.raw)
# print(r.text)
# print(r.raise_for_status)