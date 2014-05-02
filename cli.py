#!/usr/bin/env python3

from prettytable import PrettyTable
import requests


_ENDPOINT = 'http://dbios.herokuapp.com/'


class Program(object):
    def __init__(self, id, title, image_url):
        self.id = id
        self.title = title
        self.image_url = image_url

    def get_workouts(self):
        payload = {'program_id': self.id}
        r = requests.get(_ENDPOINT+'workouts', params=payload)
        workouts = r.json()
        for workout in workouts:
            yield Workout([workout[i] for i in Workout.keys()])


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
