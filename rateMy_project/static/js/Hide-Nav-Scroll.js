var prevScrollpos = window.pageYOffset;
window.onscroll = function() {

var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("navbar2").style.top = "0";
    {% if user.is_authenticated %}
    document.getElementById("drop").style.top = "45px";
    {% endif %}
  } else {
    document.getElementById("navbar2").style.top = "-70px";
    {% if user.is_authenticated %}
    document.getElementById("drop").style.top = "-110px";
    {% endif %}
  }
  prevScrollpos = currentScrollPos;
}
