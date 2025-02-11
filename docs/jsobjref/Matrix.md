.. _jsobjref/Matrix:

Matrix
################################################################################

``matrix``

**Description**

A transformation matrix specification, used to transform the geometry of objects. Use it to specify and retrieve matrix information from an Illustrator document or from page items in a document.

Matrices are used in conjunction with the ``transform`` method and as a property of a number of objects. A matrix specifies how to transform the geometry of an object. You can generate an original matrix using the :ref:`jsobjref/Application` object methods :ref:`jsobjref/Application.getTranslationMatrix`, :ref:`jsobjref/Application.getScaleMatrix`, or :ref:`jsobjref/Application.getRotationMatrix`.

A ``Matrix`` is a record containing the matrix values, not a reference to a matrix object. The matrix commands operate on the values of a matrix record. If a command modifies a matrix, a modified matrix record is returned as the result of the command. The original matrix record passed to the command is not modified.

----

==========
Properties
==========

.. _jsobjref/Matrix.mValueA:

Matrix.mValueA
********************************************************************************

``matrix.mValueA``

**Description**

Matrix property ``a``.

**Type**

Number (double).

----

.. _jsobjref/Matrix.mValueB:

Matrix.mValueB
********************************************************************************

``matrix.mValueB``

**Description**

Matrix property ``b``.

**Type**

Number (double).

----

.. _jsobjref/Matrix.mValueC:

Matrix.mValueC
********************************************************************************

``matrix.mValueC``

**Description**

Matrix property ``c``.

**Type**

Number (double).

----

.. _jsobjref/Matrix.mValueD:

Matrix.mValueD
********************************************************************************

``matrix.mValueD``

**Description**

Matrix property ``d``.

**Type**

Number (double).

----

.. _jsobjref/Matrix.mValueTX:

Matrix.mValueTX
********************************************************************************

``matrix.mValueTX``

**Description**

Matrix property ``tx``.

**Type**

Number (double).

----

.. _jsobjref/Matrix.mValueTY:

Matrix.mValueTY
********************************************************************************

``matrix.mValueTY``

**Description**

Matrix property ``ty``.

**Type**

Number (double).

----

.. _jsobjref/Matrix.typename:

Matrix.typename
********************************************************************************

``matrix.typename``

**Description**

The class name of the referenced object.

**Type**

String, read-only.

----

=======
Example
=======

Combining matrices to apply multiple transformations
********************************************************************************

To apply multiple transformations to objects, it is more efficient to use the matrix suite than to apply the transformations one at a time. The following script demonstrates how to combine multiple matrices.

::

  // Tranforms all art in a document using translation and rotation matrices,
  // moves art half an inch to the right and 1.5 inches up on the page
  if (app.documents.length > 0) {
    var moveMatrix = app.getTranslationMatrix(0.5, 1.5);

    // Add a rotation to the translation, 10 degrees counter clockwise
    var totalMatrix = concatenateRotationMatrix(moveMatrix, 10);

    // apply the transformation to all art in the document
    var doc = app.activeDocument;
    for (var i = 0; i < doc.pageItems.length; i++) {
      doc.pageItems[i].transform(totalMatrix);
    }
  }
