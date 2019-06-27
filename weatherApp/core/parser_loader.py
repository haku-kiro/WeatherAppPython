import os
import re
import inspect


def _get_parser_list(dirname):
    """
    Returns a list of files, as long as they don't start with two
    underscores.
    """
    files = [f.replace('.py', '')
             for f in os.listdir(dirname)
             if not f.startswith('__')]
    return files

def _import_parsers(parserFiles):

    # matches as long as the last part is parser
    m = re.compile('.+parser$', re.I)
    
    _modules = __import__('weatherterm.parsers',
                          globals(),
                          locals(),
                          parserFiles,
                          0)

    _parsers = [(k, v) for k, v in 
                inspect.getmembers(_modules)
                if inspect.ismodule(v) and m.match(k)]

    _classes = dict()

    for k, v in _parsers:
        _classes.update({k: v for k, v in inspect.getmembers(v)
                         if inspect.isclass(v) and m.match(k)})

    return _classes

def load(dirname):
    parserFiles = _get_parser_list(dirname)
    return _import_parsers(parserFiles)