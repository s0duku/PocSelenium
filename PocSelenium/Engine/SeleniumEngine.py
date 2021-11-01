from .PocEngine import PocEngine

from selenium import webdriver as wdr
import os

TYPE_CHROME_DRIVER = 0

class SeleniumEngine(PocEngine):
    
    def __init__(self,driver_type = TYPE_CHROME_DRIVER ):
        self.driver_type = driver_type
        self.window_size = (600,600)
        self.ready = False
        if driver_type == TYPE_CHROME_DRIVER:
            self.executable_path = os.path.join(os.path.dirname(__file__),r"..\driver\chromedriver.exe")
            self.cache_path = os.path.join(os.path.dirname(__file__),r"..\driver\chrome_cache")
            self.options = wdr.ChromeOptions()
        else:
            raise TypeError()


    def add_option_argument(self,arg):
        self.options.add_argument(arg)

    def option_disable_images_and_js(self):
        if self.driver_type ==  TYPE_CHROME_DRIVER:
            prefs = {
                    'profile.default_content_setting_values': {
                            'images': 2,
                            'javascript': 2
                        }
                    }

            self.options.add_experimental_option("prefs", prefs)
        else:
            raise TypeError()


    def option_cache_path(self,arg):
        if self.driver_type == TYPE_CHROME_DRIVER:
            self.cache_path = arg
        else:
            raise TypeError()

    def option_ignore_cert(self):
        if self.driver_type == TYPE_CHROME_DRIVER:
            self.options.add_argument("--ignore-certificate-errors")
        else:
            raise TypeError()


    def option_window_size(self,arg):
        self.window_size = arg

    def option_executable_path(self,arg):
        self.executable_path = arg


    def init_driver(self):
        if self.driver_type == TYPE_CHROME_DRIVER:
            #self.options.add_argument("user-data-dir="+self.cache_path)
            self.driver = wdr.Chrome(executable_path=self.executable_path,options=self.options)
        else:
            raise TypeError()
        self.driver.set_window_size(*self.window_size)
        self.ready = True


    def get(self,url):
        if not self.ready:
            raise TypeError()
        return self.driver.get(url)

    
    def find_elements_by_xpath(self,xpath):
        return self.driver.find_elements_by_xpath(xpath)


    def engine_type(self):
        return SeleniumEngine


    
    
    

        