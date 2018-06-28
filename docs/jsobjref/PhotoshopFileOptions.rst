.. _jsobjref/PhotoshopFileOptions:

PhotoshopFileOptions
################################################################################

``preferences.photoshopFileOptions``

**Description**

Options for opening a Photoshop file, used with the :ref:`jsobjref/Application.open` method. All properties are optional.

----

==========
Properties
==========

.. _jsobjref/PhotoshopFileOptions.parent:

PhotoshopFileOptions.parent
********************************************************************************

``preferences.photoshopFileOptions.parent``

**Description**

The parent of this object.

**Type**

Object; read-only.

----

.. _jsobjref/PhotoshopFileOptions.pixelAspectRatioCorrection:

PhotoshopFileOptions.pixelAspectRatioCorrection
********************************************************************************

``preferences.photoshopFileOptions.pixelAspectRatioCorrection``

**Description**

If ``true``, imported images that have a non-square pixel aspect ratio should be adjusted.

**Type**

Boolean

----

.. _jsobjref/PhotoshopFileOptions.preserveImageMaps:

PhotoshopFileOptions.preserveImageMaps
********************************************************************************

``preferences.photoshopFileOptions.preserveImageMaps``

**Description**

If ``true``, image maps should be preserved when document is converted.

Default: ``true``

**Type**

Boolean

----

.. _jsobjref/PhotoshopFileOptions.preserveLayers:

PhotoshopFileOptions.preserveLayers
********************************************************************************

``preferences.photoshopFileOptions.preserveLayers``

**Description**

If ``true``, layers should be preserved when document is converted.

Default: ``true``

**Type**

Boolean

----

.. _jsobjref/PhotoshopFileOptions.preserveSlices:

PhotoshopFileOptions.preserveSlices
********************************************************************************

``preferences.photoshopFileOptions.preserveSlices``

**Description**

If ``true``, slices should be preserved when document is converted.

Default: ``true``

**Type**

Boolean

----

.. _jsobjref/PhotoshopFileOptions.typename:

PhotoshopFileOptions.typename
********************************************************************************

``preferences.photoshopFileOptions.typename``

**Description**

The class name of the referenced object.

**Type**

String; read-only.

----

==========
Example
==========

Opening a Photoshop file
********************************************************************************

::

  // Opens a Photoshop file containing layers with
  // preferences set to preserve layers
  var psdOptions = preferences.photoshopFileOptions;
  psdOptions.preserveLayers = true;
  psdOptions.pixelAspectRatioCorrection = false;

  // open a file using these prefs
  var fileRef = File(psdFilePath);
  if (fileRef != null) {
    var docRef = open(fileRef, DocumentColorSpace.RGB);
  }
