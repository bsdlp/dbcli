#!/usr/bin/env python3

from prettytable import PrettyTable
import requests


_ENDPOINT = 'http://dbios.herokuapp.com/'

def _get_thing(thing_type):
    r = requests.get(_ENDPOINT+thing_type)
    return r.json()

def list_things(thing_type):
    if thing_type == 'programs':
        _jawns = ['id', 'title', 'image_url']
    elif thing_type == 'workouts':
        _jawns = ['title', 'trainer_name', 'workout_description',
                  'program_ids', 'image_url']

    table = PrettyTable(_jawns)
    for program in _get_thing(thing_type):
        table.add_row([program[i] for i in _jawns])

    table.align = 'l'
    return print(table)
