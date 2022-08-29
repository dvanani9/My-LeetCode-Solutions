class Logger(object):

    def __init__(self):
        self.Logger = {}
        
    def shouldPrintMessage(self, timestamp, message):
        """
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        
        if message not in self.Logger:
            self.Logger[message] = timestamp
            return True
        else:
            if timestamp - self.Logger[message] >= 10:
                self.Logger[message] = timestamp
                return True  
        return False
    
    