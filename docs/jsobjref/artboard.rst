.. _jsobjref/artboard:

Artboard
################################################################################

``artboard``

**Description**

An Artboard object represents a single artboard in a document. There can be between 1 to 100 artboards
in one document.

==========
Properties
==========

.. _jsobjref/artboard.artboardRect:

artboard.artboardRect
********************************************************************************

``artboard.artboardRect``

**Description**

Size and position of the artboard.

**Type**

Rect

----

.. _jsobjref/artboard.name:

artboard.name
********************************************************************************

``artboard.name``

**Description**

The unique identifying name of the artboard.

**Type**

String

----

.. _jsobjref/artboard.parent:

artboard.parent
********************************************************************************

``artboard.parent``

**Description**

The parent of this object.

**Type**

:ref:`jsobjref/document`; read-only.

----

.. _jsobjref/artboard.rulerOrigin:

artboard.rulerOrigin
********************************************************************************

``artboard.rulerOrigin``

**Description**

Ruler origin of the artboard, relative to the top left corner of the artboard.

**Type**

Point

----

.. _jsobjref/artboard.rulerPAR:

artboard.rulerPAR
********************************************************************************

``artboard.rulerPAR``

**Description**

Pixel aspect ratio, used in ruler visualization if the units are pixels.

Range: 0.1 to 10.

**Type**

Number (double)

----

.. _jsobjref/artboard.showCenter:

artboard.showCenter
********************************************************************************

``artboard.showCenter``

**Description**

Show center mark.

**Type**

Boolean

----

.. _jsobjref/artboard.showCrossHairs:

artboard.showCrossHairs
********************************************************************************

``artboard.showCrossHairs``

**Description**

Show cross hairs.

**Type**

Boolean

----

.. _jsobjref/artboard.showSafeAreas:

artboard.showSafeAreas
********************************************************************************

``artboard.showSafeAreas``

**Description**

Show title and action safe areas (for video).

**Type**

Boolean

----

.. _jsobjref/artboard.typename:

artboard.typename
********************************************************************************

``artboard.typename``

**Description**

Read-only. The class name of this object.

**Type**

String

----

==========
Methods
==========

.. _jsobjref/artboard.remove:

artboard.remove()
********************************************************************************

``artboard.remove()``

**Description**

Deletes this artboard object. You cannot remove the last artboard in a document.

**Returns**

Nothing.
