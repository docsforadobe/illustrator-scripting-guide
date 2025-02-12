# TextFrameItem

`app.activeDocument.textFrames[index]`

#### Description

The basic art item for displaying text. From the user interface, this is text created with the Text tool. There are three types of text art in Illustrator: point text, path text, and area text. The type is indicated by the text frame's [kind](#kind) property.

When you create a text frame, you also create a [Story](./Story.md) object. However, threading text frames combines the frames into a single story object. To thread frames, use the [nextFrame](#textframeitemnextframe) or [previousFrame](#textframeitempreviousframe) property.

---

## Properties

### TextFrameItem.anchor

`app.activeDocument.textFrames[index].anchor`

#### Description

The position of the anchor point, the start of the base line for point text.

#### Type

Array of 2 numbers

---

### TextFrameItem.antialias

`app.activeDocument.textFrames[index].antialias`

#### Description

The type of anti-aliasing to use in the text.

#### Type

[TextAntialias](scripting-constants.md#textantialias)

---

### TextFrameItem.characters

`app.activeDocument.textFrames[index].characters`

#### Description

All the characters in this text frame.

#### Type

[Characters](./Characters.md); read-only.

---

### TextFrameItem.columnCount

`app.activeDocument.textFrames[index].columnCount`

#### Description

The column count in the text frame (area text only).

#### Type

Number (long)

---

### TextFrameItem.columnGutter

`app.activeDocument.textFrames[index].columnGutter`

#### Description

The column gutter in the text frame (area text only).

#### Type

Number (double)

---

### TextFrameItem.contents

`app.activeDocument.textFrames[index].contents`

#### Description

The text string.

#### Type

String

---

### TextFrameItem.contentVariable

`app.activeDocument.textFrames[index].contentVariable`

#### Description

The content variable bound to this text frame item.

#### Type

[Variable](./Variable.md)

---

### TextFrameItem.endTValue

`app.activeDocument.textFrames[index].endTValue`

#### Description

The end position of text along a path, as a value relative to the path's segments (path text only).

#### Type

Number (double)

---

### TextFrameItem.flowLinksHorizontally

`app.activeDocument.textFrames[index].flowLinksHorizontally`

#### Description

If `true`, flow text between linked frames horizontally first (area text only).

#### Type

Boolean

---

### TextFrameItem.insertionPoints

`app.activeDocument.textFrames[index].insertionPoints`

#### Description

All the insertion points in this text range.

#### Type

[InsertionPoints](./InsertionPoints.md); read-only.

---

### TextFrameItem.kind

`app.activeDocument.textFrames[index].kind`

#### Description

The type of a text frame item (area, path or point).

#### Type

[TextType](scripting-constants.md#texttype); read-only.

---

### TextFrameItem.lines

`app.activeDocument.textFrames[index].lines`

#### Description

All the lines in this text frame.

#### Type

[Lines](./Lines.md); read-only.

---

### TextFrameItem.matrix

`app.activeDocument.textFrames[index].matrix`

#### Description

The transformation matrix for this text frame.

#### Type

[Matrix](./Matrix.md); read-only.

---

### TextFrameItem.nextFrame

`app.activeDocument.textFrames[index].nextFrame`

#### Description

The linked text frame following this one.

#### Type

[TextFrameItem](#jsobjref-textframeitem)

---

### TextFrameItem.opticalAlignment

`app.activeDocument.textFrames[index].opticalAlignment`

#### Description

If `true`, the optical alignment feature is active.

#### Type

Boolean

---

### TextFrameItem.orientation

`app.activeDocument.textFrames[index].orientation`

#### Description

The orientation of the text.

#### Type

[TextOrientation](scripting-constants.md#textorientation)

---

### TextFrameItem.paragraphs

`app.activeDocument.textFrames[index].paragraphs`

#### Description

All the paragraphs in this text frame.

#### Type

[Paragraphs](./Paragraphs.md); read-only.

---

### TextFrameItem.parent

`app.activeDocument.textFrames[index].parent`

#### Description

The parent of this object.

#### Type

[Layer](./Layer.md) or [GroupItem](./GroupItem.md); read-only.

---

### TextFrameItem.previousFrame

`app.activeDocument.textFrames[index].previousFrame`

#### Description

The linked text frame preceding this one.

#### Type

[TextFrameItem](#jsobjref-textframeitem)

---

### TextFrameItem.rowCount

`app.activeDocument.textFrames[index].rowCount`

#### Description

The row count in the text frame (area text only).

#### Type

Number (long)

---

### TextFrameItem.rowGutter

`app.activeDocument.textFrames[index].rowGutter`

#### Description

The row gutter in the text frame (area text only).

#### Type

Number (double)

---

### TextFrameItem.spacing

`app.activeDocument.textFrames[index].spacing`

#### Description

The amount of spacing.

#### Type

Number (double)

---

### TextFrameItem.startTValue

`app.activeDocument.textFrames[index].startTValue`

#### Description

The start position of text along a path, as a value relative to the path's segments (path text only).

#### Type

Number (double)

---

### TextFrameItem.story

`app.activeDocument.textFrames[index].story`

#### Description

The story to which the text frame belongs.

#### Type

[Story](./Story.md); read-only.

---

### TextFrameItem.textPath

`app.activeDocument.textFrames[index].textPath`

#### Description

The path item associated with the text frame. Note: Valid only when [kind](#textframeitemkind) is area or path.

#### Type

[TextPath](./TextPath.md)

---

### TextFrameItem.textRange

`app.activeDocument.textFrames[index].textRange`

#### Description

The text range of the text frame.

#### Type

[TextRange](./TextRange.md); read-only.

---

### TextFrameItem.textRanges

`app.activeDocument.textFrames[index].textRanges`

#### Description

All the text in this text frame.

#### Type

[TextRanges](./TextRanges.md); read-only.

---

### TextFrameItem.textSelection

`app.activeDocument.textFrames[index].textSelection`

#### Description

The selected text range(s) in the text frame.

#### Type

Array of [TextRange](./TextRange.md); read-only.

---

### TextFrameItem.typename

`app.activeDocument.textFrames[index].typename`

#### Description

The class name of the referenced object.

#### Type

String; read-only.

---

### TextFrameItem.words

`app.activeDocument.textFrames[index].words`

#### Description

All the words in this text frame.

#### Type

[Words](./Words.md); read-only.

---

## Methods

### TextFrameItem.convertAreaObjectToPointObject()

`app.activeDocument.textFrames[index].convertAreaObjectToPointObject()`

#### Description

Converts the area-type text frame to a point-type text frame.

#### Returns

[TextFrameItem](#jsobjref-textframeitem)

---

### TextFrameItem.convertPointObjectToAreaObject()

`app.activeDocument.textFrames[index].convertPointObjectToAreaObject()`

#### Description

Converts the point-type text frame to an area-type text frame.

#### Returns

[TextFrameItem](#jsobjref-textframeitem)

---

### TextFrameItem.createOutline()

`app.activeDocument.textFrames[index].createOutline()`

#### Description

Converts the text in the text frame to outlines.

#### Returns

[GroupItem](./GroupItem.md)

---

### TextFrameItem.duplicate()

`app.activeDocument.textFrames[index].duplicate([relativeObject] [,insertionLocation])`

#### Description

Creates a duplicate of the selected object.

#### Parameters

|      Parameter      |                                 Type                                  |        Description         |
| ------------------- | --------------------------------------------------------------------- | -------------------------- |
| `relativeObject`    | Object, optional                                                      | Object to duplicate to     |
| `insertionLocation` | [ElementPlacement](scripting-constants.md#elementplacement), optional | Location to insert element |

#### Returns

[TextRange](./TextRange.md)

---

### TextFrameItem.move()

`app.activeDocument.textFrames[index].move(relativeObject, insertionLocation)`

#### Description

Moves the object.

#### Parameters

|      Parameter      |                                 Type                                  |          Description          |
| ------------------- | --------------------------------------------------------------------- | ----------------------------- |
| `relativeObject`    | Object                                                                | Object to move element within |
| `insertionLocation` | [ElementPlacement](scripting-constants.md#elementplacement), optional | Location to move element to   |

#### Returns

[TextRange](./TextRange.md)

---

### TextFrameItem.remove()

`app.activeDocument.textFrames[index].remove()`

#### Description

Deletes this object.

#### Returns

Nothing.

---

### TextFrameItem.resize()

```javascript
app.activeDocument.textFrames[index].resize(
    scaleX,
    scaleY
    [,changePositions]
    [,changeFillPatterns]
    [,changeFillGradients]
    [,changeStrokePattern]
    [,changeLineWidths]
    [,scaleAbout]
)
```

#### Description

Scales the art item where `scaleX` is the horizontal scaling factor and `scaleY` is the vertical scaling factor. 100.0 = 100%.

#### Parameters

|       Parameter       |                               Type                                |                       Description                       |
| --------------------- | ----------------------------------------------------------------- | ------------------------------------------------------- |
| `scaleX`              | Number (double)                                                   | Horizontal scaling factor                               |
| `scaleY`              | Number (double)                                                   | Vertical scaling factor                                 |
| `changePositions`     | Boolean, optional                                                 | Whether to effect art object positions and orientations |
| `changeFillPatterns`  | Boolean, optional                                                 | Whether to transform fill patterns                      |
| `changeFillGradients` | Boolean, optional                                                 | Whether to transform fill gradients                     |
| `changeStrokePattern` | Boolean, optional                                                 | Whether to transform stroke patterns                    |
| `changeLineWidths`    | Number (double), optional                                         | The amount to scale line widths                         |
| `scaleAbout`          | [Transformation](scripting-constants.md#transformation), optional | The point to use as anchor, to transform about          |

#### Returns

Nothing.

---

### TextFrameItem.rotate()

```javascript
app.activeDocument.textFrames[index].rotate(
    angle
    [,changePositions]
    [,changeFillPatterns]
    [,changeFillGradients]
    [,changeStrokePattern]
    [,rotateAbout]
)
```

#### Description

Rotates the art item relative to the current rotation. The object is rotated counter-clockwise if the `angle` value is positive, clockwise if the value is negative.

#### Parameters

|       Parameter       |                               Type                                |                       Description                       |
| --------------------- | ----------------------------------------------------------------- | ------------------------------------------------------- |
| `angle`               | Number (double)                                                   | The angle amount to rotate the element                  |
| `changePositions`     | Boolean, optional                                                 | Whether to effect art object positions and orientations |
| `changeFillPatterns`  | Boolean, optional                                                 | Whether to transform fill patterns                      |
| `changeFillGradients` | Boolean, optional                                                 | Whether to transform fill gradients                     |
| `changeStrokePattern` | Boolean, optional                                                 | Whether to transform stroke patterns                    |
| `rotateAbout`         | [Transformation](scripting-constants.md#transformation), optional | The point to use as anchor, to transform about          |

#### Returns

Nothing.

---

### TextFrameItem.transform()

```javascript
app.activeDocument.textFrames[index].transform(
    transformationMatrix
    [, changePositions]
    [, changeFillPatterns]
    [, changeFillGradients]
    [, changeStrokePattern]
    [, changeLineWidths]
    [, transformAbout]
)
```

#### Description

Transforms the art item by applying a transformation matrix.

#### Parameters

|       Parameter        |                               Type                                |                  Description                   |
| ---------------------- | ----------------------------------------------------------------- | ---------------------------------------------- |
| `transformationMatrix` | [Matrix](./Matrix.md)                                             | Transformation matrix to apply                 |
| `changePositions`      | Boolean, optional                                                 | Whether to change Positions                    |
| `changeFillPatterns`   | Boolean, optional                                                 | Whether to change Fill Patterns                |
| `changeFillGradients`  | Boolean, optional                                                 | Whether to change Fill Gradients               |
| `changeStrokePattern`  | Boolean, optional                                                 | Whether to change Stroke Pattern               |
| `changeLineWidths`     | Number (double), optional                                         | The amount to scale line widths                |
| `transformAbout`       | [Transformation](scripting-constants.md#transformation), optional | The point to use as anchor, to transform about |

#### Returns

Nothing.

---

### TextFrameItem.translate()

```javascript
app.activeDocument.textFrames[index].translate(
    [deltaX]
    [, deltaY]
    [, transformObjects]
    [, transformFillPatterns]
    [, transformFillGradients]
    [, transformStrokePatterns]
)
```

#### Description

Repositions the art item relative to the current position, where `deltaX` is the horizontal offset and `deltaY` is the vertical offset.

#### Parameters

|         Parameter         |           Type            |             Description              |
| ------------------------- | ------------------------- | ------------------------------------ |
| `deltaX`                  | Number (double), optional | Horizontal offset                    |
| `deltaY`                  | Number (double), optional | Vertical offset                      |
| `transformObjects`        | Boolean, optional         | Whether to transform Objects         |
| `transformFillPatterns`   | Boolean, optional         | Whether to transform Fill Patterns   |
| `transformFillGradients`  | Boolean, optional         | Whether to transform Fill Gradients  |
| `transformStrokePatterns` | Boolean, optional         | Whether to transform Stroke Patterns |

#### Returns

Nothing.

---

### TextFrameItem.zOrder()

`app.activeDocument.textFrames[index].zOrder(zOrderCmd)`

#### Description

Arranges the art item's position in the stacking order of the group or layer (parent) of this object.

#### Parameters

|  Parameter  |                        Type                         |            Description            |
| ----------- | --------------------------------------------------- | --------------------------------- |
| `zOrderCmd` | [ZOrderMethod](scripting-constants.md#zordermethod) | Stacking order arrangement method |

#### Returns

Nothing.

---

## Example

### Rotate a text art item

```javascript
// Duplicates and rotates the selected text art item 5 times
if ( app.documents.length > 0 ) {
    selectedItems = app.activeDocument.selection;

    // make sure something is selected.
    if ( selectedItems.length > 0 ) {

        // The selection must be a text art item
        if ( selectedItems[0].typename == "TextFrame" ) {

            // Get the parent of the text art so new text art items
            // can be inserted in the same group or layer
            dupSrc = selectedItems[0];
            textContainer = dupSrc.parent;

            // Create 5 new versions of the text art each rotated a bit
            for ( i = 1; i <= 5; i++ ) {
                dupText = dupSrc.duplicate( textContainer, ElementPlacement.PLACEATEND );
                dupText.rotate(180 * i/6);
            }
        }
    }
}
```
