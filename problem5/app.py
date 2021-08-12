from flask import Flask, request, render_template
from plot import draw_function
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        params = ['a1', 'b1', 'c1', 'd1', 'a2', 'b2', 'c2', 'd2']
        plot = draw_function(*[int(request.form[p]) for p in params])
        return render_template('index.html', plot=plot)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)