.. _jsobjref/TextFrameItems:

TextFrameItems
################################################################################

``app.activeDocument.textFrames``

**Description**

The collection of :ref:`jsobjref/TextFrameItem` objects in the document.

----

==========
Properties
==========

.. _jsobjref/TextFrameItems.length:

TextFrameItems.length
********************************************************************************

``app.activeDocument.textFrames.length``

**Description**

The number of elements in the collection.

**Type**

Number; read-only.

----

.. _jsobjref/TextFrameItems.parent:

TextFrameItems.parent
********************************************************************************

``app.activeDocument.textFrames.parent``

**Description**

The object's container.

**Type**

Object; read-only.

----

.. _jsobjref/TextFrameItems.typename:

TextFrameItems.typename
********************************************************************************

``app.activeDocument.textFrames.typename``

**Description**

The class name of the referenced object.

**Type**

String; read-only.

----

=======
Methods
=======

.. _jsobjref/TextFrameItems.add:

TextFrameItems.add()
********************************************************************************

``app.activeDocument.textFrames.add()``

**Description**

Creates a point text frame item.

**Returns**

:ref:`jsobjref/TextFrameItem`

----

.. _jsobjref/TextFrameItems.areaText:

TextFrameItems.areaText()
********************************************************************************

``app.activeDocument.textFrames.areaText(textPath[, orientation][, baseFrame][, postFix])``

**Description**

Creates an area text frame item.

**Parameters**

+-----------------+---------------------------------------------------------------+---------------------------------------------+
|    Parameter    |                             Type                              |                 Description                 |
+=================+===============================================================+=============================================+
| ``textPath``    | :ref:`jsobjref/PathItem`                                      | Path item to use                            |
+-----------------+---------------------------------------------------------------+---------------------------------------------+
| ``orientation`` | :ref:`jsobjref/scripting-constants.TextOrientation`, optional | Orientation of text                         |
+-----------------+---------------------------------------------------------------+---------------------------------------------+
| ``baseFrame``   | :ref:`jsobjref/TextFrameItem`, optional                       | Text frame to use                           |
+-----------------+---------------------------------------------------------------+---------------------------------------------+
| ``postFix``     | Boolean, optional                                             | Whether to prefix or postfix the text frame |
+-----------------+---------------------------------------------------------------+---------------------------------------------+

**Returns**

:ref:`jsobjref/TextFrameItem`

----

.. _jsobjref/TextFrameItems.getByName:

TextFrameItems.getByName()
********************************************************************************

``app.activeDocument.textFrames.getByName(name)``

**Description**

Get the first element in the collection with the provided name.

**Parameters**

+-----------+--------+------------------------+
| Parameter |  Type  |      Description       |
+===========+========+========================+
| ``name``  | String | Name of element to get |
+-----------+--------+------------------------+

**Returns**

:ref:`jsobjref/TextFrameItem`

----

.. _jsobjref/TextFrameItems.index:

TextFrameItems.index()
********************************************************************************

``app.activeDocument.textFrames.index(itemKey)``

**Description**

Gets an element from the collection.

**Parameters**

+-------------+----------------+----------------------+
|  Parameter  |      Type      |     Description      |
+=============+================+======================+
| ``itemKey`` | String, Number | String or number key |
+-------------+----------------+----------------------+

**Returns**

:ref:`jsobjref/TextFrameItem`

----

.. _jsobjref/TextFrameItems.pathText:

TextFrameItems.pathText()
********************************************************************************

``app.activeDocument.textFrames.pathText(textPath[,startTValue][,endTValue][, orientation][, baseFrame][, postFix])``

**Description**

Creates an on-path text frame item.

**Parameters**

+-----------------+---------------------------------------------------------------+---------------------------------------------+
|    Parameter    |                             Type                              |                 Description                 |
+=================+===============================================================+=============================================+
| ``textPath``    | :ref:`jsobjref/PathItem`                                      | Path item to use                            |
+-----------------+---------------------------------------------------------------+---------------------------------------------+
| ``startTValue`` | Number (double)                                               | Start position of text along the path       |
+-----------------+---------------------------------------------------------------+---------------------------------------------+
| ``endTValue``   | Number (double)                                               | End position of text along the path         |
+-----------------+---------------------------------------------------------------+---------------------------------------------+
| ``orientation`` | :ref:`jsobjref/scripting-constants.TextOrientation`, optional | Orientation of text                         |
+-----------------+---------------------------------------------------------------+---------------------------------------------+
| ``baseFrame``   | :ref:`jsobjref/TextFrameItem`, optional                       | Text frame to use                           |
+-----------------+---------------------------------------------------------------+---------------------------------------------+
| ``postFix``     | Boolean, optional                                             | Whether to prefix or postfix the text frame |
+-----------------+---------------------------------------------------------------+---------------------------------------------+

**Returns**

:ref:`jsobjref/TextFrameItem`

----

.. _jsobjref/TextFrameItems.pointText:

TextFrameItems.pointText()
********************************************************************************

``app.activeDocument.textFrames.pointText(anchor[, orientation])``

**Description**

Creates a point text frame item.

**Parameters**

+-----------------+---------------------------------------------------------------+---------------------+
|    Parameter    |                             Type                              |     Description     |
+=================+===============================================================+=====================+
| ``anchor``      | Array of 2 numbers                                            | Point text anchor   |
+-----------------+---------------------------------------------------------------+---------------------+
| ``orientation`` | :ref:`jsobjref/scripting-constants.TextOrientation`, optional | Orientation of text |
+-----------------+---------------------------------------------------------------+---------------------+

**Returns**

:ref:`jsobjref/TextFrameItem`

----

.. _jsobjref/TextFrameItems.removeAll:

TextFrameItems.removeAll()
********************************************************************************

``app.activeDocument.textFrames.removeAll()``

**Description**

Deletes all elements in this collection.

**Returns**

Nothing.

----

=======
Example
=======

Creating and modifying text frames
********************************************************************************

::

   // Creates a document with text frames displaying path, area and point
   // text, changes the content of each frame then deletes the 2nd frame

   // create a new document
   var docRef = documents.add();

   // create 3 new textFrames (area, line, point)
   // Area Text
   var rectRef = docRef.pathItems.rectangle(700, 50, 100, 100); var areaTextRef = docRef.textFrames.areaText(rectRef); areaTextRef.contents = "TextFrame #1";
   areaTextRef.selected = true;

   // Line Text
   var lineRef = docRef.pathItems.add();
   lineRef.setEntirePath( Array(Array(200, 700), Array(300, 550) ) ); var pathTextRef = docRef.textFrames.pathText(lineRef); pathTextRef.contents = "TextFrame #2";
   pathTextRef.selected = true;

   // Point Text
   var pointTextRef = docRef.textFrames.add(); pointTextRef.contents = "TextFrame #3"; pointTextRef.top = 700;
   pointTextRef.left = 400; pointTextRef.selected = true; redraw();

   // count the TextFrames
   var iCount = docRef.textFrames.length;
   var sText = "There are " + iCount + " TextFrames.\r" sText += "Changing contents of each TextFrame.";

   // change the content of each docRef.textFrames[0].contents = "Area TextFrame."; docRef.textFrames[1].contents = "Path TextFrame."; docRef.textFrames[2].contents = "Point TextFrame."; redraw();
   docRef.textFrames[1].remove(); redraw();

   // count again

   var iCount = docRef.textFrames.length;
