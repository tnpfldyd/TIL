import requests

URL = 'https://api.themoviedb.org/3'
# movie = '/search/movie'
# params = { 'api_key' : '896988be1c1bb3801b7d75f69bd7b9a5', 'language' : 'ko-KR', 'query' : title}
# result = requests.get(URL+movie, params = params).json()
# a = result['results']
# movi = a[0]['id']

movie2 = '/movie/496243/credits'
params = { 'api_key' : '896988be1c1bb3801b7d75f69bd7b9a5', 'language' : 'ko-KR'}
result2 = requests.get(URL+movie2, params = params).json()
# cast = []
# for i in range(len(result2)):
#     cast.append(result2[i]['department'])
c = result2['crew']
d = []
for i in range(len(c)):
    if c[i]['department'] == 'Directing':
        d.append(c[i]['name'])
print(d)