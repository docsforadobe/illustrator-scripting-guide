.. highlight:: basic

.. _scriptingVBScript/workingWithTextFrames:

Working with text frames
################################################################################

To create a text frame of a specific type in VBScript, use the ``TextFrames`` method that corresponds to the type of frame you want to create:::

  Set rectRef = docRef.PathItems.Rectangle(700, 50, 100, 100)

  ' Use the AreaText method to create the text frame
  Set areaTextRef = docRef.TextFrames.AreaText(rectRef)

----

Threaded frames
================================================================================

As in the Illustrator application, you can thread area text frames or path text frames.

To thread existing text frames, use the ``NextFrame`` or ``PreviousFrame`` property of the ``TextFrames`` object.

When copying the following script to your script editor, place the value of the ``Contents`` property on one
line. The long-line character (``_``) is not valid within a string value.

::

  Set appRef = CreateObject("Illustrator.Application")
  Set myDoc = appRef.Documents.Add
  Set myPathItem1 = myDoc.PathItems.Rectangle(244, 64, 82, 76)
  Set myTextFrame1 = myDoc.TextFrames.AreaText(myPathItem1)
    myTextFrame1.Contents = "This is two text frames linked together as one story, with text flowing from the first to the last."
  Set myPathItem2 = myDoc.PathItems.Rectangle(144, 144, 42, 116)
  Set myTextFrame2 = myDoc.TextFrames.AreaText(myPathItem2)

  'Use the NextFrame property to thread the frames
  myTextFrame1.NextFrame = myTextFrame2

  appRef.Redraw()


Threaded frames make one story object
********************************************************************************

Threaded frames make a single story object. To observe this, run the following VBScript after running
the script above.

::

  Set myDoc = appRef.ActiveDocument
  myMsg = "alert(""There are " & CStr(myDoc.TextFrames.Count) & " text frames. "")"
  appRef.DoJavaScript myMsg
  myMsg = "alert(""There are " & CStr(myDoc.Stories.Count) & " storiess. "")"
  appRef.DoJavaScript myMsg
