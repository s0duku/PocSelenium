
from PocSelenium.Manager.TestManager import TestManager

from .TestManager import TestManager
from ..Target.TestTarget import TestTarget

class PocManager(TestManager):
    def __init__(self,target:TestTarget):
        self.target = target
        self.poc_callbacks = []
        self.poc_true = []
        self.user_stop_test = False

    def test(self):
        targets = self.target.targets()
        for target in targets:
            for callback in self.poc_callbacks:
                if callback(target) == True:
                    self.poc_true.append(target)
                    print(target)
    
    def add_poc(self):
        def addPoc(func):
            self.poc_callbacks.append(func)
        return addPoc

                    
        
        
    
