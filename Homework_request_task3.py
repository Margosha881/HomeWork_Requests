import requests
from datetime import timedelta
from datetime import datetime


def search_tag(days, tag):
    url = 'https://api.stackexchange.com/2.3/questions'

    final_date = int(datetime.timestamp(datetime.now()))
    initial_date = final_date - days * 86400

    PARAMS = {
        'fromdate': initial_date,
        'todate': final_date,
        'tagged': tag,
        'site': 'stackoverflow'
    }

    response = requests.get(url, params=PARAMS)
    print("За два последних дня вопросы с тегом 'Python':")
    print()

    for question in response.json().get('items'):
        quest =[]
        quest.append(str(question['title']))
        print(quest)
        
search_tag(2, 'python')