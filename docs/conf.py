"""Sphinx configuration."""
project = "bestie1"
author = "Juan Ignacio Gelos"
copyright = "2024, Juan Ignacio Gelos"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
