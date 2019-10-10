from .core import field, Field, MandatoryFieldInitError, UnsupportedOnNativeFieldError
from .validate_n_convert import Converter
from .init_makers import inject_fields, make_init, init_fields
from .helpers import copy_value, copy_field, copy_attr

try:
    # Distribution mode : import from _version.py generated by setuptools_scm during release
    from ._version import version as __version__
except ImportError:
    # Source mode : use setuptools_scm to get the current version from src using git
    from setuptools_scm import get_version as _gv
    from os import path as _path
    __version__ = _gv(_path.join(_path.dirname(__file__), _path.pardir))

__all__ = [
    '__version__',
    # submodules
    'core', 'validate_n_convert', 'init_makers', 'helpers',
    # symbols
    'field', 'Field', 'MandatoryFieldInitError', 'UnsupportedOnNativeFieldError',
    'Converter',
    'inject_fields', 'make_init', 'init_fields',
    'copy_value', 'copy_field', 'copy_attr'
]
