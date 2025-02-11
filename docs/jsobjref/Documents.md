# Documents

`app.documents`

**Description**

A collection of [Document](Document.md#jsobjref-document) objects.

---

## Properties

### Documents.length

`app.documents.length`

**Description**

The number of objects in the collection.

**Type**

Number, read-only.

---

### Documents.parent

`app.documents.parent`

**Description**

The parent of this object.

**Type**

Object, read-only.

---

### Documents.typename

`app.documents.typename`

**Description**

The class name of the referenced object.

**Type**

String, read-only.

---

## Methods

### Documents.add()

```default
app.documents.add([documentColorSpace] [, width] [, height] [, numArtBoards]
    [, artboardLayout] [, artboardSpacing] [, artboardRowsOrCols]
)
```

**Description**

Creates a new document using optional parameters and returns a reference to the new document.

**Parameters**

| Parameter            | Type                                                                                                           | Description                   |
|----------------------|----------------------------------------------------------------------------------------------------------------|-------------------------------|
| `documentColorSpace` | [DocumentColorSpace](scripting-constants.md#jsobjref-scripting-constants-documentcolorspace), optional         | Color space of document       |
| `width`              | Number (double), optional                                                                                      | Width of document to add      |
| `height`             | Number (double), optional                                                                                      | Height of document to add     |
| `numArtBoards`       | Number (long), optional                                                                                        | Number of artboards to create |
| `artboardLayout`     | [DocumentArtboardLayout](scripting-constants.md#jsobjref-scripting-constants-documentartboardlayout), optional | Artboard layout               |
| `artboardSpacing`    | Number, optional                                                                                               | Number of pixels for spacing  |
| `artboardRowsOrCols` | Integer, optional                                                                                              | Number of rows or columns     |

**Returns**

[Document](Document.md#jsobjref-document)

---

### Documents.addDocument()

`app.documents.addDocument(startupPreset [, presetSettings] [, showOptionsDialog])`

**Description**

Creates a document from the preset, replacing any provided setting values, and returns a reference to the new document.

**Parameters**

| Parameter           | Type                                                                  | Description                    |
|---------------------|-----------------------------------------------------------------------|--------------------------------|
| `startupPreset`     | String                                                                | Startup preset to use          |
| `presetSettings`    | [DocumentPreset](DocumentPreset.md#jsobjref-documentpreset), optional | Preset document template       |
| `showOptionsDialog` | Boolean, optional                                                     | Whether to show options dialog |

**Returns**

[Document](Document.md#jsobjref-document)

---

### Documents.addDocumentNoUI()

`app.documents.addDocumentNoUI(startupPreset)`

**Description**

Creates a document without showing in UI.

**Parameters**

| Parameter       | Type   | Description           |
|-----------------|--------|-----------------------|
| `startupPreset` | String | Startup preset to use |

**Returns**

[Document](Document.md#jsobjref-document)

---

### Documents.getByName()

`app.documents.getByName(name)`

**Description**

Gets the first element in the collection with the specified name.

**Parameters**

| Parameter   | Type   | Description            |
|-------------|--------|------------------------|
| `name`      | String | Name of element to get |

**Returns**

[Document](Document.md#jsobjref-document)

---

### Documents.index()

`app.documents.index(itemKey)`

**Description**

Gets an element from the collection.

**Parameters**

| Parameter   | Type           | Description          |
|-------------|----------------|----------------------|
| `itemKey`   | String, Number | String or number key |

**Returns**

[Document](Document.md#jsobjref-document)

---

## Example

### Creating a new document

```default
// Creates a new document with an RGB color space

app.documents.add(DocumentColorSpace.RGB);
```
