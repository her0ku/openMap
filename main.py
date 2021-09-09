import requests
import gmaps
import gmaps.datasets

response = requests.get('https://graphhopper.com/api/1/route?point=55.79683470754812, 37.724203498762215&point=55.798432887249085, 37.72355440412516&vehicle=foot&avoid=steps;bridge&points_encoded=false&instructions=true&algorithm=alternative_route'
                        '&elevation=true&ch.disable=truet&details=road_class&details=road_access&details=road_environment&key=API')

points = []
road_info = []
road_class = []
for data in response.json()['paths']:
    points.append(data['points']['coordinates'])


for data in response.json()['paths']:
    road_info.append(data['details']['road_environment'])
    road_class.append(data['details']['road_class'])

print('Координаты:')
print(points)
print('Структура:')
print(road_info)
print('Поверхность:')
print(road_class)

fix_points = []
for i in points:
    for j in i:
        fix_points.append(j[1::-1]) #Получаем координаты без всего лишнего

print('Каноничные точки:')
print(fix_points)

point_cast = fix_points[6]
point_cast2 = fix_points[7]

response = requests.get(f'https://graphhopper.com/api/1/route?point={point_cast[0]}, {point_cast[1]}&point={point_cast2[0]}, {point_cast[1]}&vehicle=foot&avoid=steps;bridge&points_encoded=false&instructions=true&algorithm=alternative_route'
                        '&elevation=true&ch.disable=truet&details=road_class&details=road_access&details=road_environment&key=API')

new_points = []
new_road = []
new_road_class = []
for data in response.json()['paths']:
    new_points.append(data['points']['coordinates'])

for data in response.json()['paths']:
    new_road.append(data['details']['road_environment'])
    new_road_class.append(data['details']['road_class'])

print('Координаты:')
print(new_points)
print('Структура:')
print(new_road)
print('Поверхность:')
print(new_road_class)

#Отрисовка координат
#fig = gmaps.figure()
#mak = gmaps.marker_layer(fix_points)
#fig.add_layer(mak)
#fig
