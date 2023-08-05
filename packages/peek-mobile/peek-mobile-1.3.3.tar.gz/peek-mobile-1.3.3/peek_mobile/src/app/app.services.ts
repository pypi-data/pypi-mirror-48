import {Ng2BalloonMsgService} from "@synerty/ng2-balloon-msg";
import {VortexService, VortexStatusService} from "@synerty/vortexjs";
import {TitleService, FooterService, NavBackService} from "@synerty/peek-util";
import {titleBarLinks} from "../plugin-title-bar-links";


export function titleServiceFactory() {
    return new TitleService(titleBarLinks);
}

export function footerServiceFactory() {
    return new FooterService([]);
}


export let peekRootServices = [
    // Ng2BalloonMsg
    Ng2BalloonMsgService,

    // Peek-Util
    {
        provide: TitleService,
        useFactory: titleServiceFactory
    },
    {
        provide: FooterService,
        useFactory: footerServiceFactory
    },
    NavBackService,

    // Vortex Services
    VortexStatusService,
    VortexService
];

