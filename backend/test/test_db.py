def preparation_test():
    
    # TODO supprimer Riri1
    # TODO supprimer Riri2



def test_db_register():
    
    # success
    result = db_register(ip, email, login, password, is_admin)
    assert(result["status"] == 0)
    
    # fail: user already exists
    result = db_register(ip, email, login, password, is_admin)
    assert(result["status"] == 1)
    
    
    
    
def test_db_login():
    
    # success
    result = db_login(ip, email, password)
    assert(result["status"] == 0)
    
    # fail: email doesn't exist
    result = db_login(ip, email, password)
    assert(result["status"] == 1)
    
    # fail:  hashPass not correct
    assert(result["status"] == 1)
    
    
    
    