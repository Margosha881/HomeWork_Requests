import requests
from pprint import pprint

base_url = 'https://akabab.github.io/superhero-api/api/'
list_heroes = ['Hulk', 'Captain America', 'Thanos']


class Heroes:
   
    def init_feature_heroes(self):
        uri = 'all'
        request_url = base_url + uri + '.json'
        response = requests.get(request_url).json()  
        my_hero = []      
        for dict in response:
            for hero in list_heroes:
                if hero == dict['name']:
                    my_hero.append({'name':dict['name'],'intelligence':int(dict['powerstats']['intelligence'])})
        largest_intelligence = 0
        for intelligens_hero in my_hero:
            if largest_intelligence < int(intelligens_hero['intelligence']):
                largest_intelligence = int(intelligens_hero['intelligence'])
                name = intelligens_hero['name']
        pprint(f'Самый умный супергерой {name}, интелект: {largest_intelligence}')

best_hero = Heroes()
best_hero.init_feature_heroes()


