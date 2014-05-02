class Program(object):
    def __init__(self, id=None, title=None, image_url=None):
        self.id = id
        self.title = title
        self.image_url = image_url

    def get(self, **kwargs):
        programs = _get_thing('programs')
        try:
            program = next(filter(lambda x: x['id'] == kwargs['program_id'], programs))
            return self.__class__(**program)
        except KeyError:
            program = next(filter(lambda x: x['title'] == kwargs['title'], programs))
            return self.__class__(**program)
        except:
            pass

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
