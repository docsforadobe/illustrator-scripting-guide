<a id="jsobjref-printer"></a>

# Printer

`app.PrinterList[index`

**Description**

Associates an available printer with printer information.

To request a list of printers, you must first have a document open or an error is returned.

---

## Properties

<!-- jsobjref/Printer.name: -->

### Printer.name

`app.printerList[index].name`

**Description**

The printer name.

**Type**

String

---
<!-- jsobjref/Printer.printerInfo: -->

### Printer.printerInfo

`app.printerList[index].printerInfo`

**Description**

The printer information.

**Type**

[PrinterInfo](PrinterInfo.md#jsobjref-printerinfo)

---
<!-- jsobjref/Printer.typename: -->

### Printer.typename

`app.printerList[index].typename`

**Description**

The class name of the object.

**Type**

String; read-only.
