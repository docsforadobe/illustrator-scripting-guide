.. _jsobjref/Tag:

Tag
################################################################################

``app.activeDocument.selection[index].tags[index``

**Description**

A label associated with a specific piece of artwork.

Tags allows you to assign an unlimited number of key-value pairs to any page item in a document.

----

==========
Properties
==========

.. _jsobjref/Tag.name:

Tag.name
********************************************************************************

``app.activeDocument.selection[index].tags[index].name``

**Description**

The tag's name.

**Type**

String, read-only.

----

.. _jsobjref/Tag.parent:

Tag.parent
********************************************************************************

``app.activeDocument.selection[index].tags[index].parent``

**Description**

The object that contains this tag.

**Type**

Object, read-only.

.. _jsobjref/Tag.typename:

Tag.typename
********************************************************************************

``app.activeDocument.selection[index].tags[index].typename``

**Description**

The class name of the object.

**Type**

String, read-only.

----

.. _jsobjref/Tag.value:

Tag.value
********************************************************************************

``app.activeDocument.selection[index].tags[index].value``

**Description**

The data stored in this tag.

**Type**

String, read-only.

----

=======
Methods
=======

.. _jsobjref/Tag.remove:

Tag.remove()
********************************************************************************

``app.activeDocument.selection[index].tags[index].remove()``

**Description**

Deletes this object.

**Returns**

Nothing.

=======
Example
=======

Using tags
********************************************************************************

::

  // Finds the tags associated with the selected art item,
  // show names and values in a separate document

  if ( app.documents.length > 0 ) {
    doc = app.activeDocument;

    if ( doc.selection.length > 0 ) {
      for ( i = 0; i < selection.length; i++ ) {
        selectedArt = selection[0];
        tagList = selectedArt.tags;

        if (tagList.length == 0) {
          var tempTag = tagList.add();
          tempTag.name = "OneWord";
          tempTag.value = "anything you want";
        }

        // Create a document and add a line of text per tag
        reportDocument = app.documents.add();
        top_offset = 400;

        for ( i = 0; i < tagList.length; i++ ) {
          tagText = tagList[i].value;
          newItem = reportDocument.textFrames.add();
          newItem.contents = "Tag: (" + tagList[i].name + " , " + tagText + ")";
          newItem.position = Array(100, top_offset);
          newItem.textRange.size = 24;
          top_offset = top_offset - 20;
        }
      }
    }
  }
