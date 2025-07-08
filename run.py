from app import create_app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
import os
from dotenv import load_dotenv


load_dotenv()

db = SQLAlchemy()
migrate = Migrate()
admin = Admin(template_mode='bootstrap3')


def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    admin.init_app(app)

    with app.app_context():
        db.create_all()

    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
