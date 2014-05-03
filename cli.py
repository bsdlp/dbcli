#!/usr/bin/env python3

from prettytable import PrettyTable
from api import LeClient
from models import Workout, Program, AWorkout, AProgram, Trainer


api = LeClient()


def list(thing_type):
    if thing_type == 'program':
        _jawns = Program().__dict__.keys()
        _path = 'programs'
        table = PrettyTable(_jawns)
    elif thing_type == 'workout':
        _jawns = Workout().__dict__.keys()
        _path = 'workouts'
        table = PrettyTable(_jawns)
    else:
        raise KeyError(thing_type + ' is not a thing.')

    for item in api.request(path=_path):
        table.add_row([item[i] for i in _jawns])

    table.align = 'l'
    return print(table)
