"""Sphinx configuration."""
project = "svcpass"
author = "Unity Digital Services"
copyright = "2025, Unity Digital Services"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
