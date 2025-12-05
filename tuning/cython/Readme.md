# C modules

You can write modules in C for python and you can find two examples here. One is for pure C code and one is for Cython

## Cython -- Static Compilation for Python

## Why Use Cython?

-   Fastest option for CPU-bound code
-   Full access to:
    -   C types
    -   C++ interop
    -   External libraries
-   Release the GIL for parallel loops

## Example Cython Function (typed)

``` cython
cpdef long fast_sum(long[:] items):
    cdef long total = 0
    cdef Py_ssize_t i
    for i in range(items.shape[0]):
        total += items[i]
    return total
```

## Releasing the GIL

``` cython
cdef void compute(double[:] arr) nogil:
    cdef Py_ssize_t i
    for i in range(arr.shape[0]):
        arr[i] = arr[i] * 1.2
```

## When to Use Cython

-   Hot loops
-   Numeric kernels
-   Cryptographic code
-   Interfacing C/C++

