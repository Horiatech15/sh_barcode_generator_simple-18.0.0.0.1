// odoo.define("sh_backend_debranging.Dashboard", function (require) {
//   "use strict";

//   // var AbstractAction = require('web.AbstractAction');
//   // var config = require('web.config');
//   // var core = require('web.core');
//   // var framework = require('web.framework');
//   // var session = require('web.session');
//   // var Widget = require('web.Widget');
//   // var rpc = require("web.rpc");

//   // var QWeb = core.qweb;
//   // var _t = core._t;
//     var dashboard = require("web_settings_dashboard");

//   dashboard.DashboardShare.include({
//     init: function (parent, data) {
//       this.data = data;
//       this.parent = parent;
//       var name = "";
//       var url = "";
//       rpc
//         .query(
//           {
//             model: "sh.debranding.config",
//             method: "search_read",
//             args: [[], ["name", "url"]],
//           },
//           { async: false }
//         )
//         .then(function (output) {
//           name = output && output[0] && output[0].name;
//           url = output && output[0] && output[0].url;
//         });
//       this.share_url = url;
//       this.share_text = encodeURIComponent(
//         "I am using - Awesome open source business apps."
//       );

//       this.name = name;
//       this.url = url;
//       return this._super.apply(this, arguments);
//     },
//   });
// });
