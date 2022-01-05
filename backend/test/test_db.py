print("debut")

import sys
#sys.path.append( "../application" )


import os
os.chdir("../application")
print(os.getcwd())
from .api_functions import db_register


print("fin")




#def test_db_register():
#    
#    # success
#    ip = "1.2.3.4.5"
#    email = "homer@gmail.com"
#    password = "homerPass"
#    is_admin = False
#    result1 = db_register(ip, email, password, is_admin)
#    assert(result1["status"] == 0)
#    
#    # fail: user already exists
#    result2 = db_register(ip, email, password, is_admin)
#    assert(result2["status"] == 1)
#    
#    # delete the new user
#    if result1["status"] == 0:

    
#    
#    
#def test_db_login():
#    
#    # success
#    result = db_login(ip, email, password)
#    assert(result["status"] == 0)
#    
#    # fail: email doesn't exist
#    result = db_login(ip, email, password)
#    assert(result["status"] == 1)
#    
#    # fail: hashPass not correct
#    assert(result["status"] == 1)

        
        
        
        
        
        
        
        
        
        
        
