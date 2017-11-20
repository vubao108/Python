class Tool:
    def convert_index(self, index):
        if index < 10:
            return "000%d"  %index
        elif index < 99:
            return "00%d" % index
        elif index < 999:
            return "0%d"  %index
        else:
            return "%d"  %index

    def get_book_name(self, book_url):
        #book_url : https://www.safaribooksonline.com/library/view/automate-the-boring/9781457189906/ch11.html
        str_list =  book_url.split('/')
        return str_list[5] + "_" + str_list[6]

    def get_page_name(self, page_url):
        #page_url : https://www.safaribooksonline.com/library/view/automate-the-boring/9781457189906/ch11.html
        tmp = page_url.split('/')[-1].split('.')[0]
        if len(tmp) > 20:
            return ""
        else:
            return tmp

    def get_file_extension(self, page_url):
        return "html"
        #page_url.split('.')[-1]

    def get_file_path(self, dir_path, url, index, title_page):
        index = self.convert_index(index)
        book_dir_basename = self.get_book_name(url)
        page_file_name = self.get_page_name(url)
        extension_file = self.get_file_extension(url)
        return "%s\\%s\\%s_%s_%s.%s"%(dir_path,book_dir_basename,index,page_file_name,title_page,extension_file)


