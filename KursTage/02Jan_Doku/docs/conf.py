import os
import sys

sys.path.insert(0, os.path.abspath(".."))

project = "Mathutils"
author = "meee"
release = "0.1.0"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon"
]

html_theme = "alabaster"
