import { patch } from "@web/core/utils/patch";
import { CustomerDisplay } from "@point_of_sale/customer_display/customer_display";
import { onWillStart } from "@odoo/owl";
import { OdooLogo } from "@point_of_sale/app/generic_components/odoo_logo/odoo_logo";

patch(OdooLogo, {
    props: {
        ...OdooLogo.props,
        sh_id: { type: Number, optional: true }
    },
    defaultProps: {
        ...OdooLogo.defaultProps,
        sh_id: 0
    }
})

patch(CustomerDisplay.prototype, {
    setup() {
        super.setup(...arguments);
        this.sh_id = 0
        onWillStart(async () => {
            var record = await this.env.services.orm.searchRead("sh.debranding.config", [], [], { limit: 1 });
            if (record && record.length) {
                this.sh_id = record[0].id
            }
        });
    },
});
