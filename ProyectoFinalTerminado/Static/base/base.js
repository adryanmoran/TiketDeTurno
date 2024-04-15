function toggleMenu() {
    var menuItems = document.getElementById("menuItems");
    menuItems.classList.toggle("show");
    var menuIcon = document.querySelector(".menu-icon");
    menuIcon.classList.toggle("active");
}
