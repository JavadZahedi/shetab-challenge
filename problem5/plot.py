import numpy as np
import matplotlib.pyplot as plt
import io
import base64

LINESPACE_LEN = 50000
ORDER = 3

def make_y(params, x):
    y = np.array([0.0] * LINESPACE_LEN)
    for i in range(ORDER + 1):
        y += params[i] * (x ** (ORDER-i))
    return y

def sign(x):
    if x >= 0:
        return '+'
    return '-'
        

def make_term(ratio, exp):
    if abs(ratio) == 1:
        if exp == 0:
            return f'{sign(ratio)} 1'
        elif exp == 1:
            return f'{sign(ratio)} x'
        else:
            return f'{sign(ratio)} x^{exp}'
    else:
        if exp == 0:
            return f'{sign(ratio)} {abs(ratio)}'
        elif exp == 1:
            return f'{sign(ratio)} {abs(ratio)}x'
        else:
            return f'{sign(ratio)} {abs(ratio)}x^{exp}'


def make_label(params):
    terms = [make_term(params[i], ORDER-i)
             for i in range(ORDER+1) if params[i] != 0]
    if terms:
        return ' '.join(['y =', *terms])
    else:
        return 'y = 0'


def draw_function(*args):
    assert len(args) == (ORDER+1) * 2
    x = np.linspace(0, 100, LINESPACE_LEN)
    y1 = make_y(args[:ORDER+1], x)
    y2 = make_y(args[ORDER+1:], x)

    fig, ax = plt.subplots()
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')

    plt.plot(x, y1, color='blue', label=make_label(args[:ORDER+1]))
    plt.plot(x, y2, color='red', label=make_label(args[ORDER+1:]))
    plt.title('Two functions\' graphs in [0,100] domain', font='serif')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.legend()
    
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return f'data:image/png;base64,{plot_url}'


if __name__ == '__main__':
    draw_function(-2, 9, -10, 15, 1, -10, +6, -100)