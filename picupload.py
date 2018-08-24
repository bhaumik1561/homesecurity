
import sys
import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage


image_url = sys.argv[1]

cred = credentials.Certificate("C:/Users/bhaum/Downloads/homesecurity-65358-firebase-adminsdk-lh98m-ab8e57aa7d.json")
firebase_admin.initialize_app(cred, {'storageBucket': 'homesecurity-65358.appspot.com'})

bucket = storage.bucket('homesecurity-65358.appspot.com')

image_data = requests.get(image_url).content
blob = bucket.blob('new_cool_image1.jpg')
blob.upload_from_string(
        image_data,
        content_type='image/jpg'
    )
print(blob.public_url)


