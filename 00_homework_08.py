import flask
import stocklib
import matplotlib.pyplot as plt
import sys

IMAGE_FILENAME = 'static/images/{ticker}.png'
app = flask.Flask(__name__)

def write_chart(stock_obj):
    """ given a stock object, create and save a chart based on its .history attribute """
    image_filename = IMAGE_FILENAME.format(ticker=stock_obj.ticker)
    plt.plot(stock_obj.history)
    plt.ylabel('price')
    plt.savefig(image_filename)
    return image_filename

@app.route('/')
def display_input_form():
    return flask.render_template('stock_ticker_input_form.html')

@app.route('/chart')
def display_chart():
    stock_ticker = flask.request.args.get('ticker')
    interval = flask.request.args.get('interval')
    stock_obj = stocklib.Stock(stock_ticker, interval.split('min')[0])
    write_chart(stock_obj)
    return flask.render_template('stock_price_template.html', obj = stock_obj, image_path=f'images/{stock_ticker}.png')


if __name__ == '__main__':
    app.run(debug=True, port=8000)