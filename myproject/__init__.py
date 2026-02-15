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


from myproject.journal_entry.views import journal_entry_blueprint
from myproject.financial_standing.views import financial_standing_blueprint
from myproject.make_a_budget.views import make_a_budget_blueprint
from myproject.edit_templates.views import edit_templates_blueprint
from myproject.settings.views import settings_blueprint

server.register_blueprint(journal_entry_blueprint, url_prefix="")
server.register_blueprint(financial_standing_blueprint, url_prefix="")
server.register_blueprint(make_a_budget_blueprint, url_prefix="")
server.register_blueprint(edit_templates_blueprint, url_prefix="")
server.register_blueprint(settings_blueprint, url_prefix="")