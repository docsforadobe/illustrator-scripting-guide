.. _jsobjref/OpenOptionsAutoCAD:

OpenOptionsAutoCAD
################################################################################

``openOptionsAutoCAD``

**Description**

Options for opening an AutoCAD drawing, used with the :ref:`jsobjref/Application.open` method.

----

==========
Properties
==========

.. _jsobjref/OpenOptionsAutoCAD.centerArtwork:

OpenOptionsAutoCAD.centerArtwork
********************************************************************************

``openOptionsAutoCAD.centerArtwork``

**Description**

If ``true``, the artwork is centered on the artboard. Default: ``true``.

**Type**

Boolean.

----

.. _jsobjref/OpenOptionsAutoCAD.globalScaleOption:

OpenOptionsAutoCAD.globalScaleOption
********************************************************************************

``openOptionsAutoCAD.globalScaleOption``

**Description**

How to scale the drawing on import. Default: ``AutoCADGlobalScaleOption.FitArtboard``.

**Type**

:ref:`jsobjref/scripting-constants.AutoCADGlobalScaleOption`

----

.. _jsobjref/OpenOptionsAutoCAD.globalScalePercent:

OpenOptionsAutoCAD.globalScalePercent
********************************************************************************

``openOptionsAutoCAD.globalScalePercent``

**Description**

The value when ``globalScaleOption`` is ``AutoCADGlobalScaleOption.ScaleByValue``, expressed as a percentage. Range: 0.0 to 100.0. Default is 100.0.

**Type**

Number (double).

----

.. _jsobjref/OpenOptionsAutoCAD.mergeLayers:

OpenOptionsAutoCAD.mergeLayers
********************************************************************************

``openOptionsAutoCAD.mergeLayers``

**Description**

If ``true``, the layers of the artwork are merged. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/OpenOptionsAutoCAD.parent:

OpenOptionsAutoCAD.parent
********************************************************************************

``openOptionsAutoCAD.parent``

**Description**

The object’s container.

**Type**

Object, read-only.

----

.. _jsobjref/OpenOptionsAutoCAD.scaleLineweights:

OpenOptionsAutoCAD.scaleLineweights
********************************************************************************

``openOptionsAutoCAD.scaleLineweights``

**Description**

If ``true``, line weights are scaled by the same factor as the rest of the drawing. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/OpenOptionsAutoCAD.selectedLayoutName:

OpenOptionsAutoCAD.selectedLayoutName
********************************************************************************

``openOptionsAutoCAD.selectedLayoutName``

**Description**

The name of the layout in the drawing to import.

**Type**

String.

----

.. _jsobjref/OpenOptionsAutoCAD.typename:

OpenOptionsAutoCAD.typename
********************************************************************************

``openOptionsAutoCAD.typename``

**Description**

The class name of the object.

**Type**

String, read-only.

----

.. _jsobjref/OpenOptionsAutoCAD.unit:

OpenOptionsAutoCAD.unit
********************************************************************************

``openOptionsAutoCAD.unit``

**Description**

The unit to map to. Default: ``AutoCADUnit.Millimeters``.

**Type**

:ref:`jsobjref/scripting-constants.AutoCADUnit`

----

.. _jsobjref/OpenOptionsAutoCAD.unitScaleRatio:

OpenOptionsAutoCAD.unitScaleRatio
********************************************************************************

``openOptionsAutoCAD.unitScaleRatio``

**Description**

The ratio by which to scale while mapping units. Default: 1.0.

**Type**

Number (double).
