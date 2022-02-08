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
    """Class used to everything related to single routines"""
    pass

class TrainingPlan:
    """Class used to everything related to training plans which consist
    of single routines selected for a specific player 
    """
    def __str__(self):
        return f'Training plan {self.name} - details: {self.description}'

    def __repr__(self):
        return 'Training plan {self.name} - details: {self.description}'

    def __init__(self, name, description='', lvl=''):
        self.id = uuid4()
        self.name = name
        self.description = description
        self.lvl = lvl
        self.routines = []

    def add_routine_to_plan(self, *args):
        for i in args:
            self.routines.append(i)


class Skill:
    """Class used to manage detailed skills of players and areas to improve"""
    def __str__(self):
        return f'Skill {self.skill} - details: {self.details}'

    def __repr__(self):
        return 'Skill {self.skill} - details: {self.details}'

    def __init__(self, skill, comment=''):
        self.id = uuid4()
        self.skill = skill
        self.details = comment


class Admin:
    """Class related to role of admin"""

    def __str__(self):
        return f'Admin {self.first_name} {self.last_name}'

    def __repr__(self):
        return 'Admin {self.first_name} {self.last_name}'
    
    def __init__(self, firstname, lastname):
        self.id = uuid4()
        self.first_name = firstname
        self.last_name = lastname