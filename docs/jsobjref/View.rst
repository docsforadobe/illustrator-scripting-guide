.. _jsobjref/View:

View
################################################################################

``app.activeDocument.views[index]``

**Description**

A document view in an Illustrator document, which represents a window view onto a document.

Scripts cannot create new views, but can modify some properties of existing views, including the center point, screen mode, and zoom.

----

==========
Properties
==========

.. _jsobjref/View.bounds:

View.bounds
********************************************************************************

``app.activeDocument.views[index].bounds``

**Description**

Read-only. The bounding rectangle of this view relative to the current document’s bounds.

**Type**

Array of 4 Numbers

----

.. _jsobjref/View.centerPoint:

View.centerPoint
********************************************************************************

``app.activeDocument.views[index].centerPoint``

**Description**

The center point of this view relative to the current document’s bounds.

**Type**

Array of 2 Numbers

----

.. _jsobjref/View.parent:

View.parent
********************************************************************************

``app.activeDocument.views[index].parent``

**Description**

Read-only. The document that contains this view.

**Type**

:ref:`jsobjref/Document`

----

.. _jsobjref/View.screenMode:

View.screenMode
********************************************************************************

``app.activeDocument.views[index].screenMode``

**Description**

The mode of display for this view.

**Type**

:ref:`jsobjref/scripting-constants.ScreenMode`


----
.. _jsobjref/View.typename:

View.typename
********************************************************************************

``app.activeDocument.views[index].typename``

**Description**

Read-only. The class name of the referenced object.

**Type**

String

----

.. _jsobjref/View.zoom:

View.zoom
********************************************************************************

``app.activeDocument.views[index].zoom``

**Description**

The zoom factor of this view, where 100.0 is 100%.

**Type**

Number (double)
