// /* @odoo-module */

// import { ThreadService } from "@mail/core/common/thread_service";
// import { patch } from "@web/core/utils/patch";
// import { session } from "@web/session";

// patch(ThreadService.prototype, {
//     avatarUrl(author, thread) {
//         if (thread?.type === "livechat" && author?.type === "guest") {
//             return '/web/binary/company_logo?company_id=' + session.company_id;
//         }
//         return super.avatarUrl(author, thread);
//     },

// });
