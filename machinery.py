'''
@filename: machinery.py
@author: Krisna Pranav
'''

from IPython.core.magic import register_cell_magic
from .utilities import keep_available_packages, is_notebook

DEFAULT_MODEL = 'gpt-40-2024-08-06'

class Context:
    variables = None
    model = None
    vision_model = None
    verbose = False
    chat = []
    client = None
    version_client = None
    plugins_enabled = True
    seed = None 