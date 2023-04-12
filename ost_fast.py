#!/usr/bin/python3
# -*- coding:utf-8 -*-
import time

from fileupload import seve_file
import requests
import datetime
import hashlib
import base64
import hmac
import json
import os
import re

# path_pwd = os.path.split(os.path.realpath(__file__))[0]
# os.chdir(path_pwd)


# 创建和查询
class FastAudioToText(object):
    def __init__(self, appid, apikey, apisecret, file_path=r"./record.wav"):
        # 以下为POST请求
        self.Host = "ost-api.xfyun.cn"
        self.RequestUriCreate = "/v2/ost/pro_create"
        self.RequestUriQuery = "/v2/ost/query"
        # 设置url
        if re.match("^\d", self.Host):
            self.urlCreate = "http://" + self.Host + self.RequestUriCreate
            self.urlQuery = "http://" + self.Host + self.RequestUriQuery
        else:
            self.urlCreate = "https://" + self.Host + self.RequestUriCreate
            self.urlQuery = "https://" + self.Host + self.RequestUriQuery
        self.HttpMethod = "POST"
        self.APPID = appid
        self.Algorithm = "hmac-sha256"
        self.HttpProto = "HTTP/1.1"
        self.UserName = apikey
        self.Secret = apisecret

        # 设置当前时间
        cur_time_utc = datetime.datetime.utcnow()
        self.Date = self.httpdate(cur_time_utc)
        # 设置测试音频文件
        self.BusinessArgsCreate = {
            "language": "zh_cn",
            "accent": "mandarin",
            "domain": "pro_ost_ed",
            # "callback_url": "http://IP:端口号/xxx/"
        }
        self.fileurl = ""
        self.file_path = file_path

    def img_read(self, path):
        with open(path, 'rb') as fo:
            return fo.read()

    def hashlib_256(self, res):
        m = hashlib.sha256(bytes(res.encode(encoding='utf-8'))).digest()
        result = "SHA-256=" + base64.b64encode(m).decode(encoding='utf-8')
        return result

    def httpdate(self, dt):
        """
        Return a string representation of a date according to RFC 1123
        (HTTP/1.1).
        The supplied date must be in UTC.
        """
        weekday = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"][dt.weekday()]
        month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep",
                 "Oct", "Nov", "Dec"][dt.month - 1]
        return "%s, %02d %s %04d %02d:%02d:%02d GMT" % (weekday, dt.day, month,
                                                        dt.year, dt.hour, dt.minute, dt.second)

    def generateSignature(self, digest, uri):
        signature_str = "host: " + self.Host + "\n"
        signature_str += "date: " + self.Date + "\n"
        signature_str += self.HttpMethod + " " + uri \
                         + " " + self.HttpProto + "\n"
        signature_str += "digest: " + digest
        signature = hmac.new(bytes(self.Secret.encode('utf-8')),
                             bytes(signature_str.encode('utf-8')),
                             digestmod=hashlib.sha256).digest()
        result = base64.b64encode(signature)
        return result.decode(encoding='utf-8')

    def init_header(self, data, uri):
        digest = self.hashlib_256(data)
        sign = self.generateSignature(digest, uri)
        auth_header = 'api_key="%s",algorithm="%s", ' \
                      'headers="host date request-line digest", ' \
                      'signature="%s"' \
                      % (self.UserName, self.Algorithm, sign)
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Method": "POST",
            "Host": self.Host,
            "Date": self.Date,
            "Digest": digest,
            "Authorization": auth_header
        }
        return headers

    def get_create_body(self, fileurl):
        post_data = {
            "common": {"app_id": self.APPID},
            "business": self.BusinessArgsCreate,
            "data": {
                "audio_src": "http",
                "audio_url": fileurl,
                "encoding": "raw"
            }
        }
        body = json.dumps(post_data)
        return body

    def get_query_body(self, task_id):
        post_data = {
            "common": {"app_id": self.APPID},
            "business": {
                "task_id": task_id,
            },
        }
        body = json.dumps(post_data)
        return body

    def call(self, url, body, headers):

        try:
            response = requests.post(url, data=body, headers=headers, timeout=8)
            status_code = response.status_code
            interval = response.elapsed.total_seconds()
            if status_code != 200:
                info = response.content
                return info
            else:
                resp_data = json.loads(response.text)
                return resp_data
        except Exception as e:
            print("Exception ：%s" % e)

    def task_create(self):
        body = self.get_create_body(self.fileurl)
        headers_create = self.init_header(body, self.RequestUriCreate)
        task_id = self.call(self.urlCreate, body, headers_create)
        print(task_id)
        return task_id

    def task_query(self, task_id):
        if task_id:
            body = self.get_create_body(self.fileurl)
            query_body = self.get_query_body(task_id)
            headers_query = self.init_header(body, self.RequestUriQuery)
            result = self.call(self.urlQuery, query_body, headers_query)
            return result

    def get_fileurl(self, file_path):
        # 文件上传
        print(file_path)
        api = seve_file.SeveFile(app_id="30ca75f9", api_key="1930f11e0a9570447909d02afbc6f5a2",
              api_secret="Mjc1NTQwODZkNGJmNDE5N2RmZmVmOWRl", upload_file_path=file_path)
        file_total_size = os.path.getsize(file_path)
        if file_total_size < 31457280:
            print("-----不使用分块上传-----")
            fileurl = api.gene_params('/upload')['data']['url']
        else:
            print("-----使用分块上传-----")
            fileurl = api.gene_params('/mpupload/upload')
        self.fileurl = fileurl

    def get_result(self):
        self.get_fileurl(file_path=self.file_path)
        # 创建订单
        print("\n------ 创建任务 -------")
        task_id = self.task_create()['data']['task_id']
        # 查询任务
        print("\n------ 查询任务 -------")
        print("任务转写中······")
        while True:
            result = self.task_query(task_id)
            if isinstance(result, dict) and result['data']['task_status'] != '1' and result['data'][
                'task_status'] != '2':
                print("转写完成···\n", json.dumps(result, ensure_ascii=False))
                break
            elif isinstance(result, bytes):
                print("发生错误···\n", result)
                break
        # result_list = eval(json.dumps(result, ensure_ascii=False))\
        #             ["data"]["result"]["lattice"][0]["json_1best"]["st"]["rt"][0]["ws"]
        try:
            result_list = eval(json.dumps(result, ensure_ascii=False))\
                        ["data"]["result"]["lattice"] #  [0]
            text = ""
            for paragram in result_list:
                for unit in paragram["json_1best"]["st"]["rt"][0]["ws"]:
                    text += unit["cw"][0]["w"]
        except Exception as e:
            text = ""

        return text

if __name__ == '__main__':
    # 输入讯飞开放平台的appid，secret、key和文件路径

    # file_path = r"..\lfasr_demo.wav"
    # file_path = r".\audio\audio_sample_little.wav"
    appid = "064abef1"
    apikey = "3c6a9a112b3f566dedbae970d89eef2d"
    apisecret = "ZjMxZDA3ZDBkZmM2ZDY4YzNhZGZhZjQw"
    # file_path = r"./record.wav"

    t = time.time()
    fat = FastAudioToText(appid, apikey, apisecret)
    # gClass.get_fileurl(file_path=r".\lfasr_demo.wav")
    print(fat.get_result())
    print("dt:", time.time() - t)
