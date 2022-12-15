"""
Custom Thread is a class to extend thread function, created by 
https://www.geeksforgeeks.org/python-different-ways-to-kill-a-thread/
"""

from sys import settrace
from threading import Thread

class CustomThread(Thread):
    """Custom Thread to extend threads function"""    
    def __init__(self, *args, **keywords):
        """Same thread args"""        
        Thread.__init__(self, *args, **keywords)
        self.killed = False

    def start(self):
        """Start thread, use at the place run"""        
        self.__run_backup = self.run
        self.run = self.__run     
        Thread.start(self)

    def __run(self):
        """Private run method, used per start"""        
        settrace(self.globaltrace)
        self.__run_backup()
        self.run = self.__run_backup

    def globaltrace(self, frame, event, arg):
        """Globaltrace"""        
        if event == 'call':
            return self.localtrace
        else:
            return None

    def localtrace(self, frame, event, arg):
        """Localtrace"""
        if self.killed:
            if event == 'line':
                raise SystemExit()
        return self.localtrace

    def kill(self):
        """Kill the thread, allows the use of join without erros"""        
        self.killed = True