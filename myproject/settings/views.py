from flask import Blueprint,render_template,redirect,url_for
# from myproject.journal_entry.templates.forms import JournalEntries

settings_blueprint = Blueprint(
    'settings', 
    __name__, 
    template_folder='templates/settings'
    )

@settings_blueprint.route('/settings', methods = ['GET', 'POST'])
def render_settings():
    return render_template('settings.html')