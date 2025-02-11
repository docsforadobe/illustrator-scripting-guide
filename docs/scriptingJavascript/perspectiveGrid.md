.. _scriptingJavascript/perspectiveGrid:

Working with the perspective grid
################################################################################

The Perspective Grid is a new feature in lllustrator CC 2017 that enables you to create and manipulate art in a spatial environment using established laws of perspective. Enable Perspective Grid using the View > Perspective Grid menu or the perspective tools in the toolbar.

The SDK provides an API for working with the perspective grid programmatically, and your scripts have some access to this API. A script can:

- Set a the default grid parameters using preset values.
- Show or hide the grid.
- Set the active plane.
- Draw an object in perspective on the active plane.
- Bring an object into perspective.

----

Use perspective presets
================================================================================

Illustrator provides default grid-parameter presets for one-point, two-point, and three-point perspectives. The presets are named ``"[1P-NormalView]"``, ``"[2P-NormalView]"``, and ``"[3P-NormalView]"``.

The script shows how to select the two-point perspective preset programmatically::

  //Set the default one-point perspective preset
  app.activeDocument.selectPerspectivePreset("[1P-Normal View]");

  //Set the default two-point perspective preset
  app.activeDocument.selectPerspectivePreset("[2P-Normal View]");

  //Set the default three-point perspective preset
  app.activeDocument.selectPerspectivePreset("[3P-Normal View]");

You can create new perspective presets, export presets to files, and import presets from files. These scripts shows how to export and import presets::

  //Create a new document
  var mydoc = app.documents.add();
  //Export perspective presets to a file
  var exportPresetFile = new File("C:/scripting/PGPresetsExported")
  mydoc.exportPerspectiveGridPreset(exportPresetFile);

  //Create a new document
  var mydoc = app.documents.add();
  //Import perspective presets from a file
  var importPresetFile = new File("C:/scripting/PGPresets")
  mydoc.importPerspectiveGridPreset(importPresetFile);

----

Show or hide the grid
================================================================================

This script shows or hides the Perspective Grid programmatically::

  //Show the Perspective Grid defined in the document
  app.activeDocument.showPerspectiveGrid();

  //Hide the Perspective Grid defined in the document
  mydoc.hidePerspectiveGrid();

----

Set the active plane
================================================================================

The perspective grid plane types are:

=============  =======================================
Left plane     ``PerspectiveGridPlaneType.LEFTPLANE``
Right plane    ``PerspectiveGridPlaneType.RIGHTPLANE``
Floor plane    ``PerspectiveGridPlaneType.FLOORPLANE``
Invalid plane  ``PerspectiveGridPlaneType.NOPLANE``
=============  =======================================

For a one-point perspective grid, only the left and floor plane are valid.

This script sets the active perspective plane::

  //Set left plane as the active plane
  app.activeDocument.setPerspectiveActivePlane(PerspectiveGridPlaneType.LEFTPLANE);

  //Set right plane as the active plane
  app.activeDocument.setPerspectiveActivePlane(PerspectiveGridPlaneType.RIGHTPLANE);

  //Set floor plane as the active plane
  app.activeDocument.setPerspectiveActivePlane(PerspectiveGridPlaneType.FLOORPLANE);

----

Draw on a perspective grid
================================================================================

When the Perspective Grid is on, drawing methods allow you to draw or operate on objects in perspective. This script creates a new document, shows a two-point perspective grid, and draws art objects on the left
plane

::

  //Create a new document
  var mydoc = app.documents.add();

  //Select the default two-point perspective preset
  mydoc.selectPerspectivePreset("[2P-Normal View]");

  //Display the perspective grid defined in the document
  mydoc.showPerspectiveGrid();

  //Check if active plane is set to left; if not, set it to left
  if (mydoc.getPerspectiveActivePlane() != PerspectiveGridPlaneType.LEFTPLANE) {
    mydoc.setPerspectiveActivePlane(PerspectiveGridPlaneType.LEFTPLANE);
  }

  //Draw rectangle in perspective, then resize to 200% and move
  var myrect = mydoc.pathItems.rectangle(30, -30, 30, 30, false);
  myrect.resize(200, 200, true, false, false, false, 100, Transformation.TOPLEFT);
  myrect.translate (-420, 480);

  //Draw ellipse in perspective
  var myellipse = mydoc.pathItems.ellipse(60, -60, 30, 30, false, true);

  //Draw rounded rectangle in perspective
  var myrrect = mydoc.pathItems.roundedRectangle(90, -90, 30, 30, 10, 10, false);

  //Draw polygon in perspective
  var mypoly = mydoc.pathItems.polygon(-105, 105, 15, 7, false);

  //Draw star in perspective
  var mystar = mydoc.pathItems.star(-135, 135, 15, 10, 6, false);

  //Draw path in perspective
  var newPath = mydoc.pathItems.add();
  var lineList = new Array(4);
  lineList[0] = new Array(0,0);
  lineList[1] = new Array(60,0);
  lineList[2] = new Array(30,45);
  lineList[3] = new Array(90,110);
  newPath.setEntirePath(lineList);

----

Bring objects into perspective
================================================================================

If an art object is not in perspective, use the ``bringInPerspective()`` method to bring it into perspective and place it on a plane.

This script creates a new document, draws an art object, and brings it into perspective on a three-point perspective grid::

  //Create a new document
  var mydoc = app.documents.add();

  //Draw ellipse
  var myellipse = mydoc.pathItems.ellipse(60, -60, 30, 30, false, true);

  //Draw polygon
  var mypoly = mydoc.pathItems.polygon(-105, 105, 15, 7, false);

  //Draw star
  var mystar = mydoc.pathItems.star(-135, 135, 15, 10, 6, false);

  //Select the default three-point perspective preset
  mydoc.selectPerspectivePreset("[3P-Normal View]");

  //Display the perspective grid defined in the document
  mydoc.showPerspectiveGrid();

  //Check if active plane is set to left; if not, set it to left
  if (mydoc.getPerspectiveActivePlane() != PerspectiveGridPlaneType.LEFTPLANE) {
    mydoc.setPerspectiveActivePlane(PerspectiveGridPlaneType.LEFTPLANE);
  }

  //Bring the ellipse to the active plane (left plane)
  myellipse.bringInPerspective(-100,-100, PerspectiveGridPlaneType.LEFTPLANE);

  //Bring the polygon to the right plane
  mypoly.bringInPerspective(100,-100,PerspectiveGridPlaneType.RIGHTPLANE);

  //Bring the star to the floor plane
  mystar.bringInPerspective(100,100,PerspectiveGridPlaneType.FLOORPLANE);
