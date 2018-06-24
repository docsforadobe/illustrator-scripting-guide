.. _jsobjref/NoColor:

NoColor
################################################################################

``noColor``

**Description**

Represents the “none” color. Assigning a ``NoColor`` object to the fill or stroke color of an art item is equivalent to setting the ``filled`` or ``stroked`` property to ``false``.

----

==========
Properties
==========

.. _jsobjref/NoColor.typename:

NoColor.typename
********************************************************************************

``noColor.typename``

**Description**

The class name of the object.

**Type**

String, read-only.

----

=======
Example
=======

Using NoColor to remove a fill color
********************************************************************************

::

  // Creates 2 overlapping objects with different fill colors.
  // Assign the top object a fill color of "NoColor"
  // allowing the bottom object to become visible.

  // Create 2 overlapping objects one blue, one red;
  var docRef = documents.add();
  var itemRef1 = docRef.pathItems.rectangle(500, 200, 200, 100);
  var itemRef2 = docRef.pathItems.rectangle(550, 150, 200, 200);
  var rgbColor = new RGBColor();
  rgbColor.red = 255;
  itemRef2.fillColor = rgbColor;

  rgbColor.blue = 255;
  rgbColor.red = 0;
  itemRef1.fillColor = rgbColor;
  redraw();

  // create a nocolor and assign it to the top object
  var noColor = new NoColor();
  itemRef2.fillColor = noColor;
  redraw();
