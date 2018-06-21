.. _jsobjref/exportOptionsAutoCAD:

Export Options AutoCAD
################################################################################

``exportOptionsAutoCAD``

**Description**

Options for exporting a document as an AutoCAD file, used with the :ref:`jsobjref/document.exportFile` method.
All properties are optional.

When you export a document, a file extension is appended automatically. You should not include any file extension in the file specification.

To override the default AutoCAD export format (DWG), use the :ref:`jsobjref/exportOptionsAutoCAD.exportFileFormat` property.

----

==========
Properties
==========

.. _jsobjref/exportOptionsAutoCAD.alterPathsForAppearance:

exportOptionsAutoCAD.alterPathsForAppearance
********************************************************************************

``exportOptionsAutoCAD.alterPathsForAppearance``

**Description**

If ``true``, paths are altered if needed to maintain appearance.

Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/exportOptionsAutoCAD.colors:

exportOptionsAutoCAD.colors
********************************************************************************

``exportOptionsAutoCAD.colors``

**Description**

The colors exported into the AutoCAD file.

**Type**

:ref:`jsobjref/scriptingConstants.autoCADColors`

----

.. _jsobjref/exportOptionsAutoCAD.convertTextToOutlines:

exportOptionsAutoCAD.convertTextToOutlines
********************************************************************************

``exportOptionsAutoCAD.convertTextToOutlines``

**Description**

If ``true``, text is converted to vector paths; preserves the visual appearance of type.

Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/exportOptionsAutoCAD.exportFileFormat:

exportOptionsAutoCAD.exportFileFormat
********************************************************************************

``exportOptionsAutoCAD.exportFileFormat``

**Description**

The format to which the file is exported.

Default: ``AutoCADExportFileFormat.DWG``.

**Type**

:ref:`jsobjref/scriptingConstants.autoCADExportFileFormat`

----

.. _jsobjref/exportOptionsAutoCAD.exportOption:

exportOptionsAutoCAD.exportOption
********************************************************************************

``exportOptionsAutoCAD.exportOption``

**Description**

Specifies whether to preserve appearance or editability during export.

Default: ``AutoCADExportOption.MaximizeEditability``.

**Type**

:ref:`jsobjref/scriptingConstants.autoCADExportOption`

----

.. _jsobjref/exportOptionsAutoCAD.exportSelectedArtOnly:

exportOptionsAutoCAD.exportSelectedArtOnly
********************************************************************************

``exportOptionsAutoCAD.exportSelectedArtOnly``

**Description**

If ``true``, only selected artwork is exported.

Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/exportOptionsAutoCAD.rasterFormat:

exportOptionsAutoCAD.rasterFormat
********************************************************************************

``exportOptionsAutoCAD.rasterFormat``

**Description**

The format in which raster art is exported.

**Type**

:ref:`jsobjref/scriptingConstants.autoCADRasterFormat`

----

.. _jsobjref/exportOptionsAutoCAD.scaleLineweights:

exportOptionsAutoCAD.scaleLineweights
********************************************************************************

``exportOptionsAutoCAD.scaleLineweights``

**Description**

If ``true``, line weights are scaled by the same scaling factor as the rest of the drawing.

Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/exportOptionsAutoCAD.typename:

exportOptionsAutoCAD.typename
********************************************************************************

``exportOptionsAutoCAD.typename``

**Description**

The class name of the referenced object.

**Type**

String, read-only.

----

.. _jsobjref/exportOptionsAutoCAD.unit:

exportOptionsAutoCAD.unit
********************************************************************************

``exportOptionsAutoCAD.unit``

**Description**

The measurement units from which to map.

**Type**

:ref:`jsobjref/scriptingConstants.autoCADUnit`

----

.. _jsobjref/exportOptionsAutoCAD.unitScaleRatio:

exportOptionsAutoCAD.unitScaleRatio
********************************************************************************

``exportOptionsAutoCAD.unitScaleRatio``

**Description**

The ratio (as a percentage) by which output is scaled.

Range: 0 to 1000

**Type**

Number (double).

----

.. _jsobjref/exportOptionsAutoCAD.version:

exportOptionsAutoCAD.version
********************************************************************************

``exportOptionsAutoCAD.version``

**Description**

The release of AutoCAD to which the file is exported.

Default: ``AutoCADCompatibility.AutoCADRelease24``.

**Type**

:ref:`jsobjref/scriptingConstants.autoCADCompatibility`
