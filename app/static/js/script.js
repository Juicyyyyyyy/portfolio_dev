var categories = document.querySelector('body').getAttribute('data-categories').split(',');

document.querySelectorAll('.skills-nav-item').forEach(navItem => {
    navItem.addEventListener('click', () => {
        const category = navItem.getAttribute('data-category');
        showSkillsCategory(category);
    });
});

function showSkillsCategory(category) {
    categories.forEach(cat => {
        const element = document.getElementById(`${cat}-skills`);
        const navItem = document.querySelector(`.skills-nav-item[data-category="${cat}"]`);
        if (cat === category) {
            element.classList.remove('hidden');
            navItem.classList.add('active');
        } else {
            element.classList.add('hidden');
            navItem.classList.remove('active');
        }
    });
}

// Set initial state
showSkillsCategory(categories[0]);





        document.addEventListener("DOMContentLoaded", function () {
            particlesJS("particles-js", {
                particles: {
                    number: {
                        value: 100,
                        density: {
                            enable: true,
                            value_area: 800,
                        },
                    },
                    color: {
                        value: "#ffffff",
                    },
                    shape: {
                        type: "circle",
                        stroke: {
                            width: 0,
                            color: "#000000",
                        },
                        polygon: {
                            nb_sides: 5,
                        },
                    },
                    opacity: {
                        value: 0.5,
                        random: false,
                        anim: {
                            enable: false,
                            speed: 1,
                            opacity_min: 0.1,
                            sync: false,
                        },
                    },
                    size: {
                        value: 3,
                        random: true,
                        anim: {
                            enable: false,
                            speed: 40,
                            size_min: 0.1,
                            sync: false,
                        },
                    },
                    line_linked: {
                        enable: true,
                        distance: 150,
                        color: "#ffffff",
                        opacity: 0.4,
                        width: 1,
                    },
                    move: {
                        enable: true,
                        speed: 1, // Reduced speed from 6 to 1
                        direction: "none",
                        random: false,
                        straight: false,
                        out_mode: "out",
                        bounce: false,
                        attract: {
                            enable: false,
                            rotateX: 600,
                            rotateY: 1200,
                        },
                    },

                },
                interactivity: {
                    detect_on: "canvas",
                    events: {
                        onhover: {
                            enable: true,
                            mode: "grab",
                        },
                        onclick: {
                            enable: true,
                            mode: "push",
                        },
                        resize: true,
                    },
                    modes: {
                        grab: {
                            distance: 140,
                            line_linked: {
                                opacity: 1,
                            },
                        },
                        bubble: {
                            distance: 400,
                            size: 40,
                            duration: 2,
                            opacity: 8,
                            speed: 3,
                        },
                        repulse: {
                            distance: 200,
                            duration: 0.4,
                        },
                        push: {
                            particles_nb: 4,
                        },
                        remove: {
                            particles_nb: 2,
                        },
                    },
                },
                retina_detect: true,
            });
        });

    document.getElementById("burger").addEventListener("click", function() {
        var navContent = document.getElementById("nav-content");
        navContent.classList.toggle("hidden");
        navContent.classList.toggle("block");
    });



/* Hide menu on scroll JavaScript */
var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("custom-navbar").style.top = "0";
  } else {
    document.getElementById("custom-navbar").style.top = "-100px"; // Updated height
  }
  prevScrollpos = currentScrollPos;
}


