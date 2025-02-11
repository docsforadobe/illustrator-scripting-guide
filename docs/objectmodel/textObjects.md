# Text Objects

When you type content in an Illustrator document, the type automatically becomes a `text frame` object and, at the same time, a story object.

To observe this, open a new document in Illustrator and use the horizontal text tool to type some text, then use the vertical text tool to type more text.

Finally, create a rectangle and type some text inside it.

Now run the following JavaScript script

```default
var myDoc = app.activeDocument;
alert("There are " + myDoc.textFrames.length + " text frames.");
alert("There are " + myDoc.stories.length + " stories.");
```

---

## Text Frames

There are three types of text frames:

- point
- area
- path

![Text Frames](_static/textFrames.jpg)

To create a specific kind of text frame, use the `kind` property of the `text frames` object in AppleScript.

The JavaScript and VBScript `text frames` objects contain specific methods for creating area text frames and path text frames.

As in the Illustrator application, you can thread area or path text frames.

To thread existing text frames, use the `next frame` or `previous frame` property of the `text frame` object.

Threaded frames make a single `story` object.

For information on creating or threading text frames, see the chapter in this manual for your scripting language.

### Text Geometry

While the three kinds of text frames have common characteristics, like `orientation`, each has type-specific qualities, as reflected in the `text frame` object’s properties. For example:

- An area text frame can have rows and columns, which you access through the `row count` and `column count` properties.
- Path text has `start T` value and `end T` value properties that indicate where on the path the text begins and ends.
- Area and path text frames are associated with a text path object, which is specified using the `text frame` object’s `text path` property. The text path defines the text frame’s position and orientation (horizontal or vertical) on the artboard (while the `text frame` object’s orientation property defines the `orientation` of text within the text frame). The `text path` property is not valid for point text, because point-text position and orientation are defined completely by the properties of the text frame itself.

!!! note
    A text path is not the same as a path art item. Text paths are associated with path art items that can be accessed and manipulated to modify the appearance of the associated text frame.

---

## Objects that represent text content

Within a text frame or story, the actual text content can be accessed as any of the following objects:

- `characters`
- `words`
- `paragraphs`
- `lines`

A `line` object is all the characters that fit on one line in a `text frame` or `story` object.

All text-art items have at least one line of text, defined as a `line` object.

Text art can have multiple text lines, if the text contains hard line breaks or its characters flow to a new line because they do not fit in the width of the text art.

Text objects are accessed and identified by collections within the `text frame` and `story` objects; for example

```default
textFrame("My Text Frame").paragraphs
// or
story("My Story").paragraphs
```

![Text Frames](_static/textModel.jpg)

Both `text frame` and `story` objects have `insertion point` and `text selection` properties.

The `text frame` object’s properties also include the defining features of the text frame, such as:

- The frame `width`, `height`, and `position`
- Whether the frame is `hidden` or `locked`
- Whether the text is `editable`

!!! note
    A `line` object cannot be created in a script. Your script can create `character`, `paragraph`, and `word` objects.

### Text ranges

The various text objects within a text frame or story also are represented collectively by the `text range` object.

For example, a character is a text range with a length of 1, and a word is a text range that has a space before it.

You can set the content of a text range object by passing a string using the `contents` property.

---

## Text styles

Text-style elements, like `font`, `capitalization`, and `justification`, are represented by `paragraph attribute` and `character attribute` objects.

These attribute objects are properties of the `paragraph style` and `character style` objects.

The `paragraph style` and `character style` objects have `apply to` and `remove` methods that allow your script to assign or remove attributes in a specific paragraph, character, or text range.

You can change the display properties of a text range by applying an appropriate style or providing local overrides of attributes at the text or paragraph levels:

- character style objects apply to sets of one or more characters. They control character features like `font`, `alignment`, `leading`, `language`, and `capitalization`, which are properties of the `character attribute` object.
- `paragraph style` objects apply to paragraphs. They control paragraph features like `first line indent`, `left indent`, and `right indent`, which are properties of the `paragraph attribute` object.
