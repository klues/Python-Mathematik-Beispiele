import scipy.optimize as optimize
def rosen(x):
    """The Rosenbrock function"""
    return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)
x0 = [1.3, 0.7, 0.8, 1.9, 1.2]
xopt = optimize.fmin(rosen, x0, xtol=1e-8, disp=True)
# Optimization terminated successfully.
#          Current function value: 0.000000
#          Iterations: 339
#          Function evaluations: 571
print(xopt)