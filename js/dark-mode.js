(function() {
  var toggle = document.getElementById('dark-mode-toggle');
  if (!toggle) {
    console.error('Dark mode toggle button not found');
    return;
  }

  toggle.addEventListener('click', function(e) {
    e.preventDefault();
    document.documentElement.classList.toggle('dark-mode');

    // Save preference to localStorage
    if (document.documentElement.classList.contains('dark-mode')) {
      localStorage.setItem('dark-mode', 'enabled');
    } else {
      localStorage.setItem('dark-mode', 'disabled');
    }
  });
})();