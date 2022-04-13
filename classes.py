from enum import Enum


class User:
    id_counter = 0

    def __init__(self, id, username, password):
        self.id = User.id_counter
        User.id_counter += 1
        self.username = username
        self.password = password


class State(Enum):

    not_started = -1
    in_progress = 0
    complete = 1


class Media(Enum):

    tv_show = 0
    book = 1
    music = 2


class Topic:

    def __init__(self, name, media, state=State.not_started):
        self.name = name
        self.media = media
        self.state = state
