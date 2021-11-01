from .TestTarget import TestTarget
from ..Engine.PocEngine import PocEngine
from ..Engine.SeleniumEngine import SeleniumEngine
import base64

FOFA_LIST_XPATH = "//div[@class='rightListsMain']/div/div/span/a[@target='_blank']"
FOFA_TARGET_XPATH = "/a[@target='_blank']"


class FofaTarget(TestTarget):
    def __init__(self,engine:PocEngine,query):
        if engine.is_ready() == False:
            raise TypeError()

        self.engine = engine
        self.fofa_query = query


    def build_query_url(self,query,page):
        return r'https://fofa.so/result?qbase64='+str(base64.b64encode(query.encode('utf')))[2:-1]+'&page='+str(page)


    def target_query(self,qy):
        self.fofa_query = qy


    def targets(self,max_num=None):
        cnt_num = 0
        sp = 1
        if self.engine.engine_type() == SeleniumEngine:
            while True:
                self.engine.get(self.build_query_url(self.fofa_query,sp))
                res_list = self.engine.find_elements_by_xpath(FOFA_LIST_XPATH)
                if not res_list:
                    return
                for elem in res_list:
                    if max_num != None:
                        if cnt_num > max_num:
                            return
                    url = elem.get_attribute("href")[:-1]
                    yield url
                    cnt_num += 1
                sp += 1
        else:
            raise TypeError()

        return
         