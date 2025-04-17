from odoo import models,fields,api,_

class AccountMoveLine(models.Model):
    _inherit = 'account.move'

    def action_register_payment(self):
        """ Crea un pago en grupo a partir de una factura seleccionada en el formulario. """

        self.ensure_one()  # Solo permite una factura a la vez en el formulario

        if self.state != "posted" or self.payment_state in ["paid", "reversed"]:
            return

        partner = self.partner_id

        # Crear un pago en grupo
        payment_group = self.env["account.payment"].create({
            "partner_id": partner.id,
            "partner_type": "customer" if self.move_type in ["out_invoice", "out_refund"] else "supplier",
            "company_id": self.company_id.id,
        })

        # Asociar las facturas al pago en grupo
        payment_group.to_pay_move_line_ids = [(6, 0, self.line_ids.filtered(lambda l: l.account_id.reconcile and not l.reconciled).ids)]

        return {
            "type": "ir.actions.act_window",
            "name": "Registrar Pago",
            "res_model": "account.payment",
            "view_mode": "form",
            "res_id": payment_group.id,
            "target": "current",
        }

class AccountPayment(models.Model):
    _inherit = 'account.payment'

    @api.depends()  # Sin dependencias para que no se recalcule automáticamente
    def _compute_to_pay_move_lines(self):
        for rec in self:
            pass  # No hacer nad