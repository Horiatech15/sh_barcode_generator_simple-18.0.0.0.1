import { PosStore } from "@point_of_sale/app/store/pos_store";
import { patch } from "@web/core/utils/patch";
import { OrderReceipt } from "@point_of_sale/app/screens/receipt_screen/receipt/order_receipt";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { PosOrder } from "@point_of_sale/app/models/pos_order";

patch(PosStore.prototype, {
  async setup() {
    await super.setup(...arguments);
  },
  async processServerData() {
    await super.processServerData();
    console.log(
      "=============>",
      this.models["sh.debranding.config"].getFirst()
    );
    var output = this.models["sh.debranding.config"].getFirst();
    this.custom_logo = { img: output.avatar, id: output.id };
  },
});

patch(OrderReceipt.prototype, {
  setup() {
    super.setup();
    this.pos = usePos();
    this.company_name =
      this.pos.models["sh.debranding.config"].getFirst()["display_name"];
  },
});

patch(PosOrder.prototype, {
  setup(vals) {
    super.setup(vals);
    var output = this.models["sh.debranding.config"].getFirst();
    this.custom_logo = { img: output.avatar, id: output.id };
  },
});
