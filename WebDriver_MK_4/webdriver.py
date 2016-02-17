from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pyscreenshot
import html_report
import os
from PIL import Image


class WebDriverHandler(object):

    def __init__(self, chromedriver_path, url, xpaths, path):
        self.url = url
        self.xpaths = xpaths
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chromedriver_path, chrome_options=options)
        self.path_head, path_tail = os.path.split(path)
        self.path_head, tail = os.path.split(self.path_head)
        self.path_head = self.path_head + "\\"
        self.html_rep = html_report.HtmlReport(self.path_head)
        self.img_list = []

    def execute_invokes(self):
        exec_element = ""
        self.driver.get(self.url)
        size = 256, 256
        try:
            for index, xpath in enumerate(self.xpaths):
                try:
                    WebDriverWait(self.driver, int(10)).until(
                            EC.presence_of_element_located((By.XPATH, xpath)))
                    input_elements = self.driver.find_element_by_xpath(xpath).click()
                    exec_element = self.driver.title
                    img_path = self.prepare_screenshot(index)
                except:
                    exec_element = ''.join(str(index) + " of [xpaths] from ini file was failed")
                    img_path = ""
                self.html_rep.create_html_step(exec_element, img_path)
        finally:
            self.driver.quit()
            #self.delete_imgs()

    def prepare_screenshot(self, index):
        img = pyscreenshot.grab()
        img_name = "img"+str(index)+".jpeg"
        img_path = os.path.join(self.path_head, img_name)
        basewidth = 1024
        percent_rel = (basewidth/float(img.size[0]))
        proportional_height = int((float(img.size[1])*float(percent_rel)))
        img = img.resize((basewidth, proportional_height), Image.ANTIALIAS)
        img.save(img_path)
        self.img_list.append(img_path)
        return img_path

    def delete_imgs(self):
        for img in self.img_list:
            os.remove(img)
