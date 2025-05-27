# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'family-chen'
copyright = '2025, joe'
author = 'joe'
release = 'v1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'recommonmark',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
]

# 设置主题
html_theme = 'sphinx_rtd_theme'
language = 'zh_CN'

# 支持Markdown
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}