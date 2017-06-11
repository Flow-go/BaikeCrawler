# coding:utf-8
import urllib.request
import requests
class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        response = requests.get(url)

        if response.status_code != 200:
            return None
        response.encoding = 'utf-8' # 此处出过错
        return response.text
