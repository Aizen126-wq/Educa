window.addEventListener('DOMContentLoaded', () => {
  // Seleciona todos os links dentro do nav principal
  let nav_anchors = document.querySelectorAll('#navbar a');

  let currentPath = window.location.pathname;

  nav_anchors.forEach(anchor => {
    anchor.classList.remove('active');

    if (anchor.pathname === currentPath) {
      anchor.classList.add('active');    }
  });
});
