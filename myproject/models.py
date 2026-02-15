# THIS IS THE DB MODELS. A CLASS OBJECT FOR EACH DB TABLE.
# In order to work, we have to set up db inside the __init__.py under myproject folder
from myproject import db

class JounralEntries(db.Model):

    __tablename__ = 'journal_entries'
    entry_no = db.Column(db.Integer, primary_key = True)
    profile_id = db.relationship('Profile', backred = '', uselist = False)
    entry_date = db.Column(db.Integer)