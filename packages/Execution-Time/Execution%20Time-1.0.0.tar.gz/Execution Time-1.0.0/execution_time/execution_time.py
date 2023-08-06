import functools
import time
import os
import logging
from inspect import getmembers,isfunction,ismethod
import sys


class ExecutionTime:

    logFormatter = logging.Formatter("%(asctime)s [%(levelname)-5.5s]  %(message)s")
    rootLogger = logging.getLogger()
    rootLogger.setLevel(logging.DEBUG)

    def __init__(self,filelog=False,console=False,module_name=None):
         
        self.issue_url = "https://github.com/siddhant-curious/Python-Method-Execution-Time/issues"
        
        self.filelog = filelog        
        self.console = console
        self.module_name = module_name
        self.logtime_data = {}

        if self.filelog:
            self.enable_filelogs()

        if self.console:
            self.enable_console()

        if self.module_name is not None:
            self.auto_decorate()
    
    def timeit(self,method):
        @functools.wraps(method)
        def wrapper(*args,**kwargs):
            start_time = time.perf_counter()
            result = method(*args,**kwargs)
            end_time = time.perf_counter()
            total_time = (end_time-start_time)*1000
            self.logtime_data[method.__name__]=total_time
            if self.console is True:
                ExecutionTime.rootLogger.info(f'Time take by method : {method.__name__} is {total_time} ms')
            return result
        return wrapper
    
    def enable_console(self):
        consoleHandler = logging.StreamHandler(sys.stdout)
        consoleHandler.setFormatter(ExecutionTime.logFormatter)
        ExecutionTime.rootLogger.addHandler(consoleHandler)
    
    def auto_decorate(self):
        try:
            module = sys.modules[self.module_name]
            items = getmembers(module,isfunction)
            for name,addr in items:
                setattr(module,name,self.timeit(addr))
        except KeyError as e:
            raise f'Error Occured, No module by name {module_name}. If you think this was a mistake than raise issue at {self.issue_url}'
