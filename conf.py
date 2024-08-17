import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'OpenTTD 中文社区文档'
author = 'WenSim and China Set Team'
release = '0.1'
copyright = '2024 WenSim 与 China Set 团队'
templates_path = ['_templates']

language = 'zh_CN'
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
master_doc = 'index'
epub_show_urls = 'footnote'

# latex_engine = 'xelatex'
# latex_use_xindy = False
# latex_elements = {
#     'preamble': '\\usepackage[UTF8]{ctex}\n',
# }

myst_heading_anchors = 3

html_theme = 'sphinx_rtd_theme'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.duration',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.autosectionlabel',
    'myst_parser',
]

myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "deflist",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]
