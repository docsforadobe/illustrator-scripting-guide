.. _jsobjref/TracingObject:

TracingObject
################################################################################

``TracingObject``

**Description**

A tracing object, which associates source raster art item with a vector-art plug-in group created by tracing. Scripts can initiate tracing using :ref:`jsobjref/PlacedItem.trace` or :ref:`jsobjref/RasterItem.trace`.

The resulting PluginItem object represents the vector art group, and has this object in its tracing property.

A script can force the tracing operation by calling :ref:`jsobjref/Application.redraw`. The operation is asynchronous, so a script should call ``redraw`` after creating the tracing object, but before accessing its properties or expanding the tracing to convert it to an art item group.

The read-only properties that describe the tracing result have valid values only after the first tracing operation completes. A value of 0 indicates that the operation has not yet been completed.

----

==========
Properties
==========

.. _jsobjref/TracingObject.anchorCount:

TracingObject.anchorCount
********************************************************************************

``tracingObject.anchorCount``

**Description**

The number of anchors in the tracing result.

**Type**

Number (long); read-only.

----

.. _jsobjref/TracingObject.areaCount:

TracingObject.areaCount
********************************************************************************

``tracingObject.areaCount``

**Description**

The number of areas in the tracing result.

**Type**

Number (long); read-only.

----

.. _jsobjref/TracingObject.imageResolution:

TracingObject.imageResolution
********************************************************************************

``tracingObject.imageResolution``

**Description**

The resolution of the source image in pixels per inch.

**Type**

Number (real); read-only.

----

.. _jsobjref/TracingObject.parent:

TracingObject.parent
********************************************************************************

``tracingObject.parent``

**Description**

The object’s container.

**Type**

Object; read-only.

----

.. _jsobjref/TracingObject.pathCount:

TracingObject.pathCount
********************************************************************************

``tracingObject.pathCount``

**Description**

The number of paths in the tracing result.

**Type**

Number (long); read-only.

----

.. _jsobjref/TracingObject.sourceArt:

TracingObject.sourceArt
********************************************************************************

``tracingObject.sourceArt``

**Description**

The raster art used to create the associated vector art plug-in group.

**Type**

:ref:`jsobjref/PlacedItem` or :ref:`jsobjref/RasterItem`

----

.. _jsobjref/TracingObject.tracingOptions:

TracingObject.tracingOptions
********************************************************************************

``tracingObject.tracingOptions``

**Description**

The options used to convert the raster artwork to vector art.

**Type**

:ref:`jsobjref/TracingOptions`

----

.. _jsobjref/TracingObject.typename:

TracingObject.typename
********************************************************************************

``tracingObject.typename``

**Description**

The class name of the object.

**Type**

String; read-only.

----

.. _jsobjref/TracingObject.usedColorCount:

TracingObject.usedColorCount
********************************************************************************

``tracingObject.usedColorCount``

**Description**

The number of colors used in the tracing result.

**Type**

Number (long); read-only.

----

=======
Methods
=======

.. _jsobjref/TracingObject.expandTracing:

TracingObject.expandTracing()
********************************************************************************

``tracingObject.expandTracing([viewed])``

**Description**

Converts the vector art into a new group item. The new GroupItem object replaces the PluginItem object in the document.

By default, ``viewed`` is ``false``, and the new group contains only the tracing result (the filled or stroked paths).

If ``viewed`` is ``true``, the new group retains additional information that was specified for the viewing mode, such as outlines and overlays.

Deletes this object and its associated :ref:`jsobjref/PluginItem` object. Any group-level attributes that were applied to the plug-in item are applied to the top level of the new group item.

**Parameters**

+------------+-------------------+-------------+
| Parameter  |       Type        | Description |
+============+===================+=============+
| ``viewed`` | Boolean, optional | todo        |
+------------+-------------------+-------------+

**Returns**

:ref:`jsobjref/GroupItem`

----

.. _jsobjref/TracingObject.releaseTracing:

TracingObject.releaseTracing()
********************************************************************************

``tracingObject.releaseTracing()``

**Description**

Reverts the artwork in the document to the original source raster art and removes the traced vector art. Returns the original object used to create the tracing, and deletes this object and its associated PluginItem object.

**Parameters**

**Returns**

:ref:`jsobjref/PlacedItem` or :ref:`jsobjref/RasterItem`
