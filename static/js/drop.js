
  // select the dropdown menu and the Data_Analysis link
  var dropdownMenu = document.querySelector('.dropdown-menu');
  var dataAnalysisLink = document.querySelector('.dropdown .nav-link');

  // toggle the "show" class on the dropdown menu when the Data_Analysis link is clicked
  dataAnalysisLink.addEventListener('click', function() {
    dropdownMenu.classList.toggle('show');
  });

  // hide the dropdown menu when clicking outside of it
  document.addEventListener('click', function(event) {
    if (!event.target.closest('.dropdown')) {
      dropdownMenu.classList.remove('show');
    }
  });

