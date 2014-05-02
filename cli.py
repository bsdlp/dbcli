#!/usr/bin/env python3

from prettytable import PrettyTable
import requests


_ENDPOINT = 'http://dbios.herokuapp.com/'

def _get_thing(thing_type):
    r = requests.get(_ENDPOINT+thing_type)
    return r.json()

def list_programs():
    table = PrettyTable(['id', 'title', 'image_url'])
    for program in _get_thing('programs'):
        table.add_row([program['id'], program['title'], program['image_url']])
    table.align = 'l'
    return print(table)
