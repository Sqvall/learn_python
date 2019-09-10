import json
from python_advanced.serialize.json.serializer import User


with open('serialize.json') as f:
    users = json.load(f, object_hook=User.from_json)

print(users)
print()
for u in users:
    print(u.username)
    print(u.email)
    print()
