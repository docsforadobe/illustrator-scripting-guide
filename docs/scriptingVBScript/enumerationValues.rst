.. highlight:: basic

.. _scriptingVBScript/enumerationValues:

Working with enumeration values
################################################################################

Properties that use enumeration values in VBScript use a numeral rather than a text value. For example,
the Orientation property of the ``TextFrame`` object specifies whether text content in the text frame is
horizontal or vertical. The property uses the ``aiTextOrientation`` enumeration, which has two possible
values, ``aiHorizontal`` and ``aiVertical``.

To find the numeral values of enumerations, use either of the following:

- The object browser in your scripting editor environment. See “Viewing the VBScript object model” on page 10.

- The Adobe lllustrator CC 2017 Scripting Reference: VBScript, which lists the numeral values directly after the constant value in the “Enumerations” chapter at the end of the book. The following example is from that table:

=====================  ====================  =======================================
**Enumeration type**   **Values**            **What it means**
=====================  ====================  =======================================
``AiTextOrientation``  ``aiHorizontal = 0``  The orientation of text in a text frame
                       ``aiVertical = 1``
=====================  ====================  =======================================

The following sample specifies vertical text orientation::

  Set appRef = CreateObject ("Illustrator.Application")
  Set docRef = appRef.Documents.Add
  Set textRef = docRef.TextFrames.Add
  textRef.Contents = "This is some text content."
  textRef.Left = 50
  textRef.Top = 700
  textRef.Orientation = 1

Generally, it is considered good scripting practice to place the text value in a comment following the
numeral value, as in the following sample statement::

  textRef.Orientation = 1 ' aiVertical
