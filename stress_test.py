from locust import Locust, TaskSet, task
import sys
import os
import base64
import hmac
import hashlib
import time
import httplib
import mimetools
import requests

class MyTaskSet(TaskSet):
        def post_multipart(self, host, selector, fields, files):
            content_type, body = self.encode_multipart_formdata(fields, files)
            h = httplib.HTTP(host)
            h.putrequest('POST', selector)
            h.putheader('content-type', content_type)
            h.putheader('content-length', str(len(body)))
            h.endheaders()
            h.send(body)
            errcode, errmsg, headers = h.getreply()
            return h.file.read()

        def encode_multipart_formdata(self, fields, files):
            boundary = mimetools.choose_boundary()
            CRLF = '\r\n'
            L = []
            for (key, value) in fields.items():
                L.append('--' + boundary)
                L.append('Content-Disposition: form-data; name="%s"' % key)
                L.append('')
                L.append(str(value))
            for (key, value) in files.items():
                L.append('--' + boundary)
                L.append('Content-Disposition: form-data; name="%s"; filename="%s"' % (key, key))
                L.append('Content-Type: application/octet-stream')
                L.append('')
                L.append(value)
            L.append('--' + boundary + '--')
            L.append('')
            body = CRLF.join(L)
            content_type = 'multipart/form-data; boundary=%s' % boundary
            return content_type, body

        @task
        def init(self):
            host = "identify-ap-southeast-1.acrcloud.com"
            access_key = "*******************************"
            access_secret = "*************************************"

            f = open("/Users/linuxautobot/Downloads/SampleAudio_0.4mb.mp3", "rb")
            sample_bytes = os.path.getsize("/Users/linuxautobot/Downloads/SampleAudio_0.4mb.mp3")
            content = f.read()
            f.close()

            http_method = "POST"
            http_uri = "/v1/identify"
            data_type = "audio"
            signature_version = "1"
            timestamp = time.time()

            string_to_sign = http_method + "\n" + http_uri + "\n" + access_key + "\n" + data_type + "\n" + signature_version + "\n" + str(
                timestamp)
            sign = base64.b64encode(hmac.new(access_secret, string_to_sign, digestmod=hashlib.sha1).digest())

            fields = {'access_key': access_key,
                      'sample_bytes': sample_bytes,
                      'timestamp': str(timestamp),
                      'signature': sign,
                      'data_type': data_type,
                      "signature_version": signature_version}

            res = self.post_multipart(host, "/v1/identify", fields, {"sample": content})
            print res
	    r = requests.post('https://uol56erc77.execute-api.ap-south-1.amazonaws.com/dev/api/acrdata','res')

class MyLocust(Locust):
    task_set = MyTaskSet
    min_wait = 5000
    max_wait = 15000
