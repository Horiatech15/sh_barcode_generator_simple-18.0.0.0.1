/** @odoo-module **/

import {
  ErrorDialog,
  RPCErrorDialog,
  odooExceptionTitleMap,
  ClientErrorDialog,
  NetworkErrorDialog,
  WarningDialog,
} from "@web/core/errors/error_dialogs";
import { rpc } from "@web/core/network/rpc";

import { patch } from "@web/core/utils/patch";
import { _t } from "@web/core/l10n/translation";

var debrand_title = "";

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
    // console.log(output, debrand_title);

    ErrorDialog.title = debrand_title;
    ClientErrorDialog.title = debrand_title + " Client Error";
    NetworkErrorDialog.title = debrand_title + " Network Error";
  }
});

patch(ErrorDialog.prototype, {
  async setup() {
    super.setup();
    console.log(this.props);
    const result = await rpc(
      "/web/dataset/call_kw/sh.debranding.config/search_read",
      {
        model: "sh.debranding.config",
        method: "search_read",
        args: [[], ["name", "url"]],
        kwargs: {},
        limit: 1,
      },
      { async: false }
    );
    this.props.message = result[0].name + " Server Error";
  },
});

patch(WarningDialog.prototype, {
  setup() {
    super.setup();
    this.title = _t("Warning");
    this.inferTitle();
    const { data, message } = this.props;
    if (data && data.arguments && data.arguments.length > 0) {
      this.message = data.arguments[0];
    } else {
      this.message = message;
    }
  },
});

patch(RPCErrorDialog.prototype, {
  setup() {
    super.setup(), this.inferTitle();
    //        this.traceback = this.props.traceback;
    if (this.props && this.props.traceback) {
      this.traceback = this.props?.traceback.replace(/Odoo/gi, debrand_title);
    }

    if (this.props.data && this.props.data.debug) {
      //            this.traceback = `${this.props.data.debug}`;
      this.traceback = this.props.data.debug.replace(/Odoo/gi, debrand_title);
    }
  },
  inferTitle() {
    // If the server provides an exception name that we have in a registry.
    if (
      this.props.exceptionName &&
      odooExceptionTitleMap.has(this.props.exceptionName)
    ) {
      this.title = odooExceptionTitleMap
        .get(this.props.exceptionName)
        .toString();
      return;
    }
    // Fall back to a name based on the error type.
    if (!this.props.type) return;
    switch (this.props.type) {
      case "server":
        this.title = debrand_title + " Server Error";
        //this.env._t("Server Error");
        break;
      case "script":
        this.title = debrand_title + " Client Error";
        //this.title = this.env._t("Client Error");
        break;
      case "network":
        this.title = debrand_title + " Network Error";
        //                this.title = this.env._t("Network Error");
        break;
    }
  },
});
