#!/usr/bin/env python3

from prettytable import PrettyTable
from api import LeClient


api = LeClient()

_workout_jawns = ['title', 'trainer_name', 'workout_description',
                  'program_ids', 'image_url']
_program_jawns = ['id', 'title', 'image_url']


def list_all(thing_type):
    if thing_type == 'programs':
        _jawns = _program_jawns
    elif thing_type == 'workouts':
        _jawns = _workout_jawns
    table = PrettyTable(_jawns)
    for item in api.request(path=thing_type):
        table.add_row([item[i] for i in _jawns])

    table.align = 'l'
    return print(table)
