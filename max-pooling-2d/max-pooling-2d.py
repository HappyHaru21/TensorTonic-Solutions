def max_pooling_2d(X, pool_size):
    """
    Apply 2D max pooling with non-overlapping windows.
    """
    # Write code here
    h, w = len(X), len(X[0])
    return [[max(val for row in X[i:i+pool_size] for val in row[j:j+pool_size]) 
             for j in range(0, w // pool_size * pool_size, pool_size)] 
            for i in range(0, h // pool_size * pool_size, pool_size)]