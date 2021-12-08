from application import create_app
import os

app = create_app()

if __name__ == "__main__":
    PORT = os.environ.get('PORT', 33507)
    app.run(host='0.0.0.0', port=PORT, DEBUG=True)
