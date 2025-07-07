from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval


class InvoiceLine(metaclass=PoolMeta):
    __name__ = 'account.invoice.line'

    number = fields.Char('Number', states={
            'readonly': Eval('invoice_state') != 'draft',
            }, depends=['invoice_state'])
