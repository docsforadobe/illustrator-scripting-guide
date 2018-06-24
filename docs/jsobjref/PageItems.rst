.. _jsobjref/PageItems:

PageItems
################################################################################

``app.activeDocument.pageItems``

**Description**

A collection of page item objects. Provides complete access to all the art items in an Illustrator document in the following classes:

.. toctree::
  :maxdepth: 2

  CompoundPathItem
  GraphItem
  GroupItem
  LegacyTextItem
  MeshItem
  NonNativeItem
  PathItem
  PlacedItem
  PluginItem
  RasterItem
  SymbolItem
  TextFrameItem

You can reference page items through the :ref:`jsobjref/PageItems` property in a :ref:`jsobjref/Document`, :ref:`jsobjref/Layer`, or :ref:`jsobjref/Group`. When you access an individual item in one of these collections, the reference is a page item of one of a particular type. For example, if you use :ref:`jsobjref/PageItems` to reference a graph item, the typename value of that object is :ref:`jsobjref/GraphItem`.

----

==========
Properties
==========

.. _jsobjref/PageItems.length:

PageItems.length
********************************************************************************

``app.activeDocument.pageItems.length``

**Description**

The number of objects in the collection.

**Type**

Number, read-only.

----

.. _jsobjref/PageItems.parent:

PageItems.parent
********************************************************************************

``app.activeDocument.pageItems.parent``

**Description**

The parent of this object.

**Type**

Object, read-only.

----

.. _jsobjref/PageItems.typename:

PageItems.typename
********************************************************************************

``app.activeDocument.pageItems.typename``

**Description**

The class name of the referenced object.

**Type**

String, read-only.

----

=======
Methods
=======

.. _jsobjref/PageItems.getByName:

PageItems.getByName()
********************************************************************************

``app.activeDocument.pageItems.getByName(name)``

**Description**

Gets the first element in the collection with the specified name.

**Parameters**

+-----------+--------+-------------+
| Parameter |  Type  | Description |
+===========+========+=============+
| ``name``  | String | todo        |
+-----------+--------+-------------+

**Returns**

:ref:`jsobjref/PageItem`

----

.. _jsobjref/PageItems.index:

PageItems.index()
********************************************************************************

``app.activeDocument.pageItems.index(itemKey)``

**Description**

Gets an element from the collection.

**Parameters**

+-------------+----------------+-------------+
|  Parameter  |      Type      | Description |
+=============+================+=============+
| ``itemKey`` | String, Number | todo        |
+-------------+----------------+-------------+

**Returns**

:ref:`jsobjref/PageItem`

----

.. _jsobjref/PageItems.removeAll:

PageItems.removeAll()
********************************************************************************

``app.activeDocument.pageItems.removeAll()``

**Description**

Deletes all elements in this collection.

**Returns**

Nothing.

----

=======
Example
=======

Getting references to external files in page items
********************************************************************************

::

  // Gets all file-references in the current document using the pageItems object,
  // then displays them in a new document

  if (app.documents.length > 0) {
    var fileReferences = new Array();
    var sourceDoc = app.activeDocument;

    for (var i = 0; i < sourceDoc.pageItems.length; i++) {
      var artItem = sourceDoc.pageItems[i];
      switch (artItem.typename) {
        case "PlacedItem":
          fileReferences.push(artItem.file.fsName);
          break;
        case "RasterItem":
          if (!artItem.embedded) {
            fileReferences.push(artItem.file.fsName);
          }
          break;
      }
    }

    // Write the file references to a new document
    var reportDoc = documents.add();
    var areaTextPath = reportDoc.pathItems.rectangle(reportDoc.height, 0, reportDoc.width, reportDoc.height);
    var fileNameText = reportDoc.textFrames.areaText(areaTextPath);
    fileNameText.textRange.size = 24;
    var paragraphCount = 3;
    var sourceName = sourceDoc.name;
    var text = "File references in \'" + sourceName + "\':\r\r";
    for (i = 0; i < fileReferences.length; i++) {
      text += (fileReferences[i] + "\r");
      paragraphCount++;
    }
    fileNameText.contents = text;
  }
