import requests
import pandas as pd
def get_child_screen_time_results():
    # results=requests.get("API url here for screen activity:")
    # if results.status_code==200:
    #     data=results.json()
    #     return data
    data={
        'child_activity':[
            "8:00 am - 11:00 pm : Study Time on Laptop",
            "12:00 pm - 1:00 pm : Chhota Bheem Cartoon",
            "3:30 pm - 4:00 pm : Playing game on Mobile Phone",
            "8:00 pm - 10:00 pm : Movie Time",
            "11:00 pm - 11:30 pm : Playing games on PS5"

        ],
        'screen_time':'4 hours'
    }
    return data

def get_data_to_calculate_right_screen_time():
    # results=requests.get("API url here for child's basic information")
    # if results.status_code == 200:
        # data=results.json()
        # return data

    data={
        'Age':10,
        'StudyHabits':'average',
        'EmotionalHealth':'good',
        'CurrentScreenUsage':4,
        'TimeForSocialActivities':1.5,
        'TimeWithFamily':2.5,
        'SleepDuration':8,
        'HistoryOfEyeProblems':'Yes',
        'HeadacheHistory':'No'

    }
    return data
