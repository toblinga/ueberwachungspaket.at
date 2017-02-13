from flask import Flask
from .representatives import Representatives

app = Flask(__name__)
app.config.from_pyfile("config.py")
app.config.from_pyfile("config_sensitive.py")
reps = Representatives()

if __name__ == "__main__":
    app.run()

from . import views
