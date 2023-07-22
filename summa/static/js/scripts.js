(function () {
  function scrollToElement(target) {
    const domRect = document.querySelector(target).getBoundingClientRect();
    window.scrollTo(domRect.x, domRect.y);
  };

  // this is to make sure the year shown on the page is updated at all times instead of manually updating it.
  document.querySelector(".js-footer-copy").innerText = `©${new Date().getFullYear()} Summa Encore. Your trusted partner for your digital success from planet`;

  // scroll to view for #about
  document.querySelector(".js-about-button").addEventListener("click", () => { scrollToElement(".js-about-section") });

  // scroll to view for #contact
  const contactButtons = document.querySelectorAll(".js-contact-button");
  for (button of contactButtons){
    button.addEventListener("click", () => { scrollToElement(".js-contact-section") })    
  };
  
}());