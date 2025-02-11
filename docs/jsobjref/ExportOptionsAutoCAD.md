.. _jsobjref/ExportOptionsAutoCAD:

ExportOptionsAutoCAD
################################################################################

``exportOptionsAutoCAD``

**Description**

Options for exporting a document as an AutoCAD file, used with the :ref:`jsobjref/Document.exportFile` method.
All properties are optional.

When you export a document, a file extension is appended automatically. You should not include any file extension in the file specification.

To override the default AutoCAD export format (DWG), use the :ref:`jsobjref/ExportOptionsAutoCAD.exportFileFormat` property.

----

==========
Properties
==========

.. _jsobjref/ExportOptionsAutoCAD.alterPathsForAppearance:

ExportOptionsAutoCAD.alterPathsForAppearance
********************************************************************************

``exportOptionsAutoCAD.alterPathsForAppearance``

**Description**

If ``true``, paths are altered if needed to maintain appearance.

Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/ExportOptionsAutoCAD.colors:

ExportOptionsAutoCAD.colors
********************************************************************************

``exportOptionsAutoCAD.colors``

**Description**

The colors exported into the AutoCAD file.

**Type**

:ref:`jsobjref/scripting-constants.AutoCADColors`

----

.. _jsobjref/ExportOptionsAutoCAD.convertTextToOutlines:

ExportOptionsAutoCAD.convertTextToOutlines
********************************************************************************

``exportOptionsAutoCAD.convertTextToOutlines``

**Description**

If ``true``, text is converted to vector paths; preserves the visual appearance of type.

Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/ExportOptionsAutoCAD.exportFileFormat:

ExportOptionsAutoCAD.exportFileFormat
********************************************************************************

``exportOptionsAutoCAD.exportFileFormat``

**Description**

The format to which the file is exported.

Default: ``AutoCADExportFileFormat.DWG``.

**Type**

:ref:`jsobjref/scripting-constants.AutoCADExportFileFormat`

----

.. _jsobjref/ExportOptionsAutoCAD.exportOption:

ExportOptionsAutoCAD.exportOption
********************************************************************************

``exportOptionsAutoCAD.exportOption``

**Description**

Specifies whether to preserve appearance or editability during export.

Default: ``AutoCADExportOption.MaximizeEditability``.

**Type**

:ref:`jsobjref/scripting-constants.AutoCADExportOption`

----

.. _jsobjref/ExportOptionsAutoCAD.exportSelectedArtOnly:

ExportOptionsAutoCAD.exportSelectedArtOnly
********************************************************************************

``exportOptionsAutoCAD.exportSelectedArtOnly``

**Description**

If ``true``, only selected artwork is exported.

Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/ExportOptionsAutoCAD.rasterFormat:

ExportOptionsAutoCAD.rasterFormat
********************************************************************************

``exportOptionsAutoCAD.rasterFormat``

**Description**

The format in which raster art is exported.

**Type**

:ref:`jsobjref/scripting-constants.AutoCADRasterFormat`

----

.. _jsobjref/ExportOptionsAutoCAD.scaleLineweights:

ExportOptionsAutoCAD.scaleLineweights
********************************************************************************

``exportOptionsAutoCAD.scaleLineweights``

**Description**

If ``true``, line weights are scaled by the same scaling factor as the rest of the drawing.

Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/ExportOptionsAutoCAD.typename:

ExportOptionsAutoCAD.typename
********************************************************************************

``exportOptionsAutoCAD.typename``

**Description**

The class name of the referenced object.

**Type**

String, read-only.

----

.. _jsobjref/ExportOptionsAutoCAD.unit:

ExportOptionsAutoCAD.unit
********************************************************************************

``exportOptionsAutoCAD.unit``

**Description**

The measurement units from which to map.

**Type**

:ref:`jsobjref/scripting-constants.AutoCADUnit`

----

.. _jsobjref/ExportOptionsAutoCAD.unitScaleRatio:

ExportOptionsAutoCAD.unitScaleRatio
********************************************************************************

``exportOptionsAutoCAD.unitScaleRatio``

**Description**

The ratio (as a percentage) by which output is scaled.

Range: 0 to 1000

**Type**

Number (double).

----

.. _jsobjref/ExportOptionsAutoCAD.version:

ExportOptionsAutoCAD.version
********************************************************************************

``exportOptionsAutoCAD.version``

**Description**

The release of AutoCAD to which the file is exported.

Default: ``AutoCADCompatibility.AutoCADRelease24``.

**Type**

:ref:`jsobjref/scripting-constants.AutoCADCompatibility`
