from ast import arg
from uuid import uuid4


class Coach:
    """Class used to everything related to coaches"""

    def __init__(self, firstname, lastname, *args):
        self.id = uuid4()
        self.first_name = firstname
        self.last_name = lastname
        self.players = list(args) if args else list()

    def __str__(self):
        return f'Coach {self.first_name} {self.last_name}'

    def __repr__(self):
        return 'Coach {self.first_name} {self.last_name}'

    def show_stats(self):
        pass

    def send_feedback(self):
        pass

    def approve_finished_plan(self):
        pass

    def create_training_plan(self):
        pass

    

class Player:
    """Class used to everything related to players"""

    def __init__(self, firstname, lastname, coach=None):
        self.id = uuid4()
        self.first_name = firstname
        self.last_name = lastname
        self.coach = coach

    def __str__(self):
        return f'Player {self.first_name} {self.last_name}, coach {self.coach}'

    def __repr__(self):
        return 'Player {self.first_name} {self.last_name}, coach {self.coach}'

    def send_scores(self):
        pass

    def show_stats(self):
        pass

    def send_feedback(self):
        pass

class Routine:
    pass

class TrainingPlan:
    pass

class Skill:
    pass

class Admin:
    pass