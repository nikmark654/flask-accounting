from flask import Blueprint,render_template,redirect,url_for
# from myproject.journal_entry.templates.forms import JournalEntries

journal_entry_blueprint = Blueprint(
    'journal_entry', 
    __name__, 
    template_folder='templates/journal_entry'
    )

@journal_entry_blueprint.route('/', methods = ['GET', 'POST'])
def render_journal_entries():
    return render_template('journal_entry.html')