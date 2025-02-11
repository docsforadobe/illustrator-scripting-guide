<a id="jsobjref-preferences"></a>

# Preferences

`app.Preferences`

**Description**

Specifies the preferred options for AutoCAD, FreeHand, PDF, and Photoshop files.

---

## Properties

<a id="jsobjref-preferences-autocadfileoptions"></a>

### Preferences.AutoCADFileOptions

`app.preferences.AutoCADFileOptions`

**Description**

Options to use when opening or placing an AutoCAD file.

**Type**

[OpenOptionsAutoCAD](OpenOptionsAutoCAD.md#jsobjref-openoptionsautocad); read-only.

---

<a id="jsobjref-preferences-freehandfileoptions"></a>

### Preferences.FreeHandFileOptions

`app.preferences.FreeHandFileOptions`

**Description**

Options to use when opening or placing a FreeHand file.

**Type**

[OpenOptionsFreeHand](OpenOptionsFreeHand.md#jsobjref-openoptionsfreehand); read-only.

---

<a id="jsobjref-preferences-parent"></a>

### Preferences.parent

`app.preferences.parent`

**Description**

The parent of this object.

**Type**

object; read-only.

---

<a id="jsobjref-preferences-pdffileoptions"></a>

### Preferences.PDFFileOptions

`app.preferences.PDFFileOptions`

**Description**

Options to use when opening or placing a PDF file.

**Type**

[PDFFileOptions](PDFFileOptions.md#jsobjref-pdffileoptions); read-only.

---

<a id="jsobjref-preferences-photoshopfileoptions"></a>

### Preferences.PhotoshopFileOptions

`app.preferences.PhotoshopFileOptions`

**Description**

Options to use when opening or placing a Photoshop file.

**Type**

[PhotoshopFileOptions](PhotoshopFileOptions.md#jsobjref-photoshopfileoptions); read-only.

---

<a id="jsobjref-preferences-typename"></a>

### Preferences.typename

`app.preferences.typename`

**Description**

The class name of the referenced object.

**Type**

string; read-only.

---

## Methods

<a id="jsobjref-preferences-getbooleanpreference"></a>

### Preferences.getBooleanPreference

`app.preferences.getBooleanPreference(key)`

**Description**

Gets the boolean value of a given application preference.

**Parameters**

| Parameter   | Type   | Description              |
|-------------|--------|--------------------------|
| `key`       | String | Pref key of value to get |

**Returns**

Boolean

---

<a id="jsobjref-preferences-getintegerpreference"></a>

### Preferences.getIntegerPreference

`app.preferences.getIntegerPreference(key)`

**Description**

Gets the integer value of a given application preference.

**Parameters**

| Parameter   | Type   | Description              |
|-------------|--------|--------------------------|
| `key`       | String | Pref key of value to get |

**Returns**

Integer

---

<a id="jsobjref-preferences-getrealpreference"></a>

### Preferences.getRealPreference

`app.preferences.getRealPreference(key)`

**Description**

Gets the real-number value of a given application preference.

**Parameters**

| Parameter   | Type   | Description              |
|-------------|--------|--------------------------|
| `key`       | String | Pref key of value to get |

**Returns**

Real

---

<a id="jsobjref-preferences-getstringpreference"></a>

### Preferences.getStringPreference

`app.preferences.getStringPreference(key)`

**Description**

Gets the string value of a given application preference.

**Parameters**

| Parameter   | Type   | Description              |
|-------------|--------|--------------------------|
| `key`       | String | Pref key of value to get |

**Returns**

String

---

<a id="jsobjref-preferences-removepreference"></a>

### Preferences.removePreference

`app.preferences.removePreference(key)`

**Description**

Deletes a given application preference.

**Parameters**

| Parameter   | Type   | Description              |
|-------------|--------|--------------------------|
| `key`       | String | Pref key of value to get |

**Returns**

Nothing.

---

<a id="jsobjref-preferences-setbooleanpreference"></a>

### Preferences.setBooleanPreference

`app.preferences.setBooleanPreference(key, value)`

**Description**

Sets the boolean value of a given application preference.

**Parameters**

| Parameter   | Type    | Description              |
|-------------|---------|--------------------------|
| `key`       | String  | Pref key of value to get |
| `value`     | Boolean | Value to set             |

**Returns**

Nothing.

---

<a id="jsobjref-preferences-setintegerpreference"></a>

### Preferences.setIntegerPreference

`app.preferences.setIntegerPreference(key, value)`

**Description**

Sets the integer value of a given application preference.

**Parameters**

| Parameter   | Type    | Description              |
|-------------|---------|--------------------------|
| `key`       | String  | Pref key of value to get |
| `value`     | Integer | Value to set             |

**Returns**

Nothing.

---

<a id="jsobjref-preferences-setrealpreference"></a>

### Preferences.setRealPreference

`app.preferences.setRealPreference(key, value)`

**Description**

Sets the real-number value of a given application preference.

**Parameters**

| Parameter   | Type   | Description              |
|-------------|--------|--------------------------|
| `key`       | String | Pref key of value to get |
| `value`     | Double | Value to set             |

**Returns**

Nothing.

---

<a id="jsobjref-preferences-setstringpreference"></a>

### Preferences.setStringPreference

`app.preferences.setStringPreference(key, value)`

**Description**

Sets the string value of a given application preference.

**Parameters**

| Parameter   | Type   | Description              |
|-------------|--------|--------------------------|
| `key`       | String | Pref key of value to get |
| `value`     | String | Value to set             |

**Returns**

Nothing.
