# Third party modules
import pytest
from datetime import date

from __init__ import create_app, db
from users_model import Users
from logs_model import Logs

import fictive_users
import ficitve_logs


@pytest.fixture
def client():
    app = create_app()

    app.config["TESTING"] = True
    app.testing = True


    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"

    client = app.test_client()
    with app.app_context():
        db.create_all()
  
        for i in range(1,6):
            db.session.add(fictive_users.get_user_object(i))
            
        for i in range(1,3):
            db.session.add(ficitve_logs.get_log_object(i))
     
        db.session.commit()
    
    yield client



def test_get_user(client):
    index = 1
    predict_results = client.get("/api/users/{}}".format(index))
    true_results = fictive_users.get_user_json(index)
    assert predict_results.json == true_results

    




    
    
    
    