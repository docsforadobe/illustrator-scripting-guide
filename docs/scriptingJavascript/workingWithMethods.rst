.. _scriptingJavascript/workingWithMethods:

Working with methods in JavaScript
################################################################################

When you work with methods that have multiple parameters, you may omit optional parameters at the
end of the parameter list, but you may not omit parameters in the middle of the list. If you do not want to
specify a particular parameter in the middle of the list, you must insert the value ``undefined`` to use the
parameter’s default value. For example, the following definition describes the ``rotate()`` method for an art
object.

::

  rotate
    (angle
      [,changePositions]
      [,changeFillPatterns]
      [,changeFillGradients]
      [,changeStrokePattern]
      [,rotateAbout])

In the definition, taken from Adobe lllustrator CC 2017 Scripting Reference: JavaScript, optional parameters
are enclosed in square brackets ( [] ).

To rotate the object 30 degrees and change the ``fillGradients``, you would use the following script
statement::

  myObject.rotate(30, undefined, undefined, true);

You need to specify ``undefined`` for the ``changePositions`` and ``changeFillPatterns`` parameters. You do
not have to specify anything for the two optional parameters following ``changeFillGradients``, since they
are at the end of the parameter list.
