from api import LeClient


class Program(object):
    def __init__(self, id=None, title=None, image_url=None):
        self.id = id
        self.title = title
        self.image_url = image_url


class AProgram(Program):
    def __init__(self, id=None, title=None, image_url=None, workout_ids=None):
        Program.__init__(self, id, title, image_url)
        self.workout_ids = workout_ids

    def get(self, **kwargs):
        programs = LeClient().request(path='programs')
        try:
            program = next(filter(lambda x: x['id'] == kwargs['program_id'],
                                  programs))
            return self.__class__(**program)
        except KeyError:
            program = next(filter(lambda x: x['title'] == kwargs['title'],
                                  programs))
            return self.__class__(**program)
        except:
            pass

    def get_workouts(self, program_id):
        payload = {'program_id': program_id}
        workouts = LeClient().request(path='workouts', params=payload)
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

    def get_workouts(self, trainer_name):
        data = LeClient().request(path='workouts')
        try:
            workouts = filter(lambda x: x['trainer_name'] == trainer_name,
                             data)
            return workouts
        except:
            return False


class AWorkout(Workout):
    def __init__(self, id=None, title=None, trainer_name=None,
                 workout_description=None, program_ids=None, image_url=None):
        Workout.__init__(self, id, title, trainer_name, workout_description,
                         program_ids, image_url)


class Trainer(object):
    def __init__(self, id=None, name=None, workout_ids=None, program_ids=None):
        self.id = id
        self.name = name
        self.workout_ids = workout_ids
        self.program_ids = program_ids
