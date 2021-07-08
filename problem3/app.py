from flask import Flask, request, render_template
from plot import draw_spline
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        draw_spline(int(request.form['t']), int(request.form['c']), 
                    int(request.form['k']))
        return render_template('index.html', plot=True)
    else:
        return render_template('index.html', plot=False)


if __name__ == '__main__':
    app.run(debug=True)