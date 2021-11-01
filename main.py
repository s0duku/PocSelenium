"""
Simple Python Framework for fast testing pocs, based on Selenium Chrome driver, 
and gather targets from Fofa search engine. 
"""


from PocSelenium.Engine.SeleniumEngine import SeleniumEngine,TYPE_CHROME_DRIVER
from PocSelenium.Target.FofaTarget import FofaTarget
from PocSelenium.Manager.PocManager import PocManager
from hikcve import check_cve

engine = SeleniumEngine(TYPE_CHROME_DRIVER)

engine.option_disable_images_and_js()

engine.add_option_argument("user-data-dir=C:\\Users\\s0duku\\log")

engine.init_driver()

query = 'app="HIKVISION-视频监控"'

target = FofaTarget(engine,query)

manager = PocManager(target)

@manager.add_poc()
def my_poc(url):
    return check_cve(url)


manager.test()


