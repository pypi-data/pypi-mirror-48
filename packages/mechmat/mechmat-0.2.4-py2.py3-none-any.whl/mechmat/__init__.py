# -*- coding: utf-8 -*-

"""Top-level package for mechmat."""

__author__ = """Jelle Spijker"""
__email__ = 'spijker.jelle@gmail.com'
__version__ = '0.2.4'

from pint import UnitRegistry, set_application_registry

ureg = UnitRegistry(autoconvert_offset_to_baseunit=True, default_as_delta=False)
ureg.setup_matplotlib(True)
Q_ = ureg.Quantity
set_application_registry(ureg)

from mechmat.core.bibliography import bib
from mechmat.core.chainable import Chainable, Guarded
from mechmat.material import material_factory
