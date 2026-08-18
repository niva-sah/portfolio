
document.addEventListener("DOMContentLoaded", function () {

    // =========================
    // MOBILE NAVBAR
    // =========================

    const menuToggle = document.getElementById("menuToggle");
    const navLinks = document.getElementById("navLinks");

    if (menuToggle && navLinks) {

        menuToggle.addEventListener("click", function () {
            navLinks.classList.toggle("show");
        });

        navLinks.querySelectorAll("a").forEach(function (link) {

            link.addEventListener("click", function () {
                navLinks.classList.remove("show");
            });

        });
    }


    // =========================
    // SMOOTH SCROLL
    // =========================

    document.querySelectorAll(".nav-links a").forEach(function (anchor) {

        anchor.addEventListener("click", function (e) {

            const targetId = this.getAttribute("href");

            if (targetId && targetId.startsWith("#")) {

                const target = document.querySelector(targetId);

                if (target) {

                    e.preventDefault();

                    target.scrollIntoView({
                        behavior: "smooth",
                        block: "start"
                    });

                }
            }

        });

    });

});
