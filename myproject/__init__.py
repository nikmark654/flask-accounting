from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from platformdirs import user_desktop_dir

server = Flask(__name__)

server.config['SECRET_KEY'] = 'mysecretkey'
basedir = user_desktop_dir() # /Users/nickmarkoulis/Library/Application Support
server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + user_desktop_dir()
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(server)
Migrate(server, db)


# from myproject.journal_entry.views import 
# from myproject.financial_standing.views import 
# from myproject.make_a_budget.views import
# from myproject.settings.views import

# app.register_blueprint(owners_blueprint,url_prefix="/owners")
# app.register_blueprint(puppies_blueprint,url_prefix='/puppies')