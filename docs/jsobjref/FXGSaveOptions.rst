.. _jsobjref/FXGSaveOptions:

FXGSaveOptions
################################################################################

``fxgSaveOptions``

**Description**

Specifies options which may be supplied when saving a document as an FXG file. All properties are optional.

----

==========
Properties
==========

.. _jsobjref/FXGSaveOptions.artboardRange:

FXGSaveOptions.artboardRange
********************************************************************************

``fxgSaveOptions.artboardRange``

**Description**

If saveMultipleArtboards is true, this is considered for multi-asset extraction, which specifies the artboard range. An empty string extracts all the artboards. Default: empty String.

**Type**

String.

----

.. _jsobjref/FXGSaveOptions.blendsPolicy:

FXGSaveOptions.blendsPolicy
********************************************************************************

``fxgSaveOptions.blendsPolicy``

**Description**

The policy used by FXG to expand blends. Default: ``BlendsExpandPolicy.AUTOMATICALLYCONVERTBLENDS``.

**Type**

:ref:`jsobjref/scripting-constants.BlendsExpandPolicy`

----

.. _jsobjref/FXGSaveOptions.downsampleLinkedImages:

FXGSaveOptions.downsampleLinkedImages
********************************************************************************

``fxgSaveOptions.downsampleLinkedImages``

**Description**

If ``true``, linked images are downsampled (at 72 dpi). Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/FXGSaveOptions.filtersPolicy:

FXGSaveOptions.filtersPolicy
********************************************************************************

``fxgSaveOptions.filtersPolicy``

**Description**

The policy used by FXG to preserve filters. Default: ``FiltersPreservePolicy.KEEPFILTERSEDITABLE``.

**Type**

:ref:`jsobjref/scripting-constants.FiltersPreservePolicy`

----

.. _jsobjref/FXGSaveOptions.gradientsPolicy:

FXGSaveOptions.gradientsPolicy
********************************************************************************

``fxgSaveOptions.gradientsPolicy``

**Description**

The policy used by FXG to preserve gradients. Default: ``GradientsPreservePolicy.AUTOMATICALLYCONVERTGRADIENTS``.

**Type**

:ref:`jsobjref/scripting-constants.GradientsPreservePolicy`

----

.. _jsobjref/FXGSaveOptions.includeUnusedSymbols:

FXGSaveOptions.includeUnusedSymbols
********************************************************************************

``fxgSaveOptions.includeUnusedSymbols``

**Description**

If ``true``, unused symbols are included. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/FXGSaveOptions.preserveEditingCapabilities:

FXGSaveOptions.preserveEditingCapabilities
********************************************************************************

``fxgSaveOptions.preserveEditingCapabilities``

**Description**

If ``true``, the editing capabilities of FXG are preserved. Default: ``true``.

**Type**

Boolean.

----

.. _jsobjref/FXGSaveOptions.saveMultipleArtboards:

FXGSaveOptions.saveMultipleArtboards
********************************************************************************

``fxgSaveOptions.saveMultipleArtboards``

**Description**

If ``true``, all artboards or range of artboards are saved. Default: ``false``.

**Type**

Boolean.

----

.. _jsobjref/FXGSaveOptions.textPolicy:

FXGSaveOptions.textPolicy
********************************************************************************

``fxgSaveOptions.textPolicy``

**Description**

The policy used by FXG to preserve text. Default: ``TextPreservePolicy.AUTOMATICALLYCONVERTTEXT``.

**Type**

:ref:`jsobjref/scripting-constants.TextPreservePolicy`

----

.. _jsobjref/FXGSaveOptions.version:

FXGSaveOptions.version
********************************************************************************

``fxgSaveOptions.version``

**Description**

The version of the FXG file format to create. Default ``FXGVersion.VERSION2PT0``.

**Type**

:ref:`jsobjref/scripting-constants.FXGVersion`
