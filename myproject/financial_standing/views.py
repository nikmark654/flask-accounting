from flask import Blueprint,render_template,redirect,url_for
# from myproject.journal_entry.templates.forms import JournalEntries

financial_standing_blueprint = Blueprint(
    'financial_standing', 
    __name__, 
    template_folder='templates/financial_standing'
    )

@financial_standing_blueprint.route('/financial_standing', methods = ['GET', 'POST'])
def render_financial_standing():
    return render_template('financial_standing.html')