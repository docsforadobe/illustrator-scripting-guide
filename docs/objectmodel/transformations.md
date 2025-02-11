.. _objectmodel/transformations:

Transformations
################################################################################

The ``matrix`` object provides access to the power of geometric-transformation matrices.

Transformation matrices in Illustrator store the settings of an operation that scales, rotates, or moves (translates) an object on a page.

There are advantages to using matrices:

- By storing transformation values in a ``matrix`` object, you can use the values repeatedly on different objects in your script.
- By concatenating rotation, translation, and/or scaling matrices and applying the resulting matrix, you can perform many geometric transformations with only one script statement.
- You can invert matrix values.
- You can compare the values of two matrices.

The ``application`` object. has commands or methods to create, get, invert, compare, or concatenate matrices.

The command or method used to apply a matrix is the ``transform`` command, which belongs to any type of object on which transformations can be performed.
