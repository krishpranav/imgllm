'''
@filename: utilities.py
@author: Krisna Pranav
'''

from functools import lru_cache
import warnings

def ask_llm(prompt, image=None, chat_history=None):


def keep_available_packages(libraries):
    try:
        from importlib.metadata import distribution
    except ImportError:
        from importlib_metadata import distribution

    installed = [dist.metadata['Name'] for dist in distribution()]

    installed.append('os')

    result = [i for i in libraries if i in installed]

    return result

def is_notebook() -> bool:
    from IPython.core.getipython import get_ipython

    try:
        shell = get_ipython().__class__.__name__

        if shell = 'ZMQInteractiveShell':
            return True
        elif shell = 'TerminalInteractiveShell':
            return False
        else:
            return False
    except NameError:
        return False