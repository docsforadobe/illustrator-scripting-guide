.. _jsobjref/scriptingConstants:

Scripting Constants
################################################################################

This chapter lists and describes the enumerations defined for use with Illustrator JavaScript properties and methods.

----

.. _jsobjref/scriptingConstants/AlternateGlyphsForm:

AlternateGlyphsForm
********************************************************************************

========================================  ===========
                 Value                    Description
========================================  ===========
``AlternateGlyphsFormDEFAULTFORM``        todo
``AlternateGlyphsFormTRADITIONAL``        todo
``AlternateGlyphsFormEXPERT``             todo
``AlternateGlyphsFormJIS78FORM``          todo
``AlternateGlyphsFormJIS83FORM``          todo
``AlternateGlyphsFormHALFWIDTH``          todo
``AlternateGlyphsFormTHIRDWIDTH``         todo
``AlternateGlyphsFormQUARTERWIDTH``       todo
``AlternateGlyphsFormFULLWIDTH``          todo
``AlternateGlyphsFormPROPORTIONALWIDTH``  todo
``AlternateGlyphsFormJIS90FORM``          todo
``AlternateGlyphsFormJIS04FORM``          todo
========================================  ===========

**Example**

::

  textRef.textRange.characters[i].characterAttributes.alternateGlyphs == AlternateGlyphsForm.DEFAULTFORM;
  textRef.textRange.characters[i].characterAttributes.alternateGlyphs == AlternateGlyphsForm.FULLWIDTH
