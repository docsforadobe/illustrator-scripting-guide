# FXGSaveOptions

`fxgSaveOptions`

#### Description

Specifies options which may be supplied when saving a document as an FXG file. All properties are optional.

---

## Properties

### FXGSaveOptions.artboardRange

`fxgSaveOptions.artboardRange`

#### Description

If [`saveMultipleArtboards`](#fxgsaveoptionssavemultipleartboards) is true, this is considered for multi-asset extraction, which specifies the artboard range. An empty string extracts all the artboards.

Default: empty String.

#### Type

String.

---

### FXGSaveOptions.blendsPolicy

`fxgSaveOptions.blendsPolicy`

#### Description

The policy used by FXG to expand blends.

Default: `BlendsExpandPolicy.AUTOMATICALLYCONVERTBLENDS`.

#### Type

[BlendsExpandPolicy](scripting-constants.md#blendsexpandpolicy)

---

### FXGSaveOptions.downsampleLinkedImages

`fxgSaveOptions.downsampleLinkedImages`

#### Description

If `true`, linked images are downsampled (at 72 dpi).

Default: `false`.

#### Type

Boolean.

---

### FXGSaveOptions.filtersPolicy

`fxgSaveOptions.filtersPolicy`

#### Description

The policy used by FXG to preserve filters.

Default: `FiltersPreservePolicy.KEEPFILTERSEDITABLE`.

#### Type

[FiltersPreservePolicy](scripting-constants.md#filterspreservepolicy)

---

### FXGSaveOptions.gradientsPolicy

`fxgSaveOptions.gradientsPolicy`

#### Description

The policy used by FXG to preserve gradients.

Default: `GradientsPreservePolicy.AUTOMATICALLYCONVERTGRADIENTS`.

#### Type

[GradientsPreservePolicy](scripting-constants.md#gradientspreservepolicy)

---

### FXGSaveOptions.includeUnusedSymbols

`fxgSaveOptions.includeUnusedSymbols`

#### Description

If `true`, unused symbols are included.

Default: `false`.

#### Type

Boolean.

---

### FXGSaveOptions.preserveEditingCapabilities

`fxgSaveOptions.preserveEditingCapabilities`

#### Description

If `true`, the editing capabilities of FXG are preserved.

Default: `true`.

#### Type

Boolean.

---

### FXGSaveOptions.saveMultipleArtboards

`fxgSaveOptions.saveMultipleArtboards`

#### Description

If `true`, all artboards or range of artboards are saved.

Default: `false`.

#### Type

Boolean.

---

### FXGSaveOptions.textPolicy

`fxgSaveOptions.textPolicy`

#### Description

The policy used by FXG to preserve text.

Default: `TextPreservePolicy.AUTOMATICALLYCONVERTTEXT`.

#### Type

[TextPreservePolicy](scripting-constants.md#textpreservepolicy)

---

### FXGSaveOptions.version

`fxgSaveOptions.version`

#### Description

The version of the FXG file format to create. Default `FXGVersion.VERSION2PT0`.

#### Type

[FXGVersion](scripting-constants.md#fxgversion)
