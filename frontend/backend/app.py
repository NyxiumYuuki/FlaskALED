print("Import backend")
from application import create_app
print("Import os")
import os

app = create_app(os.environ.get('FLASK_ENV'))

if __name__ == "__main__":
  app.run(host='0.0.0.0', DEBUG=True)
