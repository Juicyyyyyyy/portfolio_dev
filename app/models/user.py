from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id):
        self.id = id

    def get_id(self):
        return self.id 