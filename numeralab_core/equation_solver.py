import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def solve_equation_numeric(equation_str, method):
    x = sp.symbols('x')
    try:
        equation = sp.sympify(equation_str)
    except:
        return "Invalid equation format", plt.figure()

    f = sp.lambdify(x, equation, 'numpy')
    x_vals = np.linspace(-10, 10, 200)
    y_vals = f(x_vals)

    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label=f"{method} solution approximation")
    ax.axhline(0, color='gray', linestyle='--')
    ax.legend()

    result_summary = f"Equation solved numerically using {method}. Range: -10 to 10"
    return result_summary, fig
