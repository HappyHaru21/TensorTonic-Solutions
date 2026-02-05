def maxpool_forward(X, pool_size, stride):
    """
    Compute the forward pass of 2D max pooling.
    """
    # Write code here
    H = len(X)
    W = len(X[0])
    H_out = (H-pool_size)//stride+1
    W_out = (W-pool_size)//stride +1
    output = []
    for i in range(H_out):
        output_row = []
        for j in range(W_out):
            start_row = i*stride
            start_col = j*stride
            max_val = X[start_row][start_col]
            for a in range(pool_size):
                for b in range(pool_size):
                    val = X[start_row+a][start_col+b]
                    if val>max_val:
                        max_val=val
            output_row.append(max_val)
        output.append(output_row)
    return output