import pyrebase
config = {
  "apiKey": "AIzaSyCZowZajsv49aNYRKbZJaHT7P4r_bHnSfU",
  "authDomain": "homesecurity-65358.firebaseapp.com",
  "databaseURL": "https://homesecurity-65358.firebaseio.com/",
  "storageBucket": "homesecurity-65358.appspot.com",
 "serviceAccount": "C:/Users/bhaum/Downloads/homesecurity-65358-firebase-adminsdk-lh98m-ab8e57aa7d.json"

}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
# as admin
#storage.child("images/C:/Users/bhaum/Pictures/Camera Roll/my.jpg")
storage.child("example.jpg").put("C:/Users/bhssaum/Pictures/Camera Roll/my.jpg")