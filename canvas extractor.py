import requests

from pprint import pprint



canvas_url = 'https://canvas.instructure.com'

# api = input("Please input API key")
api = "10284~19SXSR0jhcLeQQ4Mvjmmgm8P2mKkXkNOSVcgMOQ5e4mv36GJcH8OtxkT0HzwdKis"

header = {'Authorization': 'Bearer ' + api}

def get_courses():
    response = requests.get(canvas_url + '/api/v1/courses',
         headers=header)

    pprint([course.get('name') for course in response.json()])


get_courses()
