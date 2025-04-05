const days = document.getElementById("days");
const hours = document.getElementById("hours");
const minutes = document.getElementById("minutes");
const seconds = document.getElementById("seconds");
const countdown = document.getElementById("countdown");
const program = document.getElementById("program");
const mainNav = document.getElementById("mainNav");
const  mobileMenuBtn = document.getElementById("mobileMenuBtn");
const countdownDate = new Date("2025-09-23T00:00:00Z").getTime();


function fn_countdown(){
    const now = new Date().getTime();
    const distance = countdownDate - now;


    const daysLeft = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hoursLeft = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutesLeft = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const secondsLeft = Math.floor((distance % (1000 * 60)) / 1000);

    days.innerHTML = daysLeft;
    hours.innerHTML = hoursLeft;
    minutes.innerHTML = minutesLeft;
    seconds.innerHTML = secondsLeft;

    if (distance < 0) {
        clearInterval(countdownInterval);
        countdown.innerHTML = "EXPIRED";
    }
}
const countdownInterval = setInterval(fn_countdown, 1000);
program.style.display = "none";


mobileMenuBtn.addEventListener("click", function() {
    if (mainNav.style.display === "none" || mainNav.style.display === "") {
        mainNav.style.display = "block";
        mobileMenuBtn.innerHTML = "&#10005;";
    } else {
        mainNav.style.display = "none";
        mobileMenuBtn.innerHTML = "&#9776;";
    }
}
);

// restore the default display of the mainNav
window.addEventListener("resize", function() {
    if (window.innerWidth > 768) {
        mainNav.style.display = "flex";
        mobileMenuBtn.innerHTML = "&#9776;";
    } else {
        mainNav.style.display = "none";
        mobileMenuBtn.innerHTML = "&#9776;";
    }
}
);