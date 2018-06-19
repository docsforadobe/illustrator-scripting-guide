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

.. _artboard.artboardRect:

artboard.artboardRect
********************************************************************************

``artboard.artboardRect``

**Description**

Size and position of the artboard.

**Type**

Rect

----

.. _artboard.name:

artboard.name
********************************************************************************

``artboard.name``

**Description**

The unique identifying name of the artboard.

**Type**

String

----

.. _artboard.parent:

artboard.parent
********************************************************************************

``artboard.parent``

**Description**

The parent of this object.

**Type**

`Document <#document>`__; read-only.

----

.. _artboard.rulerOrigin:

artboard.rulerOrigin
********************************************************************************

``artboard.rulerOrigin``

**Description**

Ruler origin of the artboard, relative to the top left corner of the artboard.

**Type**

Point

----

.. _artboard.rulerPAR:

artboard.rulerPAR
********************************************************************************

``artboard.rulerPAR``

**Description**

Pixel aspect ratio, used in ruler visualization if the units are pixels.

Range: 0.1 to 10.

**Type**

Number (double)

----

.. _artboard.showCenter:

artboard.showCenter
********************************************************************************

``artboard.showCenter``

**Description**

Show center mark.

**Type**

Boolean

----

.. _artboard.showCrossHairs:

artboard.showCrossHairs
********************************************************************************

``artboard.showCrossHairs``

**Description**

Show cross hairs.

**Type**

Boolean

----

.. _artboard.showSafeAreas:

artboard.showSafeAreas
********************************************************************************

``artboard.showSafeAreas``

**Description**

Show title and action safe areas (for video).

**Type**

Boolean

----

.. _artboard.typename:

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

.. _artboard.remove:

artboard.remove()
********************************************************************************

``artboard.remove()``

**Description**

Deletes this artboard object. You cannot remove the last artboard in a document.

**Returns**

Nothing.
