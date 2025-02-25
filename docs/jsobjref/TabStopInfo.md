# TabStopInfo

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.tabStops`

#### Description

Information about the alignment, position, and other details for a tab stop in a [ParagraphAttributes](./ParagraphAttributes.md) object.

---

## Properties

### TabStopInfo.alignment

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.tabStops.alignment`

#### Description

The alignment of the tab stop.

Default: `Left`

#### Type

[TabStopAlignment](scripting-constants.md#tabstopalignment)

---

### TabStopInfo.decimalCharacter

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.tabStops.decimalCharacter`

#### Description

The character used for decimal tab stops.

Default: `.`

#### Type

String

---

### TabStopInfo.leader

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.tabStops.leader`

#### Description

The leader dot character.

#### Type

String

---

### TabStopInfo.position

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.tabStops.position`

#### Description

The position of the tab stop expressed in points.

Default: 0.0

#### Type

Number (double)

---

### TabStopInfo.typename

`app.activeDocument.textFrames[index].paragraphs[index].paragraphAttributes.tabStops.typename`

#### Description

The class name of the object.

#### Type

String; read-only.

---

## Example

### Displaying tab stop information

```javascript
// Displays tab stop information found in each text frame
// of current document, if any.

var docRef = app.activeDocument;
var sData = "Tab Stops Found \\rTabStop Leader\t\tTabStop Position\r";
var textRef = docRef.textFrames;

for( var i=0 ; i < textRef.length; i++ ) {
    // Get all paragraphs in the textFrames
    var paraRef = textRef[i].paragraphs;

    for ( p=0 ; p < paraRef.length ; p++ ) {
        // Get para attributes for all textRanges in paragraph
        var attrRef = paraRef[p].paragraphAttributes;
        var tabRef = attrRef.tabStops;

        if ( tabRef.length > 0 ) {
            for(var t=0; t<tabRef.length; t++){
                sData += "\t" + tabRef[t].leader + "\t\t";
                sData += "\t\t" + tabRef[t].position + "\r";
            } // end for
        } // end if
    } // end for
} // end for

var newTF = docRef.textFrames.add();
newTF.contents = sData;
newTF.top = 400;
newTF.left = 100; redraw();
```
