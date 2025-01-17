# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.
from odoo import _

try:
    import barcode
    _lib_imported = True
except ImportError:
    _lib_imported = False
import random

# import werkzeug.exceptions
from odoo.exceptions import UserError


def get_random_number():
    random_num = str(random.randint(10000000000, 99999999999))
    random_first_digit = random.randint(1, 9)
    random_str = str(random_first_digit) + ''.join(map(str, random_num[:11]))
    return random_str

def generate_ean(barcode_type):
    if not _lib_imported:
        raise UserError(
            _('python-barcode is not installed. Please install it.'))
    EAN = barcode.get_barcode_class(barcode_type)
    ean = EAN(get_random_number())
    return ean.get_fullcode()
