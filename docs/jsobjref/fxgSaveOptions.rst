.. _jsobjref/fxgSaveOptions:

FXG Save Options
################################################################################

``fxgSaveOptions``

**Description**

Specifies options which may be supplied when saving a document as an FXG file. All properties are optional.

----

==========
Properties
==========

.. _jsobjref/fxgSaveOptions.artboardRange:

fxgSaveOptions.artboardRange
********************************************************************************

``fxgSaveOptions.artboardRange``

**Description**

If saveMultipleArtboards is true, this is considered for multi-asset extraction, which specifies the artboard range. An empty string extracts all the artboards. Default: empty String.

**Type**

String.

----

.. _jsobjref/fxgSaveOptions.blendsPolicy:

fxgSaveOptions.blendsPolicy
********************************************************************************

``fxgSaveOptions.blendsPolicy``

**Description**

The policy used by FXG to expand blends. Default: ``BlendsExpandPolicy.AUTOMATICALLYCONVERTBLENDS``.

**Type**

:ref:`jsobjref/scriptingConstants.blendsExpandPolicy`

----

.. _jsobjref/fxgSaveOptions.downsampleLinkedImages:

fxgSaveOptions.downsampleLinkedImages
********************************************************************************

``fxgSaveOptions.downsampleLinkedImages``

**Description**

If ``true``, linked images are downsampled (at 72 dpi). Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/fxgSaveOptions.filtersPolicy:

fxgSaveOptions.filtersPolicy
********************************************************************************

``fxgSaveOptions.filtersPolicy``

**Description**

The policy used by FXG to preserve filters. Default: ``FiltersPreservePolicy.KEEPFILTERSEDITABLE``.

**Type**

:ref:`jsobjref/scriptingConstants.filtersPreservePolicy`

----

.. _jsobjref/fxgSaveOptions.gradientsPolicy:

fxgSaveOptions.gradientsPolicy
********************************************************************************

``fxgSaveOptions.gradientsPolicy``

**Description**

The policy used by FXG to preserve gradients. Default: ``GradientsPreservePolicy.AUTOMATICALLYCONVERTGRADIENTS``.

**Type**

:ref:`jsobjref/scriptingConstants.gradientsPreservePolicy`

----

.. _jsobjref/fxgSaveOptions.includeUnusedSymbols:

fxgSaveOptions.includeUnusedSymbols
********************************************************************************

``fxgSaveOptions.includeUnusedSymbols``

**Description**

If ``true``, unused symbols are included. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/fxgSaveOptions.preserveEditingCapabilities:

fxgSaveOptions.preserveEditingCapabilities
********************************************************************************

``fxgSaveOptions.preserveEditingCapabilities``

**Description**

If ``true``, the editing capabilities of FXG are preserved. Default: ``true``.

**Type**

Boolean.

----

.. _jsobjref/fxgSaveOptions.saveMultipleArtboards:

fxgSaveOptions.saveMultipleArtboards
********************************************************************************

``fxgSaveOptions.saveMultipleArtboards``

**Description**

If ``true``, all artboards or range of artboards are saved. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/fxgSaveOptions.textPolicy:

fxgSaveOptions.textPolicy
********************************************************************************

``fxgSaveOptions.textPolicy``

**Description**

The policy used by FXG to preserve text. Default: ``TextPreservePolicy.AUTOMATICALLYCONVERTTEXT``.

**Type**

:ref:`jsobjref/scriptingConstants.textPreservePolicy`

----

.. _jsobjref/fxgSaveOptions.version:

fxgSaveOptions.version
********************************************************************************

``fxgSaveOptions.version``

**Description**

The version of the FXG file format to create. Default ``FXGVersion.VERSION2PT0``.

**Type**

:ref:`jsobjref/scriptingConstants.fxgVersion`
