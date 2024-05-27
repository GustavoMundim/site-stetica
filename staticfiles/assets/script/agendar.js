const fundo_pc = document.querySelector(".mobile-version");
const telaMobile = window.screen.width;

if (telaMobile < 600) {
    fundo_pc.classList.remove('min-h-screen');
} else {
    fundo_pc.classList.add('min-h-screen');
}