import os
import sys

sys.path.insert(0, os.path.abspath('..'))
project = 'Sphinx Demo'
author = 'Lotic'
release = '0.1.0'

extension = {
    'sphinx.ext.autodoc'
    'sphinx.ext.napoleon'
}

html_theme = 'alabaster'
