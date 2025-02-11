<a id="jsobjref-openoptions"></a>

# OpenOptions

`openOptions`

**Description**

Options for opening a document, used with the [Application.open()](Application.md#jsobjref-application-open) method.

---

## Properties

<a id="jsobjref-openoptions-convertcropareatoarboard"></a>

### OpenOptions.convertCropAreaToArboard

`openOptions.convertCropAreaToArboard`

**Description**

Optional. Convert crop areas to artboards when opening a legacy document in Illustrator CS4 or later. When `false`, crop areas are discarded. Default: `true`.

**Type**

Boolean.

---

<a id="jsobjref-openoptions-converttilestoarboard"></a>

### OpenOptions.convertTilesToArboard

`openOptions.convertTilesToArboard`

**Description**

Optional. Convert print tiles to artboards when opening a legacy document in Illustrator CS4 or later. Default: `false`.

**Type**

Boolean.

---

<a id="jsobjref-openoptions-createartboardwithartworkboundingbox"></a>

### OpenOptions.createArtboardWithArtworkBoundingBox

`openOptions.createArtboardWithArtworkBoundingBox`

**Description**

Optional. Create an artboard with the dimensions of the bounding box of the artwork when opening a legacy document in Illustrator CS4 or later. Default: `false`.

**Type**

Boolean.

---

<a id="jsobjref-openoptions-openas"></a>

### OpenOptions.openAs

`openOptions.openAs`

**Description**

Optional. Open the file as an Illustrator library of this type. Default: `LibraryType.IllustratorArtwork`.

**Type**

[LibraryType](scripting-constants.md#jsobjref-scripting-constants-librarytype)

---

<a id="jsobjref-openoptions-preservelegacyartboard"></a>

### OpenOptions.preserveLegacyArtboard

`openOptions.preserveLegacyArtboard`

**Description**

Optional. Preserve legacy artboards when opening a legacy document in Illustrator CS4 or later. Default: `true`.

**Type**

Boolean.

---

<a id="jsobjref-openoptions-updatelegacygradientmesh"></a>

### OpenOptions.updateLegacyGradientMesh

`openOptions.updateLegacyGradientMesh`

**Description**

If `true`, preserves the spot colors in the gradient mesh objects for legacy documents (pre-Illustrator CS4). Default: `true`.

**Type**

Boolean.

---

<a id="jsobjref-openoptions-updatelegacytext"></a>

### OpenOptions.updateLegacyText

`openOptions.updateLegacyText`

**Description**

Optional. If `true`, update all legacy text items (from previous versions of Illustrator). Default: `false`.

**Type**

Boolean.

---

## Example

### Automatically updating legacy text on open

```default
// Opens a file with legacy text (AI 10 or older), using
// OpenOptions to automatically update the legacy text.

var fileRef = filePath;
if (fileRef != null) {
  var openOptions = new OpenOptions();
  openOptions.updateLegacyText = true;

  var docRef = open(fileRef, DocumentColorSpace.RGB, openOptions);
}
```
