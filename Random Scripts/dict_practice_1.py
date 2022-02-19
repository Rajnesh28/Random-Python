car = {'Make': 'Toyota',
       'Model': 'Tacoma',
       'Year': 2012,
       'Transmission': 'Manual'}

def dict_practice(key):
    print(car.get('key','Not Found'))

dict_practice('Make')
