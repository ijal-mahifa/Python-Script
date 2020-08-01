import flask
import main
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


# A route to return all of the available entries in our catalog.
@app.route('/api/crawl_nike/v1/all', methods=['GET'])
def all_product():
    list_json = main.main()
    return jsonify({
        'Catalog': 'All',
        'Result': len(list_json),
        'data': list_json
                    })


# A route to return men entries in our catalog.
@app.route('/api/crawl_nike/v1/men', methods=['GET'])
def men_product():
    list_json = main.main()
    list_gend = []
    for list_gen in list_json:
        if "MEN" in list_gen['genders']:
            list_gend.append(list_gen)
    return jsonify({
        'Catalog': 'MEN',
        'Result': len(list_gend),
        'data': list_gend
    })


# A route to return women entries in our catalog.
@app.route('/api/crawl_nike/v1/women', methods=['GET'])
def women_product():
    list_json = main.main()
    list_gend = []
    for list_gen in list_json:
        if "WOMEN" in list_gen['genders']:
            list_gend.append(list_gen)
    return jsonify({
        'Catalog': 'WOMEN',
        'Result': len(list_gend),
        'data': list_gend
    })


# A route to return boys entries in our catalog.
@app.route('/api/crawl_nike/v1/boys', methods=['GET'])
def boys_product():
    list_json = main.main()
    list_gend = []
    for list_gen in list_json:
        if "BOYS" in list_gen['genders']:
            list_gend.append(list_gen)
    return jsonify({
        'Catalog': 'BOYS',
        'Result': len(list_gend),
        'data': list_gend
    })


# A route to return girls entries in our catalog.
@app.route('/api/crawl_nike/v1/girls', methods=['GET'])
def girls_product():
    list_json = main.main()
    list_gend = []
    for list_gen in list_json:
        if "GIRLS" in list_gen['genders']:
            list_gend.append(list_gen)
    return jsonify({
        'Catalog': 'GIRLS',
        'Result': len(list_gend),
        'data': list_gend
    })


if __name__ == '__main__':
    app.run()
