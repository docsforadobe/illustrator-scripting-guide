.. _introduction/whatIsScripting:

What is Scripting?
################################################################################

A script is a series of commands that tells Illustrator to perform one or
more tasks. These tasks can be simple, affecting only one object in the
current document, or complex, affecting objects in all your Illustrator
documents.

The tasks might even involve other applications, like word processors,
spreadsheets, and database management programs.

For the most part, the building blocks of scripting correspond to the
Illustrator tools, menus, panels, and dialog boxes with which you are
already an expert. If you know what you want Illustrator to do, you can
write a script to do it.

----

Why use scripting?
================================================================================

Graphic design is a field characterized by creativity, but aspects of the work
are anything but creative. In fact, you probably notice that the time you spend
placing and replacing images, correcting errors in text, and preparing files
for printing at an image-setting service provider often reduces the time you
have available for doing creative work.

With a small investment of time and effort, you can learn to write short,
simple scripts that perform repetitive tasks for you. As your scripting skills
grow, you can move on to more complex scripts.

Scripting also can enhance your creativity, by quickly performing tasks you
might not have time to try. For example, you could write a script to
systematically create a series of objects, modifying the new objects’ position,
stroke, and fill properties along the way. You also could write a script that
accesses built-in transformation matrix functions to stretch, scale, and
distort a series of objects. Without scripting, you would likely miss out on
the creative potential of such labor-intensive techniques.

----

What about actions?
================================================================================

Both actions and scripts are ways of automating repetitive tasks,
but they work very differently:

- Actions use a program’s user interface to do their work. As an action runs,
  menu choices are executed, objects are selected, and recorded paths
  are created.

  Scripts do not use a program’s user interface to perform tasks, and scripts
  can execute faster than actions.

- Actions have very limited facilities for getting and responding
  to information.

  You cannot add conditional logic to an action; therefore, actions cannot
  make decisions based on the current situation, like changing the stroke
  type of rectangles but not ellipses.

  Scripts can get information and make decisions and calculations based on the
  information they receive from Illustrator.

- A script can execute an action, but actions cannot execute scripts.
