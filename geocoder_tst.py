import requests
url = 'https://maps.googleapis.com/maps/api/geocode/json'
params = {'sensor': 'false', 'address': 'Mountain View, CA'}
r = requests.get(url, params=params)
results = r.json()['results']
# location = results[0]['geometry']['location']
# location['lat'], location['lng']
print(results)


url = "https://maps.googleapis.com/maps/api/geocode/json?address=Alberta, Canada&key=AIzaSyAAQgbbvo5dnbghgFReOCFw65mHeTlcla4"
r = requests.get(url)
print(r.json())