document.addEventListener("DOMContentLoaded", function() {
    var janela = window.innerWidth;
    if (janela <= 780) {
        document.querySelector('header').style.background = '#fff';
    } else {
        document.querySelector('header').style.background = 'transparent';
    }
});