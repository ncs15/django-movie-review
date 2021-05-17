
// sticky navbar

window.onscroll = function() {stickynav()};

var navbar = document.getElementById("navbar");
var sticky = navbar.offsetTop;

function stickynav() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
};



function unhide() {
var hid = document.getElementsByClassName("exp");
// Emulates jQuery $(element).is(':hidden');
if(hid[0].offsetWidth > 0 && hid[0].offsetHeight > 0) {
    hid[0].style.visibility = "visible";
    }
};

function openCity(evt, cityName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tab-detail-content");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " active";
};


// Function to reveal lightbox and adding YouTube autoplay
function revealVideo(div,video_id) {
  var video = document.getElementById(video_id).src;
  document.getElementById(video_id).src = video+'&autoplay=1'; // adding autoplay to the URL
  document.getElementById(div).style.display = 'block';
}

// Hiding the lightbox and removing YouTube autoplay
function hideVideo(div,video_id) {
  var video = document.getElementById(video_id).src;
  var cleaned = video.replace('&autoplay=1',''); // removing autoplay form url
  document.getElementById(video_id).src = cleaned;
  document.getElementById(div).style.display = 'none';
}


const pageHeader = document.querySelector(".page-header");
const openMobMenu = document.querySelector(".open-mobile-menu");
const closeMobMenu = document.querySelector(".close-mobile-menu");
const toggleSearchForm = document.querySelector(".search");
const searchForm = document.querySelector(".page-header form");
const topMenuWrapper = document.querySelector(".top-menu-wrapper");
const isVisible = "is-visible";
const showOffCanvas = "show-offcanvas";
const noTransition = "no-transition";
let resize;

openMobMenu.addEventListener("click", () => {
  topMenuWrapper.classList.add(showOffCanvas);
});

closeMobMenu.addEventListener("click", () => {
  topMenuWrapper.classList.remove(showOffCanvas);
});

toggleSearchForm.addEventListener("click", () => {
  searchForm.classList.toggle(isVisible);
});

window.addEventListener("resize", () => {
  pageHeader.querySelectorAll("*").forEach(function(el) {
    el.classList.add(noTransition);
  });
  clearTimeout(resize);
  resize = setTimeout(resizingComplete, 500);
});

function resizingComplete() {
  pageHeader.querySelectorAll("*").forEach(function(el) {
    el.classList.remove(noTransition);
  });
};

function unhide() {
  var hid = document.getElementsByClassName("exp");
    // Emulates jQuery $(element).is(':hidden');
  if(hid[0].offsetWidth > 0 && hid[0].offsetHeight > 0) {
    hid[0].style.visibility = "visible";
  }
}

