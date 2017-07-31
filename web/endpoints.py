from flask import Blueprint, render_template


app_routes = Blueprint('app', __name__,
                       template_folder='templates')


@app_routes.route('/', methods=['GET'])
def list():
    return render_template('index.html')
