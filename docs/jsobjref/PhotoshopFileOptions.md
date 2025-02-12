# PhotoshopFileOptions

`preferences.photoshopFileOptions`

**Description**

Options for opening a Photoshop file, used with the [Application.open()](Application.md#jsobjref-application-open) method. All properties are optional.

---

## Properties

### PhotoshopFileOptions.parent

`preferences.photoshopFileOptions.parent`

**Description**

The parent of this object.

**Type**

Object; read-only.

---

### PhotoshopFileOptions.pixelAspectRatioCorrection

`preferences.photoshopFileOptions.pixelAspectRatioCorrection`

**Description**

If `true`, imported images that have a non-square pixel aspect ratio should be adjusted.

**Type**

Boolean

---

### PhotoshopFileOptions.preserveImageMaps

`preferences.photoshopFileOptions.preserveImageMaps`

**Description**

If `true`, image maps should be preserved when document is converted.

Default: `true`

**Type**

Boolean

---

### PhotoshopFileOptions.preserveLayers

`preferences.photoshopFileOptions.preserveLayers`

**Description**

If `true`, layers should be preserved when document is converted.

Default: `true`

**Type**

Boolean

---

### PhotoshopFileOptions.preserveSlices

`preferences.photoshopFileOptions.preserveSlices`

**Description**

If `true`, slices should be preserved when document is converted.

Default: `true`

**Type**

Boolean

---

### PhotoshopFileOptions.typename

`preferences.photoshopFileOptions.typename`

**Description**

The class name of the referenced object.

**Type**

String; read-only.

---

## Example

### Opening a Photoshop file

```javascript
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
```
