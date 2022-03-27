import requests

from pprint import pprint



canvas_url = 'https://canvas.instructure.com'

api = input("Please input API key")


header = {'Authorization': 'Bearer ' + api}

def get_courses():
    response = requests.get(canvas_url + '/api/v1/courses',
         headers=header)

    pprint([course.get('name') for course in response.json()])


get_courses()
