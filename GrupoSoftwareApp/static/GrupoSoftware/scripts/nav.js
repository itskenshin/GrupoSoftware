window.addEventListener("scroll", function(){
    var header = document.querySelector("nav");
    header.classList.toggle("navbar-fixed",window.scrollY>230);
})