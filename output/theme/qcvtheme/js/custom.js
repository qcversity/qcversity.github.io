const allPreElement = window.document.querySelectorAll("pre");

allPreElement.forEach((preEl) => {
  preEl.parentElement.classList.add("highlight");
});

document.addEventListener("DOMContentLoaded", function () {
  const navbar = document.querySelector(".nav.navbar-nav");
  const orderedIds = ["nav-home", "nav-about", "nav-contact", "nav-general"];

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
  }

  // Adjusting the layout for different pages
  const mainContent = document.getElementById("content");
  const sidebar = document.getElementById("sidebar");

  // if (isHomePage) {
  //   // Apply styles for the home page
  //   if (mainContent)
  //     mainContent.className =
  //       "col-sm-8" + ("{{ SIDEBAR_ON_LEFT }}" ? " col-sm-push-4" : "");
  //   if (sidebar)
  //     sidebar.className =
  //       "col-sm-4" + ("{{ SIDEBAR_ON_LEFT }}" ? " col-sm-pull-8" : "");
  // } else {
  //   // Apply styles for other pages
  //   if (mainContent)
  //     mainContent.className =
  //       "col-sm-9" + ("{{ SIDEBAR_ON_LEFT }}" ? " col-sm-push-3" : "");
  //   if (sidebar)
  //     sidebar.className =
  //       "col-sm-3" + ("{{ SIDEBAR_ON_LEFT }}" ? " col-sm-pull-9" : "");
  // }

  // const contentClass = isHomePage ? "col-sm-8" : "col-sm-9";
  // const sidebarClass = isHomePage ? "col-sm-4" : "col-sm-3";

  // // Apply the classes to the elements
  // if (document.getElementById("content")) {
  //   document.getElementById("content").className = contentClass;
  // }
  // if (document.getElementById("sidebar")) {
  //   document.getElementById("sidebar").className = sidebarClass;
  // }

  const contentElement = document.getElementById("content");
  const sidebarElement = document.getElementById("sidebar");

  if (isHomePage) {
    // Apply classes for the home page
    if (contentElement) contentElement.className = "container-lg";
    if (sidebarElement) sidebarElement.className = "col-sm-4";
  } else {
    // Apply classes for other pages
    if (contentElement) {
      contentElement.className = "container-lg";
      const rowElement = contentElement.querySelector(".row");
      if (rowElement) {
        const colElement = rowElement.querySelector('[class^="col-sm-"]');
        if (colElement) {
          // Change the class of the column element
          colElement.className = "col-sm-9";
        }
      }
    }
    if (sidebarElement) sidebarElement.className = "col-sm-3";
  }
});
