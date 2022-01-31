from . import create_app
import os

app = create_app(os.environ.get('FLASK_ENV', None))

if __name__ == "__main__":
    app.run(host='0.0.0.0', DEBUG=True)
