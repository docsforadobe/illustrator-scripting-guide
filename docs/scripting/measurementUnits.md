# Measurement Units

Illustrator uses points as the unit of measurement for almost all distances. One inch equals 72 points. The exception is values for properties like `kerning`, `tracking`, and the `aki` properties (used for Japanese text composition), which use em units. (See [Em space units](#scripting-measurementunits-emspaceunits))

Illustrator uses points when communicating with your scripts regardless of the current ruler units. If your script depends on adding, subtracting, multiplying, or dividing specific measurement values for units other than points, it must perform any unit conversions needed to represent your measurements as points. For example, to use inches for coordinates or measurement units, you must multiply all inch values by 72 when entering the values in your script.

The following table shows conversion formulas for various units of measurement:

| Unit        | Conversion formula                             |
|-------------|------------------------------------------------|
| centimeters | 28.346 points = 1 centimeter                   |
| inches      | 72 points = 1 inch                             |
| millimeters | 2.834645 points = 1 millimeter                 |
| picas       | 12 points = 1 pica                             |
| Qs          | 0.709 point = 1 Q (1 Q equals 0.23 millimeter) |

JavaScript provides the UnitValue object type, which offers unit-conversion utilities. For details, see [JavaScript Tools Guide](https://extendscript.docsforadobe.dev/)

---

## Em space units

Values that use em units instead of points are measured in thousandths of an em.

An em is proportional to the current font size.

For example, in a 6-point font, 1 em equals 6 points; in a 10-point font, 1 em equals 10 points.

In a 10-point font, a kerning value of 20 em units is equivalent to

```
(20 units x 10 points) / 1000 units/em = 0.2 points
```
