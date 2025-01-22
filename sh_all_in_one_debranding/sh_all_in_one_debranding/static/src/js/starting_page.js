import { WelcomeScreen } from "@website/client_actions/configurator/configurator";
import { patch } from "@web/core/utils/patch";
import { useService } from "@web/core/utils/hooks";

patch(WelcomeScreen.prototype, {
  setup() {
    super.setup();
    this.companyService = useService("company");
    this.company_name = this.companyService.currentCompany.name;
  },
});
