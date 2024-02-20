# Program to multiply two matrices using nested loops
import random
import time
import numpy as np

# @profile
def main():
    N = 250
    
    # NxN matrix
    X = []
    for i in range(N):
        X.append([random.randint(0,100) for r in range(N)])
    
    # Nx(N+1) matrix
    Y = []
    for i in range(N):
        Y.append([random.randint(0,100) for r in range(N+1)])
    
    # result is Nx(N+1)
    result = []
    for i in range(N):
        result.append([0] * (N+1))
    
    X_np = np.matrix(X)
    Y_np = np.matrix(Y)
    
    st = time.time()
    numpy_result = np.matmul(X_np, Y_np)
    np_time = time.time()-st
    
    st = time.time()

    # iterate through rows of X
    for i in range(len(X)):
        # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    original_time = time.time()-st
    
    original_result = np.matrix(result)
    
    print(f"Numpy time {np_time*1000:f} ms, Original Time: {original_time*1000:f} ms")
    
    if not np.any(original_result-numpy_result  != 0):
        print("Numpy result matches the original method result")
    else:
        print("Numpy result does NOT match the original method result")
                  
#    for r in result:
 #       print(r)

if __name__ == "__main__":
    main()