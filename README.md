# Vector and Matrix Objects

## Description

Implement various vector and matrix math objects using no math libraries

## Objectives

### Learning Objectives

After completing this assignment, you should understand:

* List comprehensions
* Introductory linear algebra concepts
* Raising exceptions
* Creating classes
* Using `__` "magic" methods

### Performance Objectives

After completing this assignment, you should be able to:

* Perform mathematical operations on complex list structures

## Details

### Deliverables

* A Git repo called matrix-objects containing at least:
  * `README.md` file explaining how to run your project
  * a module called `matrix_math`
  * tests for `matrix_math`

### Requirements

* Passing unit tests
* No PEP8 or Pyflakes warnings or errors
* No use of third-party libraries - only built in `+ - / *` operators and the `math` module

## Normal Mode

Implement two object types, `Matrix` and `Vector`. These objects should implement:

<!-- * shape -->
<!-- * addition and subtraction -->
<!-- * multiplication by a scalar -->
* matrix multiplication by a vector
* matrix multiplication by a matrix
* vector dot product
* vector magnitude

These functions are all defined in [the formulas notebook](Formulas.ipynb) included with this assignment.

These functions must:

* Check the shape of the incoming vector or matrix before any calculations

You should think about how you create the initial objects. It is suggested that
you be able to write:

```py
Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
Vector([1, 5])
```

Also think about whether Vector might inherit from Matrix or vice-versa.
Vectors can often be treated as 1-dimensional matrices.

Solve the problem in [the Population Growth notebook](Population Growth.ipynb).

## Hard Mode

Make sure your objects can be used with standard Python operators. The
following should all be valid:

```python
Vector([1, 2]) + Vector([0, 4])
Vector([1, 2]) - Vector([0, 4])
Vector([1, 2]) * 3

Vector([1, 2]) == Vector([1, 2]) # results in True

Matrix([[0, 1], [1, 0]]) + Matrix([[1, 1], [0, 0]])
Matrix([[0, 1], [1, 0]]) - Matrix([[1, 1], [0, 0]])
Matrix([[0, 1], [1, 0]]) * 3
Matrix([[0, 1], [1, 0]]) * Vector([1, 2])
Matrix([[1, 1, 1], [0, 0, 0]]) * Matrix([[1, 1], [2, 2], [3, 3]])

Matrix([[0, 1], [1, 0]]) == Matrix([[1, 1], [0, 0]]) # results in False
```

Add the following abilities to matrix objects:

* matrix rotation

Research static methods and add the following abilities on the Matrix class:

* create a matrix from a size and a function

## Reading

* [A Guide to Python's Magic Methods](http://www.rafekettler.com/magicmethods.html)
* [Math Matters: Why Do I Need to Know This?](https://www.wku.edu/mathmatters/documents/mathmattersep13.pdf) - a great
explanation of how matrix math can help you with probabilities
