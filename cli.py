#!/usr/bin/env python3

from prettytable import PrettyTable
import requests


_ENDPOINT = 'http://dbios.herokuapp.com/'


class Thing(object):
    def __init__(self, **jawns):
        self.__dict__.update(jawns)

    def get_thing(self, thing_type):
        r = requests.get(_ENDPOINT+thing_type)
        things = r.json()
        for thing in things:
            yield self.__class__(**thing)

    def tableify(self):
        table = PrettyTable(self.__dict__.keys())
        table.add_row(i.__dict__.values())


thingerator = Thing()


def list_thing(thing_type):
    _table = PrettyTable(i.__dict__.keys())
    for i in thingerator.get_thing(thing_type):
        _table.add_row(i.__dict__.values())
    print(_table)
