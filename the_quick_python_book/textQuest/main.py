from textQuest.game_obj import Goblin, GameObject


def get_input():
    command = input(": ").split()
    verb_word = command[0]
    if verb_word in verb_dict:
        verb = verb_dict[verb_word]
    else:
        print(f"Unknown verb {verb_word}")
        return

    if len(command) >= 2:
        noun_word = command[1]
        print(verb(noun_word))
    else:
        print(verb())


def say(noun):
    return f"You say {noun}"


def examine(noun):
    if noun in GameObject.objects:
        return GameObject.objects[noun].get_desc()
    else:
        return f"There is no {noun} here"


def hit(noun):
    if noun in GameObject.objects:
        thing = GameObject.objects[noun]
        if type(thing) == Goblin:
            thing.health -= 1
            if thing.health <= 0:
                msg = f'You kill {noun} {thing.name}'
            else:
                msg = f'You hit {noun} {thing.name}'
        else:
            raise ValueError("Not correct target")
    else:
        msg = f'There no {noun}'
    return msg


verb_dict = {
    "say": say,
    "examine": examine,
    "hit": hit,
}

goblin = Goblin("Gobbly")
print(goblin.__dict__)
while True:
    get_input()
