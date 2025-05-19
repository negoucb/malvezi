from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
from .routes.cliente_routes import cliente_bp
from .routes.funcionario_routes import funcionario_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    app.register_blueprint(cliente_bp, url_prefix='/cliente')
    app.register_blueprint(funcionario_bp, url_prefix='/funcionario')

    return app
