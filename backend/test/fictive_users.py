from users_model import Users

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    hash_pass = db.Column(db.LargeBinary(), nullable=False)
    salt = db.Column(db.LargeBinary(), nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    


TAB_USER = [
    {
         "id": 1,
         "email": "riri@gmail.com",
         "login": "riri",
         "hash_pass": "ririPass",
         "isAdmin": False       
    },
    {
        "id": 2,
        "email": "fifi@gmail.com",
        "login": "fifi",
        "hashPass": "fifiPass",
        "isAdmin": False  
    },
    {
        "id": 3,
        "email": "loulou@gmail.com",
        "login": "loulou",
        "hashPass": "loulouPass",
        "isAdmin": False
    }, 
    {
        "id": 4,
        "email": "picsou@gmail.com",
        "login": "picsou",
        "hashPass": "picsouPass",
        "isAdmin": True
    }, 
    {
        "id": 5,
        "email": "donald@gmail.com",
        "login": "donald",
        "hashPass": "donaldPass",
        "isAdmin": True
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





