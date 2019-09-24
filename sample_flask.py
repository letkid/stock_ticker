

import flask

app = flask.Flask(__name__)   # a Flask object

@app.route('/hello')          # called when visiting web URL 127.0.0.1:5000/hello/
def hello_world():
    return 'hello flask!'

#    name = flask.request.args.get('person_name')
#    occupation = flask.request.args.get('occupation')

    # expected to return a string (usu. the HTML to display)
#    return '<PRE>Hello, World!  {} is a(n) {}</PRE>'.format(name, occupation)
#    return flask.render_template('sample_template.html', person=name, job=occupation)

if __name__ == '__main__':
    app.run(debug=True, port=5000)    # app starts serving in debug mode on port 5000