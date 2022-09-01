let navbar = document.querySelector('.navbar');

window.addEventListener('scroll',function(){
    navbar.classList.toogle('.active',windows.scrollY > 0);
})