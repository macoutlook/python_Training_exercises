from dominate import document
from dominate.tags import *
import os
import codecs


class HtmlReport(object):

    def __init__(self, file_path):
        self.file_path = file_path + "Report\\"
        self.file_name = "html_report.html"
        self.html_full_path = os.path.join(self.file_path, self.file_name)

    def create_html_step(self, line, img_for_rep = None):
        #building html string and save it as doc
        with document(title='Steps') as doc:
            meta(content="text/html; charset=UTF-8")
            with div():
                print line
                p(line)
                img("img", src='%s' % img_for_rep)
        # saving doc string to file with given path, codecs.open gives possibility to set encoding
        with codecs.open(self.html_full_path, 'a', encoding="utf-8") as f:
            f.write(doc.render())