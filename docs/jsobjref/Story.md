<a id="jsobjref-story"></a>

# Story

`story`

**Description**

A contiguous block of text as specified by a text range. A story can contain one or more text frames; if there is more than one, the multiple text frames are linked together to form a single story.

---

## Properties

<a id="jsobjref-story-characters"></a>

### Story.characters

`story.characters`

**Description**

All the characters in this story.

**Type**

[Characters](Characters.md#jsobjref-characters); read-only.

---

<a id="jsobjref-story-insertionpoints"></a>

### Story.insertionPoints

`story.insertionPoints`

**Description**

All the insertion points in this story.

**Type**

[InsertionPoints](InsertionPoints.md#jsobjref-insertionpoints); read-only.

---

<a id="jsobjref-story-length"></a>

### Story.length

`story.length`

**Description**

The number of characters in the story.

**Type**

Number (long); read-only.

---

<a id="jsobjref-story-lines"></a>

### Story.lines

`story.lines`

**Description**

All the lines in this story.

**Type**

[Lines](Lines.md#jsobjref-lines); read-only.

---

<a id="jsobjref-story-paragraphs"></a>

### Story.paragraphs

`story.paragraphs`

**Description**

All the paragraphs in this story.

**Type**

[Paragraphs](Paragraphs.md#jsobjref-paragraphs); read-only.

---

<a id="jsobjref-story-parent"></a>

### Story.parent

`story.parent`

**Description**

The object’s container.

**Type**

Object; read-only.

---

<a id="jsobjref-story-textframes"></a>

### Story.textFrames

`story.textFrames`

**Description**

The text frame items in this story.

**Type**

[TextFrameItems](TextFrameItems.md#jsobjref-textframeitems); read-only.

---

<a id="jsobjref-story-textrange"></a>

### Story.textRange

`story.textRange`

**Description**

The text range of the story.

**Type**

[TextRange](TextRange.md#jsobjref-textrange); read-only.

---

<a id="jsobjref-story-textranges"></a>

### Story.textRanges

`story.textRanges`

**Description**

All the text ranges in the story.

**Type**

[TextRanges](TextRanges.md#jsobjref-textranges); read-only.

---

<a id="jsobjref-story-textselection"></a>

### Story.textSelection

`story.textSelection`

**Description**

The selected text ranges in the story.

**Type**

Array of [TextRange](TextRange.md#jsobjref-textrange); read-only.

---

<a id="jsobjref-story-typename"></a>

### Story.typename

`story.typename`

**Description**

The class name of the object.

**Type**

String; read-only.

---

<a id="jsobjref-story-words"></a>

### Story.words

`story.words`

**Description**

All the words in the story.

**Type**

[Words](Words.md#jsobjref-words); read-only.

---

## Example

### Threading text frames into stories

```default
// Creates 1 story that flows through 2 text frames and another story that
// is displayed in a 3rd text frame
// Create a new document and add 2 area TextFrames
var docRef = documents.add();
var itemRef1 = docRef.pathItems.rectangle(600, 200, 50, 30);
var textRef1 = docRef.textFrames.areaText(itemRef1);
textRef1.selected = true;

// create 2nd text frame and link it the first
var itemRef2 = docRef.pathItems.rectangle(550, 300, 50, 200);
var textRef2 = docRef.textFrames.areaText(itemRef2, TextOrientation.HORIZONTAL, textRef1);
textRef2.selected = true;

// Add enough text to the 1st TextFrame to
// cause it to flow to the 2nd TextFrame.
textRef1.contents = "This is two text frames linked together as one story";
redraw();

// Create a 3rd text frame and count the stories
var textRef3 = docRef.textFrames.add();
textRef3.contents = "Each unlinked textFrame adds a new story."
textRef3.top = 650;
textRef3.left = 200;

redraw();
```
