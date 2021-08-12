import numpy as np
import matplotlib.pyplot as plt
import io
import base64

def draw_function(a1, b1, c1, d1, a2, b2, c2, d2):
    x = np.linspace(0, 100, 5000)
    y1 = a1*x**3 + b1*x**2 + c1*x + d1
    y2 = a2*x**3 + b2*x**2 + c2*x + d2

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    plt.plot(x,y1, 'b', label=f'y=({a1})(x^3)+({b1})(x^2)+({c1})(x)+({d1})')
    plt.plot(x,y2, 'c', label=f'y=({a2})(x^3)+({b2})(x^2)+({c2})(x)+({d2})')
    plt.legend(loc='best')
    
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return f'data:image/png;base64,{plot_url}'


if __name__ == '__main__':
    draw_function(-2, 9, -10, 15, 1, -10, +6, -100)