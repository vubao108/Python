from bs4 import BeautifulSoup
import re
import requests
import codecs
import os
import  time
import logging
class BookPage_Xuly:


    def __init__(self, html_string, sesion):
        self.str_content = html_string
        self.parser = BeautifulSoup(html_string,"html.parser")
        self.season = sesion



    def download_file(self,season_request, link, save_path):
        while True:
            try:
                writer = open(save_path, "wb")
                response = season_request.get(link, stream = True)
                for block in response.iter_content(1024):
                    if not block:
                        writer.close()
                        break
                    writer.write(block)

                return
            except requests.exceptions.ConnectionError:
                logging.warn("request exception %s" %link)
                time.sleep(3)
                continue

    def get_next_page_link(self):
        link_list = self.parser.find_all("a", {"class": "next nav-link"})
        if(len(link_list) > 0):
            return self.convert_link(link_list[0]["href"])
        return None

    def get_title_page(self):
        title_list =  self.parser.find_all("h1")
        if len(title_list) > 1:
            p = re.compile('[\/*?"<>|:]')
            return re.sub(p,"",title_list[1].text)
        return ""

    def convert_link(self,link):
        link1 = re.sub("^//","https://",link)
        link2 = re.sub("^/","https://www.safaribooksonline.com/", link1)
        return link2

    def save_file(self, file_page_path):
        dir_src_path = re.sub("\.\w+$","",file_page_path)
        base_dir_name = dir_src_path.split("\\")[-1]

        if not os.path.exists(dir_src_path):
            os.makedirs(dir_src_path)



        css_list =  self.parser.find_all("link",{"rel":"stylesheet"})

        css_order = 0

        for css_item in css_list:
            css_order += 1
            link_css_tmp = css_item["href"]
            download_link_css = self.convert_link(link_css_tmp)
            save_file ="%s/%d.css" % (dir_src_path, css_order)
            relatve_path = "%s/%d.css" %(base_dir_name, css_order)
            css_href = "./%s" % save_file
            self.str_content = re.sub(re.escape(link_css_tmp), relatve_path, self.str_content)
            self.download_file(self.season, download_link_css, save_file)

        for image_item in self.parser.find_all("img"):
            image_link_tmp = image_item["src"]
            image_name = image_link_tmp.split("/")[-1]

            download_image_link = self.convert_link(image_link_tmp)
            image_save_path = "%s\\%s"%(dir_src_path,image_name)

            image_src = "./%s/%s" %(base_dir_name, image_name)
            self.str_content = re.sub(re.escape(image_link_tmp), image_src, self.str_content )
            self.download_file(self.season, download_image_link, image_save_path)



        with codecs.open(file_page_path,"w", encoding='utf-8') as f:
            f.write(self.str_content)


if __name__ == '__main__':
    time_start = time.time()
    file_path = r"D:\OtherProject\SeleniumGetData\SaveFile\src\chapter12.html"
    my_sesion = requests.Session()
    html_content = codecs.open("safari01.html","r",encoding="utf-8").read()

    xuly = BookPage_Xuly(html_content, my_sesion)
    print  xuly.get_next_page_link()
    #xuly.save_file(file_path)

    print "done %d"%(time.time() - time_start)