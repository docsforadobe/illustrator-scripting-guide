# Preferences

`app.Preferences`

**Description**

Specifies the preferred options for AutoCAD, FreeHand, PDF, and Photoshop files.

---

## Properties

### Preferences.AutoCADFileOptions

`app.preferences.AutoCADFileOptions`

**Description**

Options to use when opening or placing an AutoCAD file.

**Type**

[OpenOptionsAutoCAD](./OpenOptionsAutoCAD.md); read-only.

---

### Preferences.FreeHandFileOptions

`app.preferences.FreeHandFileOptions`

**Description**

Options to use when opening or placing a FreeHand file.

**Type**

[OpenOptionsFreeHand](./OpenOptionsFreeHand.md); read-only.

---

### Preferences.parent

`app.preferences.parent`

**Description**

The parent of this object.

**Type**

object; read-only.

---

### Preferences.PDFFileOptions

`app.preferences.PDFFileOptions`

**Description**

Options to use when opening or placing a PDF file.

**Type**

[PDFFileOptions](./PDFFileOptions.md); read-only.

---

### Preferences.PhotoshopFileOptions

`app.preferences.PhotoshopFileOptions`

**Description**

Options to use when opening or placing a Photoshop file.

**Type**

[PhotoshopFileOptions](./PhotoshopFileOptions.md); read-only.

---

### Preferences.typename

`app.preferences.typename`

**Description**

The class name of the referenced object.

**Type**

string; read-only.

---

## Methods

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
