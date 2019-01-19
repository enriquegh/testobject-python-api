import os

class Storage(object):

    def __init__(self, testobject):
        self.testobject = testobject

    def upload_app(self, path, display_name=None, is_active=True):
        method = 'POST'
        endpoint = '/storage/upload'

        headers = {}
        headers["App-Active"] = str(True)
        headers["Accept"] = "text/plain"

        if display_name:
            headers["App-DisplayName"] = display_name
        
        with open(path,'rb') as app:
            
            content = self.testobject.request(method, endpoint, headers=headers, data=app)

            return content
        
        raise Exception
