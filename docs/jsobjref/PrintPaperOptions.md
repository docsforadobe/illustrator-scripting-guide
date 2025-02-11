# PrintPaperOptions

`new PrintPaperOptions()`

**Description**

Information about the paper to be used in the print job.

---

## Properties

### PrintPaperOptions.height

`printPaperOptions.height`

**Description**

The custom height (in points) for using the custom paper.

Default: 0.0

**Type**

Number (double)

---

### PrintPaperOptions.name

`printPaperOptions.name`

**Description**

The paper's name.

**Type**

String

---

### PrintPaperOptions.offset

`printPaperOptions.offset`

**Description**

Custom offset (in points) for using the custom paper.

Default: 0.0

**Type**

Number (double)

---

### PrintPaperOptions.transverse

`printPaperOptions.transverse`

**Description**

If `true`, transverse the artwork (rotate 90 degrees) on the custom paper.

Default: `false`

**Type**

Boolean

---

### PrintPaperOptions.typename

`printPaperOptions.typename`

**Description**

The class name of the object.

**Type**

String; read-only.

---

### PrintPaperOptions.width

`printPaperOptions.width`

**Description**

The custom width (in points) for using the custom paper.

Default: 0.0

**Type**

Number (double)

---

## Example

### Setting print paper options

```default
// Creates a new document, adds a path item, applies a graphic style
// then prints with specified paper options
var docRef = documents.add();
var pathRef = docRef.pathItems.rectangle(600, 200, 200, 200);
docRef.graphicStyles[1].applyTo(pathRef);

var paperOpts = new PrintPaperOptions;
var printOpts = new PrintOptions;
printOpts.paperOptions = paperOpts;

var printerCount = printerList.length;
if (printerCount > 0) {

    // Print with the 1st paper from the 1st printer
    for (var i = 0; i < printerList.length; i++) {

        if (printerList[i].printerInfo.paperSizes.length > 0) {
            var printerRef = printerList[i];
        }

        var paperRef = printerRef.printerInfo.paperSizes[0];
        if (printerRef.printerInfo.paperSizes.length > 0){
            paperOpts.name = paperRef.name;
            printOpts.printerName = printerRef.name;
            docRef.print(printOpts);
        }
    }
}
```
