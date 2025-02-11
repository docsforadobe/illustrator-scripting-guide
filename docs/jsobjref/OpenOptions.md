.. _jsobjref/OpenOptions:

OpenOptions
################################################################################

``openOptions``

**Description**

Options for opening a document, used with the :ref:`jsobjref/Application.open` method.

----

==========
Properties
==========

.. _jsobjref/OpenOptions.convertCropAreaToArboard:

OpenOptions.convertCropAreaToArboard
********************************************************************************

``openOptions.convertCropAreaToArboard``

**Description**

Optional. Convert crop areas to artboards when opening a legacy document in Illustrator CS4 or later. When ``false``, crop areas are discarded. Default: ``true``.

**Type**

Boolean.

----

.. _jsobjref/OpenOptions.convertTilesToArboard:

OpenOptions.convertTilesToArboard
********************************************************************************

``openOptions.convertTilesToArboard``

**Description**

Optional. Convert print tiles to artboards when opening a legacy document in Illustrator CS4 or later. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/OpenOptions.createArtboardWithArtworkBoundingBox:

OpenOptions.createArtboardWithArtworkBoundingBox
********************************************************************************

``openOptions.createArtboardWithArtworkBoundingBox``

**Description**

Optional. Create an artboard with the dimensions of the bounding box of the artwork when opening a legacy document in Illustrator CS4 or later. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/OpenOptions.openAs:

OpenOptions.openAs
********************************************************************************

``openOptions.openAs``

**Description**

Optional. Open the file as an Illustrator library of this type. Default: ``LibraryType.IllustratorArtwork``.

**Type**

:ref:`jsobjref/scripting-constants.LibraryType`

----

.. _jsobjref/OpenOptions.preserveLegacyArtboard:

OpenOptions.preserveLegacyArtboard
********************************************************************************

``openOptions.preserveLegacyArtboard``

**Description**

Optional. Preserve legacy artboards when opening a legacy document in Illustrator CS4 or later. Default: ``true``.

**Type**

Boolean.

----

.. _jsobjref/OpenOptions.updateLegacyGradientMesh:

OpenOptions.updateLegacyGradientMesh
********************************************************************************

``openOptions.updateLegacyGradientMesh``

**Description**

If ``true``, preserves the spot colors in the gradient mesh objects for legacy documents (pre-Illustrator CS4). Default: ``true``.

**Type**

Boolean.

----

.. _jsobjref/OpenOptions.updateLegacyText:

OpenOptions.updateLegacyText
********************************************************************************

``openOptions.updateLegacyText``

**Description**

Optional. If ``true``, update all legacy text items (from previous versions of Illustrator). Default: ``false``.

**Type**

Boolean.

----

=======
Example
=======

Automatically updating legacy text on open
********************************************************************************

::

  // Opens a file with legacy text (AI 10 or older), using
  // OpenOptions to automatically update the legacy text.

  var fileRef = filePath;
  if (fileRef != null) {
    var openOptions = new OpenOptions();
    openOptions.updateLegacyText = true;

    var docRef = open(fileRef, DocumentColorSpace.RGB, openOptions);
  }
