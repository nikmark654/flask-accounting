from flask import Blueprint,render_template,redirect,url_for
# from myproject.journal_entry.templates.forms import JournalEntries

edit_templates_blueprint = Blueprint(
    'edit_templates', 
    __name__, 
    template_folder='templates/edit_templates'
    )

@edit_templates_blueprint.route('/edit_templates', methods = ['GET', 'POST'])
def render_edit_templates():
    return render_template('edit_templates.html')