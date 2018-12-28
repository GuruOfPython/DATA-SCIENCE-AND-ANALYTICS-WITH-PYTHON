import requests

addr = "2945 Irvington Rd, Falls Church, VA, 22042-1607"
api_key = "AIzaSyAo6qNQJMhz2br7FbUbVcb7krKz-26VyZ0"
url = f"http://maps.googleapis.com/maps/api/streetview?fov=70&location={addr}&size=600x400&key={api_key}"

print(url)
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        }

r = requests.get(url=url, headers = headers, stream=True)

save_file_name = '1.png'
with open(save_file_name, "wb") as png:
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            png.write(chunk)
