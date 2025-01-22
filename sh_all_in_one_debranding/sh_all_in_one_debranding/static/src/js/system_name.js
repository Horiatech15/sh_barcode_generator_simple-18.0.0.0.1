/** @odoo-module **/
import { WebClient } from "@web/webclient/webclient";
import { patch } from "@web/core/utils/patch";
import { rpc } from "@web/core/network/rpc";

var debrand_title = "System";
var debrand_url = "System";

var debrand_title = "";
var debrand_url = "";

rpc(
  "/web/dataset/call_kw/sh.debranding.config/search_read",
  {
    model: "sh.debranding.config",
    method: "search_read",
    args: [[], ["name", "url"]],
    kwargs: {},
    limit: 1,
  },
  { async: false }
).then(function (output) {
  if (output && output[0]) {
    debrand_title = output[0]["name"];
    debrand_url = output[0]["url"];
  }
});

patch(WebClient.prototype, {
  setup() {
    super.setup();
    this.title.setParts({ zopenerp: debrand_title }); // zopenerp is easy to grep
  },
});
