import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'OpenTTD 中文社区文档'
author = 'WenSim and contributors'
release = '0.1'
copyright = '2024 WenSim 与其他贡献者；在 CC BY-NC-SA 4.0 许可证下发布'
templates_path = ['_templates']
exclude_patterns = ['_build', '.venv']

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
    "sphinxcontrib.mermaid",
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

html_static_path = ['_static']
html_css_files = ['fonts.css']
