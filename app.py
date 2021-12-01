import os
from flask_route import *

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 33507))
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'secret_key')
    app.run(host='0.0.0.0', port=PORT, debug=False)