# This file is part sale_line_number module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import invoice, sale

def register():
    Pool.register(
        invoice.InvoiceLine,
        sale.SaleLine,
        module='sale_line_number', type_='model')
