#!/usr/bin/env python3

from prettytable import PrettyTable
from api import LeClient


api = LeClient()

_workout_jawns = ['title', 'trainer_name', 'workout_description',
                  'program_ids', 'image_url']
_program_jawns = ['id', 'title', 'image_url']


def list_all(thing_type):
    """
    :rtype:generator all workouts or programs.
    """
    if thing_type == 'programs':
        _jawns = _program_jawns
    elif thing_type == 'workouts':
        _jawns = _workout_jawns
    for item in api.request(path=thing_type):
        yield item

def list_program_workouts(program_id=None, program_title=None):
    """
    :rtype:filter workouts in program.
    """
    _programs = api.request(path='programs')
    try:
        _program = next(filter(
            lambda x: x['id'] == program_id or x['title'] == program_title,
            _programs))
    except:
        return None

    _workouts = api.request(path='workouts')
    _prog_workouts = filter(
        lambda x: _program['id'] in x['program_ids'], _workouts)
    return _prog_workouts

def list_trainer(programs=None, workouts=None, trainer_name):
    """
    :rtype:filter either programs or workouts by specified trainer_name,
    depending on whether kwarg programs or workouts is True.
    """
    _workouts = api.request(path='workouts')
    _trainer_workouts = filter(
        lambda x: x['trainer_name'] == trainer_name, _workouts)

    if workouts:
        return _trainer_workouts

    _program_ids = { i for x in _trainer_workouts for i in x['program_ids']}
    _programs = api.request(path='programs')
    _trainer_programs = filter(
        lambda x: x['id'] in _program_ids, _programs)
    return _trainer_programs
