extensions = ['sphinx.ext.autodoc', 'sphinx.ext.todo', 'sphinx.ext.viewcode']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = 'PyBuilder'
copyright = '2022, '
author = ''
version = '1.0.dev0'
release = '1.0.dev0'
language = 'en'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
todo_include_todos = True
html_static_path = ['_static']
htmlhelp_basename = 'PyBuilderdoc'
latex_elements = {}
latex_documents = [('index', 'PyBuilder.tex', 'PyBuilder Documentation', '', 'manual')]
man_pages = [('index', 'PyBuilder', 'PyBuilder Documentation', [''], 1)]
texinfo_documents = [('index', 'PyBuilder', 'PyBuilder Documentation', '', 'PyBuilder', 'One line description of project.', 'Miscellaneous')]
epub_title = 'PyBuilder'
epub_author = ''
epub_publisher = ''
epub_copyright = '2022, '
epub_exclude_files = ['search.html']

import sys
sys.path.insert(0, '/Users/manuelfreistein/Desktop/Dev/FST_Excercise/src')
