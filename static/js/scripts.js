(function () {
  // this is to make sure the year shown on the page is updated at all times instead of manually updating it.
  document.querySelector(".js-footer-copy").innerText = `©${new Date().getFullYear()} Summa Encore. Your trusted partner for your digital success from`;
}());