from flask import Flask
from .routes.routes import pessoa_bp

app = Flask(__name__)

app.register_blueprint(pessoa_bp)

if __name__ == '__main__':
    app.run(debug=True)
