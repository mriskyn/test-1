from flask import Flask
from routes import routers

app = Flask(__name__)

routers(app)

if __name__ == "__main__":
  app.run(debug=True)