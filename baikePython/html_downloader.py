import urllib
from urllib import request


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        resp = request.urlopen(url)
        if resp.status != 200:
            return None
        return resp.read()

