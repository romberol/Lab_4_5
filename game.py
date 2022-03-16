class Room():
    def __init__(self, name):
        self.name = name
        self.description = None
        self.linked_rooms = {"south": None,
                             "north": None, "west": None, "east": None}
        self.character = None
        self.item = None

    def set_description(self, description):
        self.description = description

    def link_room(self, room, direction):
        opposite_directions = {"south": "north",
                               "north": "south", "west": "east", "east": "west"}
        self.linked_rooms[direction] = room
        room.linked_rooms[opposite_directions[direction]] = self

    def get_details(self):
        print(self.name)
        print("-"*20)
        print(self.description)
        for room_direction in self.linked_rooms:
            if self.linked_rooms[room_direction]:
                print(
                    f"The {self.linked_rooms[room_direction].name} is {room_direction}")

    def set_character(self, character):
        self.character = character

    def get_character(self):
        return self.character

    def move(self, direction):
        return self.linked_rooms[direction]

    def set_item(self, item):
        self.item = item
    def get_item(self):
        return self.item


class Enemy():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.conversation = None
        self.weakness = None

    def describe(self):
        print(self.name+" is here!")
        print(self.description)

    def set_conversation(self, conversation):
        self.conversation = conversation

    def set_weakness(self, weakness):
        self.weakness = weakness

    def talk(self):
        print(f"[{self.name} says]: "+self.conversation)

    def fight(self, fight_with):
        return fight_with == self.weakness

    def get_defeated(self):
        return None


class Item():
    def __init__(self, name):
        self.name = name
        self.description = None

    def set_description(self, description):
        self.description = description

    def describe(self):
        print(f"The [{self.name}] is here - "+self.description)

    def get_name(self):
        return self.name
