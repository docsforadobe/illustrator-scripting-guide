.. highlight:: applescript

.. _scriptingApplescript/yourFirstScript:

Your first Illustrator script
################################################################################

The traditional first project in any programming language is displaying the message “Hello World!” In this
example, you create a new Illustrator document, then add a text frame containing this message. Follow
these steps:

In a default Mac OS installation, Script Editor is in ``/Applications/AppleScript/Script Editor/``.

If you cannot find the Script Editor application, you must reinstall it from your Mac OS system CD.

1. Open Script Editor.
2. Enter the following script::

    --Send the following commands to Illustrator
    tell application "Adobe Illustrator"
    --Create a new document
    set docRef to make new document
    --Create a new text frame with the string "Hello World"
    set textRef to make new text frame in docRef
    with properties {contents: "Hello World!", position:{200, 200}}
    end tell

3. In the Script Editor toolbar, click Run.

.. tip::
  To add the script to the Illustrator Scripts menu (File > Scripts), save the script in the Scripts folder. The script will appear on the menu the next time you start Illustrator. For details, see :ref:`introduction/executingScripts/installing`.

----

Adding features to “Hello World”
================================================================================

Next, we create a new script that makes changes to the Illustrator document you created with your first
script. Our second script demonstrates how to:

- Get the active document.
- Get the width of the active document.
- Resize the text frame to match the document’s width.

If you already closed the Illustrator document, run your first script again to create a new document.

Follow these steps:

1. In Script Editor, choose File > New to create a new script.
2. Enter the following code::

    tell application "Adobe Illustrator"
    -- current document is always the active document
    set docRef to the current document
    set docWidth to the width of docRef
    -- resize the text frame to match the page width
    set width of text frame 1 of docRef to docWidth
    -- alternatively, one can reference the item directly, as follows:
    set width of text frame 1 of current document to docWidth
    end tell

3. Run the script.
