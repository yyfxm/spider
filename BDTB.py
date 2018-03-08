__author__ = "yyf"

import re
import urllib.error
import urllib.request

class BDTB(object):
    def __init__(self):
        self.base_url = "https://tieba.baidu.com/p/"
        self.default_title = "百度贴吧"
        self.page_index = 1
        self.content_num = 1
        self.file = None
        self.default_title = None

    def get_page_html(self,num,seeLZ=1,pn=1):
        try:
                url = self.base_url + str(num) + "?see_lz=" + str(seeLZ) + "&pn=" + str(pn)
                request = urllib.request.Request(url)
                response = urllib.request.urlopen(request)
                return response.read().decode()
        except urllib.error.URLError as e:
            if hasattr(e ,"reason"):
                print("出错啦",e.reason)
            return None
    def get_title(self,page_html):
        title_pattern = re.compile('''<h3.*?>(.*?)</h3>''',re.S)
        result = re.search(title_pattern,page_html)
        if result:
            return result.group(1)
        return None
    def get_page_num(self,page_html):
        page_num_pattern = re.compile('''回复贴，共.*?>(.*?)<''',re.S)
        result = re.search(page_num_pattern,page_html)
        if result:
            return int(result.group(1))

        return None
    def get_str_contents(self,page_html):
        str_contents_pattern = re.compile('''d_post_content j_d_post_content ">(.*?)</div>''',re.S)
        result = re.finditer(str_contents_pattern,page_html)
        if result:
            str_contents = self.replace(result)
            return str_contents

        return None
    def replace(self, result):
        str_contents = []
        for content in result:
            item = re.sub('''<img.*?>|<br>''',"\n", content.group(1))
            item = re.sub('''<a href.*?>|</a>| {4,7}''', '', item)
            str_contents.append(item.strip())
        return str_contents

    def open_file(self,title):
        if title:
            self.file = open(title + '.txt','w+', encoding='utf-8')
        else:
            self.file = open(self.default_title + 'w+', encoding='utf-8')
    def write_file(self,str_contents):
        for content in str_contents:
            self.file.write("-----------第" + str(self.page_index) + "楼---------\n" )
            self.file.write(content + '\n')
            self.page_index += 1

    def start(self, num, see_lz=1):
        page_html = self.get_page_html(num, see_lz, self.page_index)
        title = self.get_title(page_html)
        page_num = self.get_page_num(page_html)
        self.open_file(title)
        for i in range(page_num):
            str_contents = self.get_str_contents(page_html)
            self.write_file(str_contents)
            self.page_index += 1
            page_html = self.get_page_html(num, see_lz, self.page_index)
if __name__ == "__main__":
    spider = BDTB()
    spider.start(3138733512, 1)



