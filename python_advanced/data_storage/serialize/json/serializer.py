import json


class User(object):
    def __init__(self, name, email):
        self.username = name
        self.email = email

    def to_json(self):
        return {'username': self.username, 'email': self.email}

    @classmethod
    def from_json(cls, js_object):
        return cls(js_object['username'], js_object['email'])

    def __repr__(self):
        return 'User({!r}, {!r})'.format(self.username, self.email)


users = [User('john', 'john@gmail.com'), User('anna', 'anna@gmail.com')]


with open('serialize.json', 'w') as f:
    json.dump(users, f, indent=2, default=User.to_json)
