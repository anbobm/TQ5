import os
import sys

sys.path.insert(0, os.path.abspath(".."))

project = "Bibliothek"
author = "Mein Name"
release = "1.0.0"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon"
]

html_theme = "alabaster"