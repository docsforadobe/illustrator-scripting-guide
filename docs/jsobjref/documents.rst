.. _jsobjref/documents:

Documents
################################################################################

``documents``

**Description**

A collection of :ref:`jsobjref/document` objects.

----

==========
Properties
==========

.. _jsobjref/documents.length:

Documents.length
********************************************************************************

``app.documents.length``

**Description**

The number of objects in the collection.

**Type**

Number, read-only.

----

.. _jsobjref/documents.parent:

Documents.parent
********************************************************************************

``app.documents.parent``

**Description**

The parent of this object.

**Type**

Object, read-only.

----

.. _jsobjref/documents.typename:

Documents.typename
********************************************************************************

``app.documents.typename``

**Description**

The class name of the referenced object.

**Type**

String, read-only.

----

=======
Methods
=======

.. _jsobjref/documents.add:

Documents.add()
********************************************************************************

::

    app.documents.add([documentColorSpace] [, width] [, height] [, numArtBoards]
        [, artboardLayout] [, artboardSpacing] [, artboardRowsOrCols]
    )

**Description**

Creates a new document using optional parameters and returns a reference to the new document.

**Parameters**

+--------------------------+--------------------------------------------------------------------------------------+-------------+
|        Parameter         |                                         Type                                         | Description |
+==========================+======================================================================================+=============+
| ``[documentColorSpace]`` | :ref:`jsobjref/documentColorSpace`, optional                                         | todo        |
+--------------------------+--------------------------------------------------------------------------------------+-------------+
| ``[width]``              | number (double), optional                                                            | todo        |
+--------------------------+--------------------------------------------------------------------------------------+-------------+
| ``[height]``             | number (double), optional                                                            | todo        |
+--------------------------+--------------------------------------------------------------------------------------+-------------+
| ``[numArtBoards]``       | number (long), optional                                                              | todo        |
+--------------------------+--------------------------------------------------------------------------------------+-------------+
| ``[artboardLayout]``     | :ref:`jsobjref/documentArtboardLayout`                                               | todo        |
+--------------------------+--------------------------------------------------------------------------------------+-------------+
| ``[artboardSpacing]``    | number (double), optional                                                            | todo        |
+--------------------------+--------------------------------------------------------------------------------------+-------------+
| ``[artboardRowsOrCols]`` | number (long), optional                                                              | todo        |
+--------------------------+--------------------------------------------------------------------------------------+-------------+

**Returns**

:ref:`jsobjref/document`

----

.. _jsobjref/documents.addDocument:

Documents.addDocument()
********************************************************************************

``app.documents.addDocument(startupPreset [, presetSettings] [, showOptionsDialog])``

**Description**

Creates a document from the preset, replacing any provided setting values, and returns a reference to the new document.

**Parameters**

+-------------------------+------------------------------------------+-------------+
|        Parameter        |                   Type                   | Description |
+=========================+==========================================+=============+
| ``startupPreset``       | String                                   | todo        |
+-------------------------+------------------------------------------+-------------+
| ``[presetSettings]``    | :ref:`jsobjref/documentPreset`, optional | todo        |
+-------------------------+------------------------------------------+-------------+
| ``[showOptionsDialog]`` | Boolean, optional                        | todo        |
+-------------------------+------------------------------------------+-------------+

**Returns**

:ref:`jsobjref/document`

----

.. _jsobjref/documents.addDocumentNoUI:

Documents.addDocumentNoUI()
********************************************************************************

``app.documents.addDocumentNoUI(startupPreset)``

**Description**

Creates a document without showing in UI.

**Parameters**

+-------------------+--------+-------------+
|     Parameter     |  Type  | Description |
+===================+========+=============+
| ``startupPreset`` | String | todo        |
+-------------------+--------+-------------+

**Returns**

:ref:`jsobjref/document`

----

.. _jsobjref/documents.getByName:

Documents.getByName()
********************************************************************************

``app.documents.getByName(name)``

**Description**

Gets the first element in the collection with the specified name.

**Parameters**

+-----------+--------+-------------+
| Parameter |  Type  | Description |
+===========+========+=============+
| ``name``  | String | todo        |
+-----------+--------+-------------+

**Returns**

:ref:`jsobjref/document`

----

.. _jsobjref/documents.index:

Documents.index()
********************************************************************************

``app.documents.index(itemKey)``

**Description**

Gets an element from the collection.

**Parameters**

+-------------+----------------+-------------+
|  Parameter  |      Type      | Description |
+=============+================+=============+
| ``itemKey`` | String, Number | todo        |
+-------------+----------------+-------------+

**Returns**

:ref:`jsobjref/document`

----

=======
Example
=======

Creating a new document
********************************************************************************

::

    // Creates a new document with an RGB color space

    app.documents.add( DocumentColorSpace.RGB );
