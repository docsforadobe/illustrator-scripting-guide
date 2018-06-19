.. highlight:: applescript

.. _workingWithTextFrames:

Working with text frames
################################################################################

To create a text frame of a specific type in AppleScript, use the ``kind`` property of the ``text`` frame object::

  set myRect to make new rectangle in current document with properties
  {position:{100, 700}, height:100, width:100}
  set myAreaText to make new text frame in current document with properties
  {kind:point text,contents:"Text Frame 1"}

----

Threaded frames
================================================================================

As in the Illustrator application, you can thread area text frames or path text frames.

To thread existing text frames, use the ``next frame`` or ``previous frame`` property of the ``text frame`` object.

When copying the following script to your script editor, place the value of the contents property on one
line. The long-line character (``¬``) is not valid within a string value.

::

  tell application "Adobe Illustrator"
    make new document
    make new rectangle in current document with properties
      {position:{100, 500}, height:100, width:100}
    make new text frame in current document with properties
      {kind:area text, text path:the result, name:"tf1", contents:"This is two text frames linked together as one story, with text flowing from the first to the last. First frame content. "}
    make new rectangle in current document with properties
      {position:{300, 700}, height:100, width:100}
    make new text frame in current document with properties
      {kind:area text, text path:the result, name:"tf2", contents:"Second frame content." }
    --use the next frame property to thread the frames
      set next frame of text frame "tf1" of current document to
      text frame "tf2" of current document
    redraw
  end tell


Threaded frames make one story object
********************************************************************************

Threaded frames make a single story object. To observe this, run the following AppleScript after running
the script in “Threaded frames” on page 33.

::

  display dialog ("There are " & (count(text frames of current document)) & " text frames.")
  display dialog("There are " & (count(stories of current document)) & " stories.")
