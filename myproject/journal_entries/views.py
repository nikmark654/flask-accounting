from flask import Blueprint,render_template,redirect,url_for
# from myproject.journal_entry.templates.forms import JournalEntries

journal_entries_blueprint = Blueprint(
    'journal_entries', 
    __name__, 
    template_folder='templates/journal_entries'
    )

@journal_entries_blueprint.route('/', methods = ['GET', 'POST'])
def render_journal_entries():
    return render_template('journal_entries.html')