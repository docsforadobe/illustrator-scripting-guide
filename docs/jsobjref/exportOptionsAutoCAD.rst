.. _jsobjref/exportOptionsAutoCAD:

Export Options AutoCAD
################################################################################

``exportOptionsAutoCAD``

**Description**

Options for exporting a document as an AutoCAD file, used with the `exportFile <document.html#document-exportfile>`__ method. All properties are optional.

When you export a document, a file extension is appended automatically. You should not include any file extension in the file specification. To override the default AutoCAD export format (DWG), use the `exportFileFormat <#exportoptionsautocad-exportfileformat>`__ property.

----

==========
Properties
==========

.. _exportOptionsAutoCAD.alterPathsForAppearance:

exportOptionsAutoCAD.alterPathsForAppearance
********************************************************************************

``exportOptionsAutoCAD.alterPathsForAppearance``

**Description**

If ``true``, paths are altered if needed to maintain appearance. Default: ``false``.

**Type**

Boolean.

----

.. _exportOptionsAutoCAD.colors:

exportOptionsAutoCAD.colors
********************************************************************************

``exportOptionsAutoCAD.colors``

**Description**

The colors exported into the AutoCAD file.

**Type**

// todo: link to **AutoCADColors** in Chapter 2 "Scripting Constants"

----

.. _exportOptionsAutoCAD.convertTextToOutlines:

exportOptionsAutoCAD.convertTextToOutlines
********************************************************************************

``exportOptionsAutoCAD.convertTextToOutlines``

**Description**

If ``true``, text is converted to vector paths; preserves the visual appearance of type. Default: ``false``.

**Type**

Boolean.

----

.. _exportOptionsAutoCAD.exportFileFormat:

exportOptionsAutoCAD.exportFileFormat
********************************************************************************

``exportOptionsAutoCAD.exportFileFormat``

**Description**

The format to which the file is exported. Default: ``AutoCADExportFileFormat.DWG``.

**Type**

// todo: link to **AutoCADExportFileFormat** in Chapter 2 "Scripting Constants"

----

.. _exportOptionsAutoCAD.exportOption:

exportOptionsAutoCAD.exportOption
********************************************************************************

``exportOptionsAutoCAD.exportOption``

**Description**

Specifies whether to preserve appearance or editability during export. Default: ``AutoCADExportOption.MaximizeEditability``.

**Type**

// todo: link to **AutoCADExportOption** in Chapter 2 "Scripting Constants"

----

.. _exportOptionsAutoCAD.exportSelectedArtOnly:

exportOptionsAutoCAD.exportSelectedArtOnly
********************************************************************************

``exportOptionsAutoCAD.exportSelectedArtOnly``

**Description**

If ``true``, only selected artwork is exported. Default: ``false``.

**Type**

Boolean.

----

.. _exportOptionsAutoCAD.rasterFormat:

exportOptionsAutoCAD.rasterFormat
********************************************************************************

``exportOptionsAutoCAD.rasterFormat``

**Description**

The format in which raster art is exported.

**Type**

// todo: link to **AutoCADRasterFormat** in Chapter 2 "Scripting Constants"

----

.. _exportOptionsAutoCAD.scaleLineweights:

exportOptionsAutoCAD.scaleLineweights
********************************************************************************

``exportOptionsAutoCAD.scaleLineweights``

**Description**

If ``true``, line weights are scaled by the same scaling factor as the rest of the drawing. Default: ``false``.

**Type**

Boolean.

----

.. _exportOptionsAutoCAD.typename:

exportOptionsAutoCAD.typename
********************************************************************************

``exportOptionsAutoCAD.typename``

**Description**

The class name of the referenced object.

**Type**

String, read-only.

----

.. _exportOptionsAutoCAD.unit:

exportOptionsAutoCAD.unit
********************************************************************************

``exportOptionsAutoCAD.unit``

**Description**

The measurement units from which to map.

**Type**

// todo: link to **AutoCADUnit** in Chapter 2 "Scripting Constants"

----

.. _exportOptionsAutoCAD.unitScaleRatio:

exportOptionsAutoCAD.unitScaleRatio
********************************************************************************

``exportOptionsAutoCAD.unitScaleRatio``

**Description**

The ratio (as a percentage) by which output is scaled. Range: 0 to 1000

**Type**

Number (double).

----

.. _exportOptionsAutoCAD.version:

exportOptionsAutoCAD.version
********************************************************************************

``exportOptionsAutoCAD.version``

**Description**

The release of AutoCAD to which the file is exported. Default: ``AutoCADCompatibility.AutoCADRelease24``.

**Type**

// todo: link to **AutoCADCompatibility** in Chapter 2 "Scripting Constants"

----