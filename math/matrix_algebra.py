import numpy as np

#Define matrices and vectors

A = np.array([[1, 2, 3], [2, 7, 4]])
B = np.array([[1, -1], [0, 1]])
C = np.array([[5, -1], [9, 1], [6, 0]])
D = np.array([[3, -2, -1], [1, 2, 3]])
u = np.array([6, 2, -3, 5])
v = np.array([3, 5, -1, 4])
w = np.array([[1], [8], [0], [5]])
alpha = 6

#Q1 Find dimensions

print "Dimension of A:", A.shape
print "Dimension of B:", B.shape
print "Dimension of C:", C.shape
print "Dimension of D:", D.shape
print "Dimension of u:", u.shape
print "Dimension of w:", w.shape

#Q2 Vector operations

print "u + v:", u + v
print "u -v:", u - v
print "6u: ", alpha*u
print "u.v:", np.dot(u,v)
print "||u||:", np.linalg.norm(u)

#Q3 Matrix operations

#print A + C - error - not defined
print "A - C transpose:", A - C.T
print "C transpose - 3D:", C.T + 3*D
print "BA:", np.dot(B, A)
#print np.dot(B, A.T) - error - not defined

# Optional
#print np.dot(B, C) - error - not defined
print "CB: ", np.dot(C, B)
X = np.dot(B, B)
print "B^4: ", np.dot(X, X)
print "A.transpose(A): ", np.dot(A, A.T)
print "D.transpose(D): ", np.dot(D.T, D)
