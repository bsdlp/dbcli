#!/usr/bin/env python3

from prettytable import PrettyTable
from api import LeClient
from re import search, IGNORECASE


api = LeClient()

_workout_jawns = ['title', 'trainer_name', 'workout_description',
                  'program_ids', 'image_url']
_program_jawns = ['id', 'title', 'image_url']


def _list_trainer(trainer_name, programs=None, workouts=None):
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

def _search(keyword, search_type=None):
    """
    :rtype:filter workouts based on case-insensitive search for <keyword> in
    workouts or programs depending on search_type input.
    """
    if search_type == None:
        search_type = ['programs', 'workouts']

    if 'programs' in search_type:
        _programs = api.request(path='programs')
        _search_programs = filter(
            lambda x: search(keyword, ''.join(map(str, x.values())), IGNORECASE), _programs)
        return _search_programs
    elif 'workouts' in search_type:
        _workouts = api.request(path='workouts')
        _search_workouts = filter(
            lambda x: search(keyword, ''.join(map(str, x.values())), IGNORECASE), _workouts)
        return _search_workouts

def tabulate(jawn_type):
    def wrapper(func):
        def _wrapper(*args, **kwargs):
            table = PrettyTable(jawn_type)
            for x in func(*args, **kwargs):
                table.add_row(x.values())
            table.align = 'l'
            print(table)
        return _wrapper
    return wrapper

@tabulate(_workout_jawns)
def list_workouts():
    """
    :rtype:generator all workouts.
    """
    for item in api.request(path='workouts'):
        yield item

@tabulate(_program_jawns)
def list_programs():
    """
    :rtype:generator all programs.
    """
    for item in api.request(path='programs'):
        yield item

@tabulate(_workout_jawns)
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

@tabulate(_workout_jawns)
def list_trainer_workouts(trainer_name):
    return _list_trainer(trainer_name, workouts=True)

@tabulate(_program_jawns)
def list_trainer_programs(trainer_name):
    return _list_trainer(trainer_name, programs=True)

@tabulate(_workout_jawns)
def search_workouts(keyword):
    return _search(keyword, search_type='workouts')

@tabulate(_program_jawns)
def search_programs(keyword):
    return _search(keyword, search_type='programs')
