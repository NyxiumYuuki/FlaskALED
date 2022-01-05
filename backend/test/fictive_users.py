import sys
sys.path.append( "../application" )
import users_model
import logs_model 

from users_model import Users


    


TAB_USER = [
    {
         "email": "riri@gmail.com",
         "hash_pass": "ririPass",
         "salt": "b'\x98\x95]\xa2B\xe5\x84gN\n1\x11\x1c%\xf7S\x8b\x88\xf7\xaa\x83\xf8$\xa8\xd5A\xd1\xa0\xf7:j\x10'",
         "is_admin": False       
    },
    {
        "id": 2,
        "email": "fifi@gmail.com",
        "hash_pass": "fifiPass",
        "salt": "b'\xa9X9{\xc3\x8c\xe0\xeb\x0b\x01\xd0.o\t\xc0bv\xac\xe2n\x878\xf7\xba\x16\xd6\xee\x94\xc8U\xf0\x15'",
        "is_admin": False  
    },
    {
        "id": 3,
        "email": "donald@gmail.com",
        "hash_pass": "donaldPass",
        "salt": "b'\xefM\xe5q\r\xb2\xc5\xff3\x88\x0c\x87\xa3\xe9F\xd7:\xc1\xc2J\xabvVR&\xe1-|D\xf5L '"
        "is_admin": False
    }, 
    {
        "id": 4,
        "email": "daisy@gmail.com",
        "hash_pass": "daisyPass",
        "salt": "b'\x01\xefCC\x05\x1f\x85\xd8\xf0\x02\xd1\x1c\xcb\xab\xec\x87M\x03\xe5T\x05]\x11\xc45<}\xd3\xfbFA\xbb'"
        "is_admin": True
    }, 
]


def get_user_object(i: int):
    return Users(
        id=TAB_USER[i]["id"],
        email=TAB_USER[i]["email"],
        login=TAB_USER[i]["login"],
        hashPass=TAB_USER[i]["hashPass"],
        isAdmin=TAB_USER[i]["isAdmin"]  
    )


def get_user_json(i: int):
    return TAB_USER[i]





