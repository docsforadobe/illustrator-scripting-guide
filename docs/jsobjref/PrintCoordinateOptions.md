<a id="jsobjref-printcoordinateoptions"></a>

# PrintCoordinateOptions

`new PrintCoordinateOptions()`

**Description**

Information about the media and associated printing parameters.

---

## Properties

<a id="jsobjref-printcoordinateoptions-emulsion"></a>

### PrintCoordinateOptions.emulsion

`printCoordinateOptions.emulsion`

**Description**

If `true`, flip artwork horizontally.

Default: `false`

**Type**

Boolean

---

<a id="jsobjref-printcoordinateoptions-fittopage"></a>

### PrintCoordinateOptions.fitToPage

`printCoordinateOptions.fitToPage`

**Description**

If `true`, proportionally scale the artwork to fit on media.

Default: `false`

**Type**

Boolean

---

<a id="jsobjref-printcoordinateoptions-horizontalscale"></a>

### PrintCoordinateOptions.horizontalScale

`printCoordinateOptions.horizontalScale`

**Description**

The horizontal scaling factor expressed as a percentage (100 = 100%).

Range: 1.0 to 10000.0.

Default: 100.0

**Type**

Number (double)

---

<a id="jsobjref-printcoordinateoptions-orientation"></a>

### PrintCoordinateOptions.orientation

`printCoordinateOptions.orientation`

**Description**

The artwork orientation.

Default: `PrintOrientation.PORTRAIT`

**Type**

[PrintOrientation](scripting-constants.md#jsobjref-scripting-constants-printorientation)

---

<a id="jsobjref-printcoordinateoptions-position"></a>

### PrintCoordinateOptions.position

`printCoordinateOptions.position`

**Description**

The artwork position on media.

Default: `PrintPosition.TRANSLATECENTER`

**Type**

[PrintPosition](scripting-constants.md#jsobjref-scripting-constants-printposition)

---

<a id="jsobjref-printcoordinateoptions-tiling"></a>

### PrintCoordinateOptions.tiling

`printCoordinateOptions.tiling`

**Description**

The page tiling mode.

Default: `PrintTiling.TILESINGLEFULLPAGE`

**Type**

[PrintTiling](scripting-constants.md#jsobjref-scripting-constants-printtiling)

---

<a id="jsobjref-printcoordinateoptions-typename"></a>

### PrintCoordinateOptions.typename

`printCoordinateOptions.typename`

**Description**

The class name of the object.

**Type**

String; read-only.

---

<a id="jsobjref-printcoordinateoptions-verticalscale"></a>

### PrintCoordinateOptions.verticalScale

`printCoordinateOptions.verticalScale`

**Description**

The vertical scaling factor expressed as a percentage (100 = 100%)

Range: 1.0 to 10000.0.

Default: 100.0

**Type**

Number (double)

---

## Example

### Managing print coordinates

```default
// Creates a new document with symbol items that extend
// off the page then print with each print orientation
var docRef = documents.add();
var y = 500;
var x = -70;

if (docRef.symbols.length > 0) {

  for (var i = 0; i < 5; i++) {
    symbolRef = docRef.symbols[0];

    symbolItemRef1 = docRef.symbolItems.add(symbolRef);
    symbolItemRef1.top = y;
    symbolItemRef1.left = x;

    x += 30;
  }

  redraw();

  // Print it with various Coordinate Options
  var coordinateOptions = new PrintCoordinateOptions();
  var options = new PrintOptions();
  options.coordinateOptions = coordinateOptions;

  coordinateOptions.emulsion = true; // reverse from right to left
  coordinateOptions.fitToPage = true; // fit artwork to page size
  coordinateOptions.orientation = PrintOrientation.LANDSCAPE;
  docRef.print(options);

  coordinateOptions.emulsion = false;
  coordinateOptions.fitToPage = false;
  coordinateOptions.orientation = PrintOrientation.PORTRAIT;
  coordinateOptions.horizontalScale = 50;
  coordinateOptions.verticalScale = 50;
  docRef.print(options);
}
```
