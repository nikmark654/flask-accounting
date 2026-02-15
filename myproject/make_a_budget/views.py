from flask import Blueprint,render_template,redirect,url_for
# from myproject.journal_entry.templates.forms import JournalEntries

make_a_budget_blueprint = Blueprint(
    'make_a_budget', 
    __name__, 
    template_folder='templates/make_a_budget'
    )

@make_a_budget_blueprint.route('/make_a_budget', methods = ['GET', 'POST'])
def render_make_a_budget():
    return render_template('make_a_budget.html')