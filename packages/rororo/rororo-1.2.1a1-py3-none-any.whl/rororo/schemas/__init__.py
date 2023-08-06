"""
==============
rororo.schemas
==============

Validate request and response data using JSON Schema.

"""

from .exceptions import Error
from .schema import Schema
from .utils import defaults
from .validators import DefaultValidator, Validator

(defaults, DefaultValidator, Error, Schema, Validator)  # Make PEP8 happy
