class User:

    def __init__(self, user=None):
        if user == None: 
            self.id = 0
            self.username = ''
            self.password = ''
            self.firstname = ''
            self.lastname = ''
            self.phone = ''
            self.email = ''
            self.isReviewer = False
            self.isAdmin = False
        else:
            self.id = user['id']
            self.username = user['username']
            self.password = user['password']
            self.firstname = user['firstname']
            self.lastname = user['lastname']
            self.phone = user['phone']
            self.email = user['email']
            self.isReviewer = user['isReviewer']
            self.isAdmin = user['isAdmin']

    def toString(self):
        name = f'{self.firstname} {self.lastname}'
        return f'{self.id:3} | {self.username:15} | {name:20} | {self.isReviewer:2} | {self.isAdmin:2}'