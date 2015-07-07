#coding: utf-8

import random
import os
os.chdir("E:/scrapy/creditchina/creditchina")

class ProxyMiddleware(object):
    # overwrite process request
    def __init__(self):
        with open("proxy_ips.txt") as f:
            self.proxy_ips = []
            for line in f:
                self.proxy_ips.append(line.strip())
            self.proxy_ips_length = len(self.proxy_ips)


    def process_request(self, request, spider):
        if self.proxy_ips_length:
            randomidx = random.randint(0, self.proxy_ips_length - 1)
            proxy_ip_port = self.proxy_ips[randomidx]
        else:
            proxy_ip_port = "http://111.13.12.202"
        request.meta['proxy'] = proxy_ip_port

        # Use the following lines if your proxy requires authentication
        # proxy_user_pass = "USERNAME:PASSWORD"

        # setup basic authentication for the proxy
        # encoded_user_pass = base64.encodestring(proxy_user_pass)
        # request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass