import os 
class environ(object):
    environ = os.environ
    def __getattr__(self,variable):
        return self.get(variable)
    def __setattr__(self,variable,value):
        self.environ[variable]=value
    def __delattr__(self,variable):
        del self.environ[variable]
    def update(self,variable,value):
        self.environ[variable]=value
    def get(self,variable):
        if variable in self.environ:
            return self.environ[variable]
        else: raise KeyError
    def remove(self,variable):
        del self.environ[variable]

    
