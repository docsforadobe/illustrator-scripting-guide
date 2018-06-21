.. _scripting/workingWithObjects:

Working with objects
################################################################################

Getting the frontmost document or layer
================================================================================

To refer to the selected document, use the ``application`` object’s ``current document`` property in
AppleScript or the ``active document`` property in JavaScript or VBScript. Similarly, you can use the
``document`` object’s ``current layer`` or ``active layer`` property to refer to the selected layer.

There are other types of "active" or "current" object properties, like ``active dataset`` or ``active view``. For
details, see the Adobe lllustrator CC 2017 Scripting Reference for your language.

----

Creating new objects
================================================================================

Several objects (besides the ``application`` object itself) cannot be obtained from containers or parent
objects. Your script must create these objects directly.

The following objects must be created explicitly:

- ``CMYK color``
- ``document preset``
- ``EPS save options``
- ``export options AutoCAD``
- ``export options Flash``
- ``export options GIF``
- ``export options JPEG``
- ``export options Photoshop``
- ``export options PNG8``
- ``export options PNG24``
- ``export options SVG``
- ``export options TIFF``
- ``file``
- ``folder``
- ``gradient color``
- ``gray color``
- ``Illustrator save options``
- ``ink``
- ``ink info``
- ``lab color``
- ``matrix``
- ``MXG save options``
- ``no color``
- ``open options``
- ``open options AutoCAD``
- ``open options FreeHand``
- ``open options PDF``
- ``open options Photoshop``
- ``paper info``
- ``Pattern color``
- ``PDF save options``
- ``PPD file``
- ``PPD file info``
- ``print color management options``
- ``print color separation options``
- ``print coordinate options``
- ``printer``
- ``printer info``
- ``print flattener options``
- ``print font options``
- ``print job options``
- ``print options``
- ``print page marks options``
- ``print paper options``
- ``print postscript options``
- ``raster effect options``
- ``rasterize options``
- ``screen``
- ``screen spot function``
- ``RGB color``
- ``spot color``
- ``tracing options``

The ``file`` and ``folder`` objects are Adobe ExtendScript devices designed to provide platform-independent
access to the underlying file system. For information on using these objects, see `JavaScript Tools Guide <http://estk.aenhancers.com>`__

For information on creating an object explicitly, see the chapter for your scripting language.

----

Collection objects
================================================================================

Most collection objects must be obtained from a container. For example, a ``path items`` collection object
can be contained by a ``document`` object or a ``layer`` object; to obtain an object in a ``path items`` collection,
refer to either containing of these objects. For example, see the language-specific sections below.

AppleScript
********************************************************************************

To refer to a ``path items`` object in a document::

  path item 1 in document 1

To refer to a ``path items`` object in a layer::

  path item 1 in layer 1 in document 1

JavaScript
********************************************************************************

To refer to a ``path items`` object in a document::

  documents[0].pathItems[1]

To refer to a ``path items`` object in a layer::

  documents[0].layers[0].pathItems[0]


VBScript
********************************************************************************

To refer to a ``path items`` object in a document::

  Documents(1).PathItems(1)

To refer to a ``path items`` object in a layer::

  Documents(1).Layers(1).PathItems(1)

For more examples of collection-item containers, see the document object Elements table in Adobe
lllustrator CC 2017 Scripting Reference: AppleScript or the Properties table in Adobe lllustrator CC 2017
Scripting Reference: JavaScript or Adobe lllustrator CC 2017 Scripting Reference: VBScript. A diagram of the
lllustrator CC 2017 object model is in :ref:`objectmodel/objectModel`.

----

Selected objects
================================================================================

Sometimes, you want to write scripts that act on the currently selected object or objects. For example, you
might want to apply formatting to selected text or change a selected path’s shape.

Selecting Text
********************************************************************************

To select text, use the ``select`` command or method of the ``text range`` object.

Selecting art items
********************************************************************************

You can select an art object (like graph items, mesh items, raster items, and symbol items) by setting its
selected property to true. (In AppleScript, ``selected`` is a property of the ``page items`` object.)


Referring to selected art items
********************************************************************************

To refer to all currently selected objects in a document, use the ``document`` object’s ``selection`` property. To
work with the objects in the selection array, you must determine their type, so you will know which
properties and methods or commands you can use with them. In JavaScript and VBScript, each artwork
object type has a read-only ``typename`` property that you can use to determine the object’s type. In
AppleScript, use the ``class`` property.

----

Notes on renaming objects stored in the application’s panels
================================================================================

Several objects can be renamed; that is, their ``name`` property is writeable. The following types of objects can
be sorted alphabetically in the corresponding Illustrator panel. If a script modifies the name of such an
object, references to that object by index can become invalid.

- ``Brush``
- ``Gradient``
- ``Graphic Style``
- ``Pattern``
- ``Swatch``
- ``Symbol``
- ``Variable``

