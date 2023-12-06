document.addEventListener("DOMContentLoaded", function () {
  const allPreElement = window.document.querySelectorAll("pre");
  const navbar = document.querySelector(".nav.navbar-nav");
  const orderedIds = ["nav-home", "nav-about", "nav-contact", "nav-general"];

  allPreElement.forEach((preEl) => {
    preEl.parentElement.classList.add("highlight");
  });

  orderedIds.forEach(function (id) {
    var el = document.getElementById(id);
    if (el) {
      navbar.appendChild(el);
    }
  });

  // Handle the about me section

  const currentPath = window.location.pathname;
  const homePath = "/pages/home.html";
  const isHomePage =
    currentPath === homePath ||
    currentPath === "/" ||
    currentPath === "/index.html";

  if (isHomePage) {
    const aboutMeContainer = document.getElementById("about-me-container");
    if (aboutMeContainer) {
      aboutMeContainer.style.display = "block";
    }
  };

  const avatarContainer = document.getElementById("avatar-container");
  if (avatarContainer) {
    avatarContainer.style.display = "block";
  }

  // Adjusting the layout for different pages
  // const mainContent = document.getElementById("content");
  // const sidebar = document.getElementById("sidebar");



  // const contentElement = document.getElementById("content");
  // const sidebarElement = document.getElementById("sidebar");

  // if (isHomePage) {
  //   // Apply classes for the home page
  //   if (contentElement) {
  //     contentElement.className = "container-lg mr-1 ml-100";
  //   }
  //   if (sidebarElement) {
  //     sidebarElement.className = "col-sm-4";
  //   }
  // } else {
  //   // Apply classes for other pages
  //   if (contentElement) {
  //     contentElement.className = "container-lg mr-1 ml-100";
  //     const rowElement = contentElement.querySelector(".row");
  //     if (rowElement) {
  //       const colElement = rowElement.querySelector('[class^="col-sm-"]');
  //       if (colElement) {
  //         // Change the class of the column element
  //         colElement.className = "col-sm-9";
  //       }
  //     }
  //   }
  //   if (sidebarElement) sidebarElement.className = "col-sm-3";
  // }
});
