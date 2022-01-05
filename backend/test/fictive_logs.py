from logs_model import Logs
from datetime import date


TAB_LOG = [
    {
        "id": 1,
        "date": date.fromisoformat('2021-12-04'),
        "user": "riri",
        "ip": "0.0.0.0",
        "table": "Users",
        "action": "connexion",
        "status": "succes",
        "status_code": 200
    },
    {
        "id": 2,
        "date": date.fromisoformat('2021-12-04'),
        "user": "fifi",
        "ip": "0.0.0.0",
        "table": "Users",
        "action": "connexion",
        "status": "succes",
        "status_code": 200
    },
    {
        "id": 3,
        "date": date.fromisoformat('2021-12-04'),
        "user": "loulou",
        "ip": "0.0.0.0",
        "table": "Users",
        "action": "connexion",
        "status": "succes",
        "status_code": 200
    },
]


def get_log_object(i: int):
    return Logs(
        id=TAB_LOG[i]["id"],
        date=TAB_LOG[i]["date"],
        user=TAB_LOG[i]["user"],
        ip=TAB_LOG[i]["ip"],
        table=TAB_LOG[i]["table"],
        action=TAB_LOG[i]["action"],
        status=TAB_LOG[i]["status"],
        status_code=TAB_LOG[i]["status_code"]
    )


def get_log_json(i: int):
    return TAB_LOG[i]






