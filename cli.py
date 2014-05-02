#!/usr/bin/env python3

import click
import json
import requests


_ENDPOINT='http://dbios.herokuapp.com/'

class Thing(object):
    def __init__(self, **jawns):
        self.__dict__.update(jawns)

    def get_thing(self):
        r = requests.get(_ENDPOINT+'programs')
        things = r.json()
        for thing in things:
            yield self.__class__(**thing)

