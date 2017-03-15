# Matrix Algebra


import numpy as np
from numpy import linalg as LA
import math

A = np.array([
    (1, 2, 3),
    (2, 7, 4)])

B = np.array([
    (1, -1),
    (0, 1)])

C = np.array([
    (5, -1),
    (9, 1),
    (6, 0)])

D = np.array([
    (3, -2, -1),
    (1, 2, 3)])

u = np.array([6, 2, -3, 5])
v = np.array([3, 5, -1, 4])
w = np.array([[1], [9], [0], [5]])

print('Matrix Dimensions')
print('A: %s' % (A.shape,))
print('B: %s' % (B.shape,))
print('C: %s' % (C.shape,))
print('D: %s' % (D.shape,))
print('u: %s' % (u.shape,))
print('w: %s' % (w.shape,))
print('')

print('Vector Operations')
alpha = 6
print('u + v = %s' % (u+v,))
print('u - v = %s' % (u-v,))
print('alpha * u = %s' % (alpha * u,))
print('u dot v = %s' % (u.dot(v),))
print('u norm = %s' % LA.norm(u))
print('')

print('Matrix Operations')

print('A + C :')
print(np.vstack((A,np.zeros(3))) + np.hstack((C, np.zeros((3,1)))))
print('')

print('A - C transpose :')
print(A - C.transpose())
print('')
print('C transpose + 3 * D:')
print(C.transpose() + 3 * D)
print('')

#np.hstack((np.vstack((B,np.zeros(2))), np.zeros((3,1)))) * A

print('BA :')

print(np.dot(B,A))
print('')

print('B(A transpose) :')

print(np.dot(np.hstack((B,np.zeros((2,1)))),A.transpose()))
print('')

print('Optional')
print('BC :')
print(np.dot(np.hstack((B,np.zeros((2,1)))),C))
print('')

print('CB :')
print(np.dot(C,B))
print('')

print('B^4 :')
print(LA.matrix_power(B,4))
print('')

print('A(A transpose):')
print(np.dot(A,A.transpose()))
print('')

print('(D transpose)D :')
print(np.dot(D.transpose(),D))
print('')
