conf = { 
        'host' : 'YOUR_HOSTNAME',
        'user' :  'YOUR_USERNAME',
        'password' : 'YOUR_PASSWORD',
        }

class Config:
    def __init__(self):
        self._config = conf

    def get_property(self, property_name):
        if property_name not in self._config.keys():
            return None  
        return self._config[property_name]