# -*- coding: utf-8 -*-

import sys
import os
import sphinx_rtd_theme
#from better import better_theme_path

# -- General configuration ------------------------------------------------

def setup(app):
    try:
      app.add_stylesheet('extra.css')

    except:
      app.add_css_file('extra.css')

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

# General information about the project.
project = u'Illustrator Scripting Guide'
copyright = u'2013 Adobe Systems Incorporated'
author = u'Adobe Systems Incorporated'

version = u'0.0.1'
release = u'0.0.1'

pygments_style = 'sphinx'

highlight_language = "javascript"

# -- Options for HTML output ----------------------------------------------

html_theme = "sphinx_rtd_theme"

html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_static_path = ['_static']

# Output file base name for HTML help builder.
htmlhelp_basename = 'ai-scripting-guide'
