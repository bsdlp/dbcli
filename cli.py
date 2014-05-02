#!/usr/bin/env python3

from prettytable import PrettyTable
import requests


_ENDPOINT = 'http://dbios.herokuapp.com/'


class Program(object):
    def __init__(self, id=None, title=None, image_url=None):
        self.id = id
        self.title = title
        self.image_url = image_url

    def get(self, **kwargs):
        programs = _get_thing('programs')
        try:
            program = next(filter(lambda x: x['id'] == kwargs['program_id'], programs))
        except AttributeError:
            program = next(filter(lambda x: x['title'] == kwargs['title'], programs))
        except:
            pass
        else:
            return self.__class__(**program)

    def get_workouts(self):
        payload = {'program_id': self.id}
        r = requests.get(_ENDPOINT+'workouts', params=payload)
        workouts = r.json()
        for workout in workouts:
            yield Workout([workout[i] for i in Workout.keys()])


class Workout(object):
    def __init__(self, title=None, trainer_name=None,
                 workout_description=None, program_ids=None, image_url=None):
        self.title = title
        self.trainer_name = trainer_name
        self.workout_description = workout_description
        self.program_ids = program_ids
        self.image_url = image_url

    def get_workout(self, trainer_name):
        workouts = _get_thing('workouts')
        try:
            workout = filter(lambda x: x['trainer_name'] == trainer_name,
                             workouts)
            return workout
        except:
            return False


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
