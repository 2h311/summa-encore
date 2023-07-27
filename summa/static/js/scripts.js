(function () {
  function scrollToElement(target) {
    const domRect = document.querySelector(target).getBoundingClientRect();
    window.scrollTo(domRect.x, domRect.y);
  };

  // this is to make sure the year shown on the page is updated at all times instead of a manual update.
  const footerElement = document.querySelector(".js-footer-copy");
  if (footerElement) {
    footerElement.innerText = `©${new Date().getFullYear()} Summa Encore. Your trusted partner for your digital success from planet`;
  }

  // scroll to view for #about
  const aboutButtonElement = document.querySelector(".js-about-button");
  aboutButtonElement.addEventListener("click", () => {
    const jsAboutSection = document.querySelector(".js-about-section");
    if (!jsAboutSection) {
      location.replace(`${window.location.origin}#about`);
    } else {
      scrollToElement(".js-about-section");
    } 
  });

  // scroll to view for #contact
  const contactButtons = document.querySelectorAll(".js-contact-button");
  for (button of contactButtons) {
    button.addEventListener("click", () => {
      const contactSection = document.querySelector(".js-contact-section");
      if (!contactSection) {
        location.replace(`${window.location.origin}#contact-us`);
      } else {
        scrollToElement(".js-contact-section");
      }
    });   
  };
}());