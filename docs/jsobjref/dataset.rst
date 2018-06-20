.. _jsobjref/dataset:

Dataset
################################################################################

``dataset``

**Description**

A set of data used for dynamic publishing. A dataset allows you to collect a number of variables and their dynamic data into one object. You must have at least one variable bound to an art item in order to create a dataset. See the class :ref:`jsobjref/variable`.

----

==========
Properties
==========

.. _dataset.name:

dataset.name
********************************************************************************

``app.activeDocument.dataSets[index].name``

**Description**

Then name of the dataset.

**Type**

String.

----

.. _dataset.parent:

dataset.parent
********************************************************************************

``app.activeDocument.dataSets[index].parent``

**Description**

The name of the object that contains this dataset.

**Type**

:ref:`jsobjref/document`, read-only.

----

.. _dataset.typename:

dataset.typename
********************************************************************************

``app.activeDocument.dataSets[index].typename``

**Description**

The class name of the referenced object.

**Type**

String.

----

=======
Methods
=======

.. _dataset.display:

dataset.display()
********************************************************************************

``app.activeDocument.dataSets[index].display()``

**Description**

Displays the dataset.

**Returns**

Nothing.

----

.. _dataset.remove:

dataset.remove()
********************************************************************************

``app.activeDocument.dataSets[index].remove()``

**Description**

Deletes this object.

**Returns**

Nothing.

----

.. _dataset.update:

dataset.update()
********************************************************************************

``app.activeDocument.dataSets[index].update()``

**Description**

Updates the dataset.

**Returns**

Nothing.

----

=======
Example
=======

Using variables and datasets
********************************************************************************

::

    // Creates two variables, 1 visibility and 1 text,
    // creates two datasets each with different values for the variables,
    // then displays both datasets
    
    var docRef = documents.add();

    // Create visibility variable
    var itemRef = docRef.pathItems.rectangle(600, 200, 150, 150);
    var colorRef = new RGBColor;
    colorRef.red = 255;
    itemRef.fillColor = colorRef;
    var visibilityVar = docRef.variables.add();
    visibilityVar.kind = VariableKind.VISIBILITY;
    itemRef.visibilityVariable = visibilityVar;

    // Create text variable
    var textRef = docRef.textFrames.add();
    textRef.contents = "Text Variable, dataset 1";
    textRef.top = 400;
    textRef.left = 200;
    var textVar = docRef.variables.add();
    textVar.kind = VariableKind.TEXTUAL;
    textRef.contentVariable = textVar;
    redraw();

    // Create dataset 1
    var ds1 = docRef.dataSets.add();

    // Change variable values and create dataset 2
    itemRef.hidden = true;
    textRef.contents = "Text Variable, dataset 2";
    redraw();
    var ds2 = docRef.dataSets.add();

    // display each dataset
    ds1.display();
    redraw();
    ds2.display();
    redraw();