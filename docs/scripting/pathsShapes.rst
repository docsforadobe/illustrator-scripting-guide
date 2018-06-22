.. _scripting/pathsShapes:

Paths and shapes
################################################################################

Paths are represented in the Illustrator DOM by the ``path item`` object. Path items include all artwork that contains paths, such as rectangles, ellipses, and polygons, as well as freeform paths.

A freeform path consists of a series of path points. A path point can be specified in two ways:

- As an array of x and y page coordinates.
- As a ``path point`` object, which defines an anchor point and two direction points or handles that define the path segment’s curve:

.. image:: ../_static/pathPointObject.jpg
   :alt: Path Point Object

For details, samples, and information on creating shapes, see the chapter for your scripting language.
