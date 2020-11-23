import requests

filename = 'TestImages/impo1.jpeg'
url = 'http://127.0.0.1:5000/pick_color'

image_file_descriptor = open(filename, 'rb')

files = {'image': image_file_descriptor}

r = requests.post(url, files=files)

print(r.text)

image_file_descriptor.close()