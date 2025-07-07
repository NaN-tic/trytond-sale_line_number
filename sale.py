from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval


class SaleLine(metaclass=PoolMeta):
    __name__ = 'sale.line'
    number = fields.Char('Number', states={
            'readonly': Eval('sale_state') != 'draft',
            })

    def get_invoice_line(self):
        lines = super().get_invoice_line()
        for line in lines:
            line.number = self.number
        return lines
