#------------------------------------------------------------------------------
# Chad Baker
# clbaker@ucsc.edu
# CSE20 Fall 2021
# Pa7
#
#  matrix.py
# This class uses many funstions to add, sub, mult, trans, etc Matricies
#------------------------------------------------------------------------------
from random import uniform

class Matrix:
   """Class representing a rectangular matrix."""

   # built-in methods ---------------------------------------------------------

   def __init__(self, L=[]):
      """
      Initialize a Matrix object from a list of lists. If the list is empty,
      the resulting Matrix is empty (size 0x0).
      """

      # get number of rows and columns
      n = self.numRows = len(L)
      m = self.numCols = ( len(L[0]) if n>0 else 0 )
      self.elements = {}
      if n==0: 
         return
      # end if
      
      # build dictionary
      if n>0:
         for i in range(n):
            if len(L[i])!=m:
               msg = f'could not create Matrix from ragged list:\n{L}'
               raise ValueError(msg)
            # end if
            for j in range(m):
               self.elements[(i+1,j+1)] = L[i][j]
            # end for
         # end for
      # end if
   # end __init__()

   def __str__(self):
      '''
      Return string representation of self.
      '''
      s = ''
      for i in range(self.numRows):
         for j in range(self.numCols):
            if j == 0:
               s += f'{self.elements[(i+1,j+1)]:>8.2f}'
            else:   
               s += f'{self.elements[(i+1,j+1)]:>9.2f}'
         s += '\n'
      s = s[:-1]
      return s
      
   def __eq__(self, other):
      '''
      Return True if self==other, False otherwise.
      '''
      for i in range(self.numRows):
         for j in range(self.numCols):
            if self.elements[(i+1,j+1)] != other.elements[(i+1,j+1)]:
               return False
      return True

   # Matrix instance methods --------------------------------------------------

   def add(self, other):
      '''
      Return sum of self with other.
      '''
      if self.numRows != other.numRows or self.numCols != other.numCols:
         raise ValueError('add(): incompatible matrix sizes:\n'+str(self.numRows)+'x'+str(self.numCols)+':\n'+str(self)+'\n'+str(other.numRows)+'x'+str(other.numCols)+':\n'+str(other)+'\n')
      L = []
      for i in range(self.numRows):
         row = []
         for j in range(self.numCols):
            row.append(self.elements[(i+1,j+1)] + other.elements[(i+1,j+1)])
         L.append(row)
      return Matrix(L)

   def sub(self, other):
      '''
      Return difference of self with other.
      '''
      if self.numRows != other.numRows or self.numCols != other.numCols:
         raise ValueError('sub(): incompatible matrix sizes:\n'+str(self.numRows)+'x'+str(self.numCols)+':\n'+str(self)+'\n'+str(other.numRows)+'x'+str(other.numCols)+':\n'+str(other)+'\n')
      L = []
      for i in range(self.numRows):
         row = []
         for j in range(self.numCols):
            row.append(self.elements[(i+1,j+1)] - other.elements[(i+1,j+1)])
         L.append(row)
      return Matrix(L)

   def scale(self, c):
      '''
      Return the scalar product of self with c.
      '''
      L = []
      for i in range(self.numRows):
         row = []
         for j in range(self.numCols):
            row.append(self.elements[(i+1,j+1)] * c)
         L.append(row)
      return Matrix(L)

   def trans(self):
      '''
      Return the transpose of self.
      '''
      L = [[j for j in range(self.numRows)] for i in range(self.numCols)]
      for i in range(self.numRows):
         for j in range(self.numCols):
            L[j][i] = self.elements[(i+1,j+1)]
      return Matrix(L)

   def mult(self, other):  
      '''
      Return product of self by other.
      '''
      if self.numCols != other.numRows:
         raise ValueError('mult(): incompatible matrix sizes:\n'+str(self.numRows)+'x'+str(self.numCols)+':\n'+str(self)+'\n'+str(other.numRows)+'x'+str(other.numCols)+':\n'+str(other)+'\n')
      sum = 0
      L = []
      M = []
      for i in range(self.numRows):
         row = []
         for j in range(self.numCols):
            row.append(self.elements[(i+1,j+1)])
         M.append(row)

      B = [[j for j in range(other.numRows)] for i in range(other.numCols)]
      for i in range(other.numRows):
         for j in range(other.numCols):
            B[j][i] = other.elements[(i+1,j+1)]
      
      for f in M:
         row = []
         for s in B:
            for i in range(len(f)):
               sum += f[i] * s[i]
            row.append(sum)
            sum = 0
         L.append(row)
      return Matrix(L)

   # Matrix class methods -----------------------------------------------------
   
   def from_string(s=''):
      '''
      Return the Matrix represented by the string s. If s is empty, the
      resulting Matrix is empty (size 0x0).
      '''
      x = s.replace(' ','')
      L = x.split('\n')
      for i in range(len(L)):
         if len(L[0]) != len(L[i]):
            raise ValueError('from_string(): could not create Matrix from ragged string:\n'+repr(s))
      for i in range(len(L)):
         L[i] = list(L[i])
         for j in range(len(L[0])):
            L[i][j] = int(L[i][j])
      return Matrix(L)

   def identity(n):
      '''
      Return the nxn identity Matrix.
      '''
      L = []
      for i in range(n):
         row = []
         for j in range(n):
            if i == j:
               row.append(1)
            else:
               row.append(0)
         L.append(row)
      return Matrix(L)

   def randMatrix(n, m, a, b):
      '''
      Return an nxm Matrix with random elements x, uniformly distributed over
      the interval a<=x<=b.
      '''
      L = []
      for i in range(n):
         row = []
         for j in range(m):
            row.append(uniform(a,b))
         L.append(row)
      return Matrix(L)

# end class Matrix ------------------------------------------------------------
