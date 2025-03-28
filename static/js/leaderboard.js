import * as base from "./base.js";

document.addEventListener("DOMContentLoaded", function () {
    base.logoMovingTop("kill_centre", 4, 4, 600,-1);
    base.logoMovingTop("kill_front", 6, 3, 400,-1);
    base.logoMovingTop("kill_back", 3, 4, 500,-1);
    base.logoMovingTop("survive_centre", 4, 4, 600,-1);
    base.logoMovingTop("survive_front", 6, 3, 400,-1);
    base.logoMovingTop("survive_back", 3, 4, 500,-1);
    base.logoMovingTop("kill_num", 4, 4, 600,-1);
    base.logoMovingTop("survive_num", 4, 4, 600,-1);

    base.stars();
})