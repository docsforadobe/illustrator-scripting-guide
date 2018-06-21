.. _objectmodel/theArtworkTree:

The Artwork Tree
################################################################################

The content of an Illustrator document is called the artwork tree.
Artwork is represented by the following objects:

- ``compound path item``
- ``graph item``
- ``group item``
- ``legacy text item``
- ``mesh item``
- ``non native item``
- ``path item``
- ``placed item``
- ``plugin item``
- ``raster item``
- ``symbol item`` (see :ref:`objectmodel/dynamic`)
- ``text frame``

Your scripts can access and manipulate art objects through collections in the
document and layer objects.

There are two types of art-object collections:

- Collection objects that correspond to each individual artwork object type, such as the ``graph items`` object or the ``mesh items`` object.
- The ``page items`` object, which includes art objects of all types.

Also, you can use the group ``item`` object to reference a grouped set of art items.

You can create new art objects using the ``make`` command (AppleScript) or add method of an artwork item
collection object. For example, to create a new ``path item`` object:

===========  ============================================================
AppleScript  ``set myPathItem to make new path item in current document``
JavaScript   ``var myPathItem = activeDocument.pathItems.add();``
VBScript     ``Set myPathItem = appRef.ActiveDocument.PathItems.Add()``
===========  ============================================================

The following artwork collections do not allow the creation of new objects using the ``make`` command or
add method:

- ``graph items`` object
- ``mesh items`` object
- ``plugin items`` object
- ``legacy text items`` object

For details on creating objects of these types, see the Adobe lllustrator CC
Scripting Reference for your language.

----

Art styles
================================================================================

Your script can apply a graphic style to artwork using the ``graphic style``
object. To apply a graphic style, use the ``graphic styles`` property of the
``document`` object to access the ``apply to`` method of the ``graphic style``
object.

Similarly, the ``brush`` object allows you to specify the brush to apply to
artwork. You access any brush through the ``brushes`` collection object, which
is a property of the ``document`` object.

----

Color objects
================================================================================

Your script can apply a color, pattern or gradient to a ``path item`` object,
using the ``fill color`` or ``stroke color`` properties:

- Scripts can define new color swatches using the ``make`` command or add method of the ``swatches`` object. Your script also can create a new spot color, using the ``make`` command or ``add`` property of the ``spots`` object.
- You can define the attributes of an ink object using the ``ink info`` object, which is an ``ink`` object property. You access ``ink`` objects through the ``ink list`` property of the ``document`` object.

The following objects allow you to create colors within defined color spaces:

- The ``RGB color`` object, using the range 0.0 to 255.0 for the each of the three individual color values.
- The ``CMYK color`` object, using the percentage values 0.0 through 100.0 for each of the four individual color values.
- The ``grayscale color`` or ``LAB color`` objects, using the same range and number of values that you use in the Illustrator application.
