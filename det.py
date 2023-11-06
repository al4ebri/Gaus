mat = [[-7,-9,1,-9,29],
       [-6,-8,-5,2,42],
       [-3,6,5,-9,11],
       [-2,0,-5,-9,75]]

E = [[1,0,0,0],
     [0,1,0,0],
     [0,0,1,0],
     [0,0,0,1]]


det_mat = [mat[i][:len(mat)] for i in range(len(mat))]
minor_mat = det_mat
for i in range(len(det_mat)): 
    for j in range(len(det_mat)): 
        if i == j: 
            coef = 1/det_mat[i][j]
            minor_mat[i][j] = -coef
            for k in range(len(det_mat)): 
                if k != i:
                     minor_mat[k][j] = 
