document.addEventListener('DOMContentLoaded', () => {
  // Theme Toggle
  const themeToggle = document.getElementById('theme-toggle');
  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      const root = document.documentElement;
      const isDark = root.getAttribute('data-theme') === 'dark' ||
                    (!root.getAttribute('data-theme') && window.matchMedia('(prefers-color-scheme: dark)').matches);
      root.setAttribute('data-theme', isDark ? 'light' : 'dark');
    });
  }

  // Accordions
  const accordions = document.querySelectorAll('.acc');
  accordions.forEach(acc => {
    acc.addEventListener('click', () => {
      acc.classList.toggle('open');
      const icon = acc.querySelector('.acc-icon');
      if (icon) {
        icon.textContent = acc.classList.contains('open') ? '-' : '+';
      }
    });
  });

  // Mobile Menu Toggle (if overlay implemented)
  const menuBtn = document.getElementById('m-menu-btn');
  const menuOverlay = document.getElementById('m-menu-overlay');
  if (menuBtn && menuOverlay) {
    menuBtn.addEventListener('click', () => {
      menuOverlay.classList.toggle('hidden');
    });
  }

  // Sticky Header on Desktop
  const header = document.querySelector('.nav');
  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 0) {
        header.classList.add('sticky');
      } else {
        header.classList.remove('sticky');
      }
    });
  }
});
