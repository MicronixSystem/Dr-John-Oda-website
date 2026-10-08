/* drjohnoda.com: nav, drawer, video, reveal-on-scroll. Vanilla, no dependencies. */
(function () {
  "use strict";

  var doc = document;
  var root = doc.documentElement;
  root.classList.add("js");

  /* Page-qualified links (index.html#x) collapse to #x on the page they point at,
     so the shared nav and footer markup stays byte identical across pages. */
  var page = location.pathname.split("/").pop() || "index.html";
  doc.querySelectorAll('a[href*="#"]').forEach(function (a) {
    var href = a.getAttribute("href");
    var i = href.indexOf("#");
    if (i > 0 && href.slice(0, i) === page) a.setAttribute("href", href.slice(i));
  });

  /* Real nav height for the hero (100svh minus nav) and sticky offsets. */
  var header = doc.querySelector(".site-header");
  function setNavHeight() {
    if (header) root.style.setProperty("--nav-h", header.offsetHeight + "px");
  }
  setNavHeight();
  window.addEventListener("resize", setNavHeight);

  /* Dropdowns */
  var toggles = Array.prototype.slice.call(doc.querySelectorAll(".site-nav__toggle"));
  function closeSubs(except) {
    toggles.forEach(function (t) {
      if (t !== except) t.setAttribute("aria-expanded", "false");
    });
  }
  toggles.forEach(function (t) {
    t.addEventListener("click", function () {
      var open = t.getAttribute("aria-expanded") === "true";
      closeSubs(t);
      t.setAttribute("aria-expanded", open ? "false" : "true");
    });
  });
  doc.addEventListener("click", function (e) {
    if (!e.target.closest(".site-nav__item")) closeSubs();
  });
  doc.querySelectorAll(".site-nav__item").forEach(function (item) {
    item.addEventListener("focusout", function (e) {
      if (window.matchMedia("(min-width: 1200px)").matches && !item.contains(e.relatedTarget)) {
        var t = item.querySelector(".site-nav__toggle");
        if (t) t.setAttribute("aria-expanded", "false");
      }
    });
  });

  /* Mobile drawer */
  var menuBtn = doc.querySelector(".site-header__menu");
  var panel = doc.getElementById("site-menu");
  function isMenuOpen() { return header && header.classList.contains("is-open"); }
  function setMenu(open, returnFocus) {
    if (!header || !menuBtn) return;
    header.classList.toggle("is-open", open);
    root.classList.toggle("menu-open", open);
    menuBtn.setAttribute("aria-expanded", open ? "true" : "false");
    if (open) {
      var first = panel && panel.querySelector("button, a");
      if (first) first.focus();
    } else {
      closeSubs();
      if (returnFocus) menuBtn.focus();
    }
  }
  if (menuBtn) {
    menuBtn.addEventListener("click", function () { setMenu(!isMenuOpen(), false); });
  }
  if (panel) {
    panel.addEventListener("keydown", function (e) {
      if (e.key !== "Tab" || !isMenuOpen()) return;
      var items = Array.prototype.filter.call(
        panel.querySelectorAll("a, button"),
        function (el) { return el.offsetParent !== null; }
      );
      items.unshift(menuBtn);
      var firstEl = items[0], lastEl = items[items.length - 1];
      if (e.shiftKey && doc.activeElement === firstEl) { e.preventDefault(); lastEl.focus(); }
      else if (!e.shiftKey && doc.activeElement === lastEl) { e.preventDefault(); firstEl.focus(); }
    });
  }
  window.matchMedia("(min-width: 1200px)").addEventListener("change", function (mq) {
    if (mq.matches && isMenuOpen()) setMenu(false, false);
  });

  doc.addEventListener("keydown", function (e) {
    if (e.key !== "Escape") return;
    var openToggle = toggles.filter(function (t) { return t.getAttribute("aria-expanded") === "true"; })[0];
    if (openToggle && !isMenuOpen()) { closeSubs(); openToggle.focus(); return; }
    if (isMenuOpen()) setMenu(false, true);
  });

  /* Video: never autoplays; plays with sound on click, native controls after. */
  doc.querySelectorAll("[data-video]").forEach(function (wrap) {
    var video = wrap.querySelector("video");
    var play = wrap.querySelector(".video__play");
    if (!video || !play) return;
    play.addEventListener("click", function () {
      video.controls = true;
      video.muted = false;
      wrap.classList.add("is-playing");
      var p = video.play();
      if (p && p.catch) p.catch(function () {});
      video.focus();
    });
  });

  /* Reveal on scroll */
  var reveals = doc.querySelectorAll(".reveal");
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduce || !("IntersectionObserver" in window)) {
    reveals.forEach(function (el) { el.classList.add("is-in"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-in");
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.12 });
    reveals.forEach(function (el) { io.observe(el); });
  }
})();
