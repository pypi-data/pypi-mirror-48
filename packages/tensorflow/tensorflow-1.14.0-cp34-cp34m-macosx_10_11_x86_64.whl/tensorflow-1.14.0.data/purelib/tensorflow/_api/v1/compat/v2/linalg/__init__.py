# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator/create_python_api.py script.
"""Operations for linear algebra.
"""

from __future__ import print_function as _print_function

from tensorflow.python import cholesky
from tensorflow.python import cholesky_solve
from tensorflow.python import cross
from tensorflow.python import diag as tensor_diag
from tensorflow.python import diag_part as tensor_diag_part
from tensorflow.python import einsum
from tensorflow.python import eye
from tensorflow.python import global_norm
from tensorflow.python import log_matrix_determinant as slogdet
from tensorflow.python import lu
from tensorflow.python import matmul
from tensorflow.python import matrix_band_part as band_part
from tensorflow.python import matrix_determinant as det
from tensorflow.python import matrix_diag as diag
from tensorflow.python import matrix_diag_part as diag_part
from tensorflow.python import matrix_inverse as inv
from tensorflow.python import matrix_logarithm as logm
from tensorflow.python import matrix_set_diag as set_diag
from tensorflow.python import matrix_solve as solve
from tensorflow.python import matrix_solve_ls as lstsq
from tensorflow.python import matrix_square_root as sqrtm
from tensorflow.python import matrix_transpose
from tensorflow.python import matrix_triangular_solve as triangular_solve
from tensorflow.python import matvec
from tensorflow.python import norm_v2 as norm
from tensorflow.python import qr
from tensorflow.python import self_adjoint_eig as eigh
from tensorflow.python import self_adjoint_eigvals as eigvalsh
from tensorflow.python import svd
from tensorflow.python import tensordot
from tensorflow.python import trace
from tensorflow.python.ops.linalg.linalg import LinearOperator
from tensorflow.python.ops.linalg.linalg import LinearOperatorBlockDiag
from tensorflow.python.ops.linalg.linalg import LinearOperatorCirculant
from tensorflow.python.ops.linalg.linalg import LinearOperatorCirculant2D
from tensorflow.python.ops.linalg.linalg import LinearOperatorCirculant3D
from tensorflow.python.ops.linalg.linalg import LinearOperatorComposition
from tensorflow.python.ops.linalg.linalg import LinearOperatorDiag
from tensorflow.python.ops.linalg.linalg import LinearOperatorFullMatrix
from tensorflow.python.ops.linalg.linalg import LinearOperatorIdentity
from tensorflow.python.ops.linalg.linalg import LinearOperatorKronecker
from tensorflow.python.ops.linalg.linalg import LinearOperatorLowRankUpdate
from tensorflow.python.ops.linalg.linalg import LinearOperatorLowerTriangular
from tensorflow.python.ops.linalg.linalg import LinearOperatorScaledIdentity
from tensorflow.python.ops.linalg.linalg import LinearOperatorToeplitz
from tensorflow.python.ops.linalg.linalg import LinearOperatorZeros
from tensorflow.python.ops.linalg.linalg import adjoint
from tensorflow.python.ops.linalg.linalg import logdet
from tensorflow.python.ops.linalg.linalg import matrix_exponential as expm
from tensorflow.python.ops.linalg.linalg import tridiagonal_matmul
from tensorflow.python.ops.linalg.linalg import tridiagonal_solve
from tensorflow.python.ops.linalg.linear_operator_adjoint import LinearOperatorAdjoint
from tensorflow.python.ops.linalg.linear_operator_householder import LinearOperatorHouseholder
from tensorflow.python.ops.linalg.linear_operator_inversion import LinearOperatorInversion
from tensorflow.python.ops.nn import l2_normalize_v2 as l2_normalize

del _print_function
