const allPreElement = window.document.querySelectorAll("pre");

allPreElement.forEach((preEl) => {
  preEl.parentElement.classList.add("highlight");
});
