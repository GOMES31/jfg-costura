let menuOpen = false;

function toggleMenu() {
    menuOpen = !menuOpen;
    const overlay = document.getElementById('mobileMenuOverlay');
    const hamburgerMenu = document.getElementById('hamburger');
    if (menuOpen) {
        overlay.classList.add('active');
        document.body.style.overflowY = 'hidden';
        hamburgerMenu.style.display = 'none';

        console.log('MENU OPENED');
    } else {
        closeMenu();
    }
}

function closeMenu() {
    menuOpen = false;
    const overlay = document.getElementById('mobileMenuOverlay');
    const hamburgerMenu = document.getElementById('hamburger');
    overlay.classList.remove('active');
    document.body.style.overflowY = 'unset';
    hamburgerMenu.style.display = 'block';
}
