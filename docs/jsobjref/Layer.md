# Layer

`app.activeDocument.layers[index]`

#### Description

A layer in an Illustrator document. Layers may contain nested layers, which are called sublayers in the user interface.

The `layer` object contains all of the page items in the specific layer as elements.

Your script can access page items as elements of either the Layer object or as elements of the [Document](./Document.md) object. When accessing page items as elements of a layer, only objects in that layer can be accessed. To access page items throughout the entire document, be sure to refer to them as contained by the document.

---

## Properties

### Layer.artworkKnockout

`app.activeDocument.layers[index].artworkKnockout`

#### Description

Is this object used to create a knockout, and if so, what kind of knockout. You cannot set this value to `KnockoutState.Unknown`.

#### Type

[KnockoutState](scripting-constants.md#knockoutstate)

---

### Layer.blendingMode

`app.activeDocument.layers[index].blendingMode`

#### Description

The mode used when compositing an object.

#### Type

[BlendModes](scripting-constants.md#blendmodes)

---

### Layer.color

`app.activeDocument.layers[index].color`

#### Description

The layer's selection mark color.

#### Type

[RGBColor](./RGBColor.md)

---

### Layer.compoundPathItems

`app.activeDocument.layers[index].compoundPathItems`

#### Description

The compound path items contained in this layer.

#### Type

[CompoundPathItems](./CompoundPathItems.md); read-only.

---

### Layer.dimPlacedImages

`app.activeDocument.layers[index].dimPlacedImages`

#### Description

If `true`, placed images should be rendered as dimmed in this layer.

#### Type

Boolean.

---

### Layer.graphItems

`app.activeDocument.layers[index].graphItems`

#### Description

The graph items contained in this layer.

#### Type

[GraphItems](./GraphItems.md); read-only.

---

### Layer.groupItems

`app.activeDocument.layers[index].groupItems`

#### Description

The group items contained in this layer.

#### Type

[GroupItems](./GroupItems.md); read-only.

---

### Layer.hasSelectedArtwork

`app.activeDocument.layers[index].hasSelectedArtwork`

#### Description

If `true`, an object in this layer has been selected; set to `false` to deselect all objects in the layer.

#### Type

Boolean.

---

### Layer.isIsolated

`app.activeDocument.layers[index].isIsolated`

#### Description

If `true`, this object is isolated.

#### Type

Boolean.

---

### Layer.layers

`app.activeDocument.layers[index].layers`

#### Description

The layers contained in this layer.

#### Type

[Layers](./Layers.md); read-only.

---

### Layer.legacyTextItems

`app.activeDocument.layers[index].legacyTextItems`

#### Description

The legacy text items in this layer.

#### Type

[LegacyTextItems](./LegacyTextItems.md); read-only.

---

### Layer.locked

`app.activeDocument.layers[index].locked`

#### Description

If `true`, this layer is editable; set to false to lock the layer.

#### Type

Boolean.

---

### Layer.meshItems

`app.activeDocument.layers[index].meshItems`

#### Description

The mesh items contained in this layer.

#### Type

[MeshItems](./MeshItems.md); read-only.

---

### Layer.name

`app.activeDocument.layers[index].name`

#### Description

The name of this layer.

#### Type

String.

---

### Layer.nonNativeItems

`app.activeDocument.layers[index].nonNativeItems`

#### Description

The non-native art items in this layer.

#### Type

[NonNativeItems](./NonNativeItems.md)

---

### Layer.opacity

`app.activeDocument.layers[index].opacity`

#### Description

The opacity of the layer.

Range: 0.0 to 100.0.

#### Type

Number (double).

---

### Layer.pageItems

`app.activeDocument.layers[index].pageItems`

#### Description

The page items (all art item classes) contained in this layer.

#### Type

[PageItems](./PageItems.md)

---

### Layer.parent

`app.activeDocument.layers[index].parent`

#### Description

The document or layer that contains this layer.

#### Type

[Document](./Document.md) or [Layer](#layer); read-only.

---

### Layer.pathItems

`app.activeDocument.layers[index].pathItems`

#### Description

The path items contained in this layer.

#### Type

[PathItems](./PathItems.md); read-only.

---

### Layer.placedItems

`app.activeDocument.layers[index].placedItems`

#### Description

The placed items contained in this layer.

#### Type

[PlacedItems](./PlacedItems.md); read-only.

---

### Layer.pluginItems

`app.activeDocument.layers[index].pluginItems`

#### Description

The plug-in items contained in this layer.

#### Type

[PluginItems](./PluginItems.md); read-only.

---

### Layer.preview

`app.activeDocument.layers[index].preview`

#### Description

If `true`, this layer should be displayed using preview mode.

#### Type

Boolean.

---

### Layer.printable

`app.activeDocument.layers[index].printable`

#### Description

If `true`, this layer should be printed when printing the document.

#### Type

Boolean.

---

### Layer.rasterItems

`app.activeDocument.layers[index].rasterItems`

#### Description

The raster items contained in this layer.

#### Type

[RasterItems](./RasterItems.md); read-only.

---

### Layer.sliced

`app.activeDocument.layers[index].sliced`

#### Description

If `true`, the layer item is sliced.

Default: `false`.

#### Type

Boolean.

---

### Layer.symbolItems

`app.activeDocument.layers[index].symbolItems`

#### Description

The symbol items contained in the layer.

#### Type

[SymbolItems](./SymbolItems.md); read-only.

---

### Layer.textFrames

`app.activeDocument.layers[index].textFrames`

#### Description

The text art items contained in this layer.

#### Type

[TextFrameItems](./TextFrameItems.md); read-only.

---

### Layer.typename

`app.activeDocument.layers[index].typename`

#### Description

The class name of the referenced object.

#### Type

String; read-only.

---

### Layer.visible

`app.activeDocument.layers[index].visible`

#### Description

If `true`, this layer is visible.

#### Type

Boolean.

---

### Layer.zOrderPosition

`app.activeDocument.layers[index].zOrderPosition`

#### Description

The position of this layer within the stacking order of layers in the document.

#### Type

Number (long); read-only.

---

## Methods

### Layer.move()

`app.activeDocument.layers[index].move(relativeObject, insertionLocation)`

#### Description

Moves the object.

#### Parameters

|      Parameter      |                                 Type                                  |          Description          |
| ------------------- | --------------------------------------------------------------------- | ----------------------------- |
| `relativeObject`    | Object                                                                | Object to move element within |
| `insertionLocation` | [ElementPlacement](scripting-constants.md#elementplacement), optional | Location to move element to   |

#### Returns

[Layer](#layer)

---

### Layer.remove()

`app.activeDocument.layers[index].remove()`

#### Description

Deletes this object.

#### Returns

Nothing.

---

### Layer.zOrder()

`app.activeDocument.layers[index].zOrder(ZOrderCmd)`

#### Description

Arranges the layer's position in the stacking order of the containing layer or document (`parent`) of this object.

#### Parameters

|  Parameter  |                        Type                         |            Description            |
| ----------- | --------------------------------------------------- | --------------------------------- |
| `zOrderCmd` | [ZOrderMethod](scripting-constants.md#zordermethod) | Stacking order arrangement method |

#### Returns

Nothing.

---

## Example

### Bringing a layer to the front

```javascript
// Moves the bottom layer to become the topmost layer

if (documents.length > 0) {
    var countOfLayers = activeDocument.layers.length;
    if (countOfLayers > 1) {
        var bottomLayer = activeDocument.layers[countOfLayers - 1];
        bottomLayer.zOrder(ZOrderMethod.BRINGTOFRONT);
    } else {
        alert("The active document only has only 1 layer");
    }
}
```
