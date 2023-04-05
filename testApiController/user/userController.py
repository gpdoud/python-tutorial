# UserController

from testApiController.user.user import User
from http_client import HttpClient

class UserController:

    def __init__(self):
        self.httpclient = HttpClient('http://doudsystems.net/prsc37db/api/users')

    def list(self):
        self.resp = self.httpclient.get()
        self.json = self.resp.data
        self.users = []
        for u in self.json:
            self.users.append(User(u))
        self.resp.data = self.users
        return self.resp
    
    def get(self, id=None):
        if id == None:
            raise SyntaxError('function get required a primary key')
        self.resp = self.httpclient.get(f'/{id}')
        self.resp.data = User(self.resp.data)
        return self.resp
    
    def create(self, user):
        self.resp = self.httpclient.post('', user)
        self.resp.data = User(self.resp.data)
        return self.resp

    def change(self, id, user):
        self.resp = self.httpclient.put(f'/{id}', user)
        return self.resp

    def delete(self, id):
        self.resp = self.httpclient.delete(f'/{id}')
        return self.resp
