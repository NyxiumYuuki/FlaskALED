import os
import sys
sys.path.append("../application")
from application.users_model import Users
from application.api_functions import hash_password



TAB_USER_WITH_PASSWORD = [
    {
         "id": 1,
         "email": "riri@gmail.com",
         "nickname": "Riri",
         "password": "ririPass",
         "is_admin": False       
    },
    {
        "id": 2,
        "email": "fifi@gmail.com",
        "nickname": "Fifi",
        "password": "fifiPass",
        "is_admin": False  
    },
    {
        "id": 3,
        "email": "donald@gmail.com",
        "nickname": "Donald",
        "password": "donaldPass",
        "is_admin": False
    }, 
    {
        "id": 4,
        "email": "daisy@gmail.com",
        "nickname": "Daisy",
        "password": "daisyPass",
        "is_admin": True
    }, 
]



# Convert user with passord (uwp) to user
def uwp_to_user(uwp):
    salt0 = os.urandom(32)
    hash_pass0 = hash_password(salt0, uwp["password"])
    return Users(
        email = uwp["email"],
        nickname = uwp["nickname"],
        hash_pass = hash_pass0,
        salt = salt0,
        is_admin = uwp["is_admin"]
    )



TAB_USER = []
for uwp in TAB_USER_WITH_PASSWORD:
    TAB_USER.append(uwp_to_user(uwp))