import requests
import random

url = "http://127.0.0.1:8000/users/"

data = {
"owner_id": 2,
"description": "a wild pokemon",
"title": "squirtle",
}

# response = requests.post(url, json=data)
 
# print("Status Code", response.status_code)
# print("JSON Response ", response.json())


for n in range(100):
    data = {
        "email" :  f"{random.randint(0,20000)}@{random.choice(['sample','email','google'])}",
        "password": f"{random.randint(100000,200000)}"
    }
    requests.post(url, json=data)

    # id = Column(Integer, primary_key=True, index=True)
    # email = Column(String, unique=True, index=True)
    # hashed_password = Column(String)
    # is_active = Column(Boolean, default=True)