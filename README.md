# DailyBurn CLI Code Test

For this code test we'd like you to build a fully featured command line tool in the language of your choice.

What you'll provide to us is both a runnable version of this tool and the source code used to write it along with some documentation of how it is structured and how it works.

Your CLI program should provide a full command line user interface including usage and help information for all the supported tasks.

# Overview:

The purpose of your CLI program is to talk to a simple JSON http API and to pull down information from it then to format that output for presentation.

The data will be available from: http://dbios.herokuapp.com/

The data we are looking at is made up of programs and workouts each with a set of attributes documented on the site listed above.

Program data is of the form:

    {
      "title": "DB15",
      "id": 10,
      "image_url": "path_to_image"
    }


Workout data is of the form: 

    {
        "image_url": "path_to_image",
        "workout_description": "Anja Garcia takes no prisoners with this mini-Metcon workout as she launches an all-out-assault on your body.",
        "title": "DB15 Inferno",
        "program_ids": [
            10
        ],
        "trainer_name": "Anja"
    }

## Specific function:

*You should spend a maximum of 3 hours on this test. The desired features are:*

Your program should provide a simplified command line version of our Library and Discover interaction - our Library page is a UI that lets people filter for a specific workouts based on a few parameters like trainer, difficulty, etc.

The data you are dealing with is simplified for the supported actions for your program will be:

1. List all programs
2. List all workouts
3. List all workouts for a specified program (specified by either program id or program name)
4. List all programs for a given trainer
5. List all workouts for a given trainer
6. Search for programs based on keyword (search based on the title or description data)
7. Search for workouts based on keyword (search based on the title or description data)
8. Search across all data based on keyword (search based on the title or description data of both programs and workouts) - result data should be formatted so it's clear which are workouts and which are programs

## Loading data

The data you will be working with is provided via an HTTP API that returns JSON data so you'll need to pull that data down via HTTP in order to provide results and to part the JSON using some mechanism supported by your language of choice

## Guidelines:

* You may use whatever programming language you wish
* It's OK if you do not have time to build all features, but be prepared to walk us through your thoughts and strategy.
* Some aspects are left intentionally vague to allow you creative freedom - take this task and run with it, it should demonstrate who you are as a programmer.
* You own whatever code you write, and are free to do whatever you want with it.
* You can deliver your final app to us however you want, but it should be easy for us to get it running and play with the end-result.

