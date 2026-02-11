import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    x= np.array(x)
    n = len(x)
    x_bar = np.mean(x)
    s=np.std(x,ddof=1)
    se = s/np.sqrt(n)
    t_stat=(x_bar-mu0)/se
    return t_stat