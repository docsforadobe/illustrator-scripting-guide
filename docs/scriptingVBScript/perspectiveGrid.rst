.. _perspectiveGrid:

Working with the perspective grid
################################################################################

The Perspective Grid is a new feature in lllustrator CC 2017 that enables you to create and manipulate art in
a spatial environment using established laws of perspective. Enable Perspective Grid using the View >
Perspective Grid menu or the perspective tools in the toolbar.

The SDK provides an API for working with the perspective grid programmatically, and your scripts have
some access to this API. A script can:

- Set a the default grid parameters using preset values.
- Show or hide the grid.
- Set the active plane.
- Draw an object in perspective on the active plane.
- Bring an object into perspective.

----

Use perspective presets
================================================================================

Illustrator provides default grid-parameter presets for one-point, two-point, and three-point perspectives.
The presets are named ``"[1P-NormalView]"``, ``"[2P-NormalView]"``, and ``"[3P-NormalView]"``.

The script shows how to select the two-point perspective preset programmatically::

  Set appRef = CreateObject ("Illustrator.Application")

  Rem Create a new document
  Set docRef = appRef.Documents.Add()

  Rem Select the default two-point perspective preset
  docRef.SelectPerspectivePreset("[2P-Normal View]")

You can create new perspective presets, export presets to files, and import presets from files. These scripts
shows how to export and import presets::

  Set appRef = CreateObject ("Illustrator.Application")
  Rem Create a new document
  Set docRef = appRef.Documents.Add()
  Rem Export perspective presets to a file
  docRef.ExportPerspectiveGridPreset("C:/scripting/PGPresetsExported")

  Set appRef = CreateObject ("Illustrator.Application")
  Rem Create a new document
  Set docRef = appRef.Documents.Add()
  Rem Import perspective presets from a file
  docRef.ImportPerspectiveGridPreset("C:/scripting/PGPresets")

----

Show or hide the grid
================================================================================

This script shows or hides the Perspective Grid programmatically::

  Set appRef = CreateObject ("Illustrator.Application")

  Rem Create a new document

  Set docRef = appRef.Documents.Add()

  Rem Show the Perspective Grid defined in the document
  docRef.ShowPerspectiveGrid();

  Rem Hide the Perspective Grid defined in the document
  docRef.HidePerspectiveGrid();

----

Set the active plane
================================================================================

The perspective grid plane types are:

=============  ====================
Left plane     ``aiLEFTPLANE (1)``
Right plane    ``aiRIGHTPLANE (2)``
Floor plane    ``aiFLOORPLANE (3)``
Invalid plane  ``aiNOPLANE (4)``
=============  ====================

For a one-point perspective grid, only the left and floor plane are valid.

This script sets the active perspective plane to the left plane::

  Set appRef = CreateObject ("Illustrator.Application")

  Rem Create a new document
  Set docRef = appRef.Documents.Add()

  Rem Set left plane as the active plane
  docRef.SetPerspectiveActivePlane(1) 'aiLEFTPLANE

----

Draw on a perspective grid
================================================================================

When the Perspective Grid is on, drawing methods allow you to draw or operate on objects in perspective.
This script creates a new document, shows a two-point perspective grid, and draws art objects on the left
plane::

  Set appRef = CreateObject ("Illustrator.Application")

  Rem Create a new document
  Set docRef = appRef.Documents.Add()

  Rem Select the default two point perspective preset
  docRef.SelectPerspectivePreset("[2P-Normal View]")

  Rem Display the perspective grid defined in the document
  docRef.ShowPerspectiveGrid()

  Rem Check if active plane is set to left, otherwise set it to left
  If docRef.GetPerspectiveActivePlane() <> 1 Then
    docRef.SetPerspectiveActivePlane(1) 'aiLEFTPLANE
  End If

  Rem Draw rectangle in perspective, then resize to 200% and move
  Set pathItemRect = docRef.PathItems.Rectangle(30, -30, 30, 30, False)

  call pathItemRect.Resize(200, 200, True, False, False, False, 100, 2)
  call pathItemRect.Translate(-420, 480)

  Rem Draw ellipse in perspective
  Set pathItemEllipse = docRef.PathItems.Ellipse(60, -60, 30, 30, False, True)

  Rem Draw rounded rectangle in perspective
  Set pathItemRRect = docRef.PathItems.RoundedRectangle(90, -90, 30, 30, 10, 10, False)

  Rem Draw polygon in perspective
  Set pathItemPoly = docRef.PathItems.Polygon(-105, 105, 15, 7, False)

  Rem Draw star in perspective
  Set pathItemStar = docRef.PathItems.Star(-135, 135, 15, 10, 6, False)

  Rem Draw path in perspective
  Set newPath = docRef.PathItems.Add()
  newPath.SetEntirePath(Array(Array(0,0),Array(60,0),Array(30,45),Array(90,110)))

----

Bring objects into perspective
================================================================================

If an art object is not in perspective, use the ``bringInPerspective()`` method to bring it into perspective
and place it on a plane.

This script creates a new document, draws an art object, and brings it into perspective on a three-point
perspective grid::

  Set appRef = CreateObject ("Illustrator.Application")

  Rem Create a new document
  Set docRef = appRef.Documents.Add()

  Rem Draw ellipse
  Set pathItemEllipse = docRef.PathItems.Ellipse(60, -60, 30, 30, False, True)

  Rem Draw polygon
  Set pathItemPoly = docRef.PathItems.Polygon(-105, 105, 15, 7, False)

  Rem Draw star
  Set pathItemStar = docRef.PathItems.Star(-135, 135, 15, 10, 6, False)

  Rem Select the default three-point perspective preset
  docRef.SelectPerspectivePreset("[3P-Normal View]")

  Rem Display the perspective grid defined in the document
  docRef.ShowPerspectiveGrid()

  Rem Check if active plane is set to left, otherwise set it to left
  If docRef.GetPerspectiveActivePlane() <> 1 Then
    docRef.SetPerspectiveActivePlane(1) 'aiLEFTPLANE
  End If

  Rem Bring the ellipse to the active plane (left plane)
  Call pathItemEllipse.BringInPerspective(100,100, 1) 'aiLEFTPLANE

  Rem Bring the polygon to the right plane
  Call pathItemPoly.BringInPerspective(100,-100,2) 'aiRIGHTPLANE

  Rem Bring the star to the floor plane
  Call pathItemStar.BringInPerspective(100,100,3) 'aiFLOORPLANE
