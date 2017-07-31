from flask import Blueprint, render_template, redirect, url_for
from flask import request
from flask import current_app

from libs.entities import search, remove, get


app_routes = Blueprint('app', __name__,
                       template_folder='templates')


@app_routes.route('/', methods=['GET'])
def list():
    try:
        page = int(request.args.get('page', 1))
    except ValueError:
        page = 1

    results = search(
      index_name=current_app.config['ELASTICSEARCH_INDEX']['index_name'],
      doc_type=current_app.config['ELASTICSEARCH_INDEX']['index_name'],
      offset=(page - 1) * current_app.config['PER_PAGE'],
      limit=current_app.config['PER_PAGE']
    )
    return render_template('index.html', results=results, current_page=page)


@app_routes.route('/delete/<id>', methods=['GET'])
def delete_place(id):
    remove(
        index_name=current_app.config['ELASTICSEARCH_INDEX']['index_name'],
        doc_type=current_app.config['ELASTICSEARCH_INDEX']['index_name'],
        object_id=id 
    )
    return redirect(url_for('app.list'))


@app_routes.route('/detail/<id>', methods=['GET'])
def detail(id):
    item = get(
        index_name=current_app.config['ELASTICSEARCH_INDEX']['index_name'],
        doc_type=current_app.config['ELASTICSEARCH_INDEX']['index_name'],
        object_id=id 
    )
    return render_template('detail.html', item=item)
