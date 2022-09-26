import pyrebase

# Configuration
config = {
  "apiKey": "AIzaSyADa4fhetZo3ppVEaFj1-1IuyTEtIqqyZc",
  "authDomain": "",
  "databaseURL": "",
  "projectId": "task-management-9bc8a",
  "storageBucket": "",
  "messagingSenderId": "625821177645",
  "appId": "1:625821177645:web:ecf64eb22a9ea7a619e5a4"
}

# Initialize firebase
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

request_user = {
  "is_logged_in": False,
  "name": "",
  "email": "",
  "uid": ""
}
