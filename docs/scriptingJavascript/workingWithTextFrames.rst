.. _scriptingJavascript/workingWithTextFrames:

Working with text frames
################################################################################

To create a text frame of a specific type in JavaScript, use the ``kind`` property of the ``text`` frame object::

  var rectRef = docRef.pathItems.rectangle(700, 50, 100, 100);
  //use the areaText method to create the text frame
  var areaTextRef = docRef.textFrames.areaText(rectRef);

----

Threaded frames
================================================================================

As in the Illustrator application, you can thread area text frames or path text frames.

To thread existing text frames, use the ``nextFrame`` or ``previousFrame`` property of the ``text frame`` object.

When copying the following script to the ESTK, place the value of the contents property on one line::

  var myDoc = documents.add();
  var myPathItem1 = myDoc.pathItems.rectangle(244, 64, 82, 76);
  var myTextFrame1 = myDoc.textFrames.areaText(myPathItem1);
  var myPathItem2 = myDoc.pathItems.rectangle(144, 144, 42, 116);
  var myTextFrame2 = myDoc.textFrames.areaText(myPathItem2);

  // use the nextFrame property to thread the text frames
  myTextFrame1.nextFrame = myTextFrame2;
  var sText = "This is two text frames linked together as one story, with text
  flowing from the first to the last. This is two text frames linked together as one
  story, with text flowing from the first to the last. This is two text frames linked
  together as one story. ";
  myTextFrame1.contents = sText;
  redraw();

Threaded frames make one story object
********************************************************************************

Threaded frames make a single story object. To observe this, run the following JavaScript after running
the script in “Threaded frames” on page 44.

::

  var myDoc = app.activeDocument
  alert("There are " + myDoc.textFrames.length + " text frames.")
  alert("There are " + myDoc.stories.length + " stories.")
