from collections import deque

graph = {
    "you": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": []
}


def person_is_seller(name):
    """ If name person end letter m -> this is mango seller"""
    return name[-1] == 'm'


def search(name):
    search_queue = deque()  # Create queue
    search_queue += graph[name]  # Add name in queue
    searched = []  # Storage complete check name
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


search("you")
