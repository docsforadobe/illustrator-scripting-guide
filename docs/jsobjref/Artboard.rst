.. _jsobjref/Artboard:

Artboard
################################################################################

``artboard``

**Description**

An Artboard object represents a single artboard in a document. There can be between 1 to 100 artboards in one document.

==========
Properties
==========

.. _jsobjref/Artboard.artboardRect:

Artboard.artboardRect
********************************************************************************

``artboard.artboardRect``

**Description**

Size and position of the artboard.

**Type**

Rect

----

.. _jsobjref/Artboard.name:

Artboard.name
********************************************************************************

``artboard.name``

**Description**

The unique identifying name of the artboard.

**Type**

String

----

.. _jsobjref/Artboard.parent:

Artboard.parent
********************************************************************************

``artboard.parent``

**Description**

The parent of this object.

**Type**

:ref:`jsobjref/Document`; read-only.

----

.. _jsobjref/Artboard.rulerOrigin:

Artboard.rulerOrigin
********************************************************************************

``artboard.rulerOrigin``

**Description**

Ruler origin of the artboard, relative to the top left corner of the artboard.

**Type**

Point

----

.. _jsobjref/Artboard.rulerPAR:

Artboard.rulerPAR
********************************************************************************

``artboard.rulerPAR``

**Description**

Pixel aspect ratio, used in ruler visualization if the units are pixels.

Range: 0.1 to 10.

**Type**

Number (double)

----

.. _jsobjref/Artboard.showCenter:

Artboard.showCenter
********************************************************************************

``artboard.showCenter``

**Description**

Show center mark.

**Type**

Boolean

----

.. _jsobjref/Artboard.showCrossHairs:

Artboard.showCrossHairs
********************************************************************************

``artboard.showCrossHairs``

**Description**

Show cross hairs.

**Type**

Boolean

----

.. _jsobjref/Artboard.showSafeAreas:

Artboard.showSafeAreas
********************************************************************************

``artboard.showSafeAreas``

**Description**

Show title and action safe areas (for video).

**Type**

Boolean

----

.. _jsobjref/Artboard.typename:

Artboard.typename
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

.. _jsobjref/Artboard.remove:

Artboard.remove()
********************************************************************************

``artboard.remove()``

**Description**

Deletes this artboard object. You cannot remove the last artboard in a document.

**Returns**

Nothing.
