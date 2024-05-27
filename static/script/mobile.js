let menuMobile = document.querySelector('#menu-icon')
let navbar = document.querySelector('.navigation')

menuMobile.onclick = () => {
    menuMobile.classList.toggle('bx-x');
    navbar.classList.toggle('active');
}



const barra_navegacao = document.querySelector('header');
let ultimoScroll = 0;

window.addEventListener('scroll', function() {
    const scrollAtual = window.scrollY;

    if (scrollAtual > ultimoScroll) {
        barra_navegacao.style.transform = 'translateY(-100%)';
    } else {
        barra_navegacao.style.transform = 'translateY(0)';
    }

    ultimoScroll = scrollAtual <= 0 ? 0 : scrollAtual;
});
