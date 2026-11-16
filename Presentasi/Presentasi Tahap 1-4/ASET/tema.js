/* tema.js · tema terang/gelap dan transisi "debu" antar-slide.
   Dimuat di <head> setiap slide dan INDEX. Tidak butuh pustaka luar.

   Transisi: isi slide tersapu oleh tirai (clip-path, ringan), lalu slide berikutnya tersingkap dari arah yang sama.
   Latar halaman sama persis di kedua sisi, jadi tidak ada layar hitam.
   Tema terang: seluruh halaman dibalik warnanya (filter) dan logo dibalik sekali lagi agar tampil asli. */
(function () {
  'use strict';
  var D = document, H = D.documentElement;
  var KEY = 'ml-tema';
  var IN_FRAME = false;
  try { IN_FRAME = window.self !== window.top; } catch (e) { IN_FRAME = true; }

  /* ───────── Baca tema dan arah: hash (#t=light&d=b), lalu localStorage, lalu window.name ───────── */
  function parseHash() {
    var m = {};
    (location.hash || '').replace(/^#/, '').split('&').forEach(function (p) {
      var kv = p.split('='); if (kv[0]) m[kv[0]] = kv[1];
    });
    return m;
  }
  var hs = parseHash(), theme = null;
  if (hs.t === 'light' || hs.t === 'dark') theme = hs.t;
  if (!theme) { try { theme = localStorage.getItem(KEY); } catch (e) {} }
  if (!theme) { try { var mm = /(?:^|;)TEMA=(light|dark)/.exec(window.name || ''); if (mm) theme = mm[1]; } catch (e) {} }
  if (theme !== 'light') theme = 'dark';
  var backIn = hs.d === 'b';          // slide ini dibuka dengan tombol mundur

  function save() {
    try { localStorage.setItem(KEY, theme); } catch (e) {}
    try { window.name = 'TEMA=' + theme + ';'; } catch (e) {}
  }
  if (IN_FRAME) {
    H.classList.add('t-frame');       // pratinjau di INDEX: ikut tema induk, tanpa tombol dan animasi
  } else {
    H.setAttribute('data-tema', theme);
    H.classList.add('t-pre');         // panggung disembunyikan sampai animasi masuk siap
    save();
    try { if (location.hash && /(^#|&)t=/.test(location.hash)) history.replaceState(null, '', location.pathname + location.search); } catch (e) {}
  }

  var reduce = false;
  try { reduce = matchMedia('(prefers-reduced-motion: reduce)').matches; } catch (e) {}

  /* ───────── Transisi ringan: tirai menyapu (clip-path), tanpa filter berat ───────── */
  var stage = null, leaving = false, anim = null;

  /* Latar panggung dipindah ke elemen kembar di belakangnya, supaya hanya isi slide yang tersapu dan latar tetap */
  function mkBg() {
    var cs = getComputedStyle(stage), d = D.createElement('div');
    d.id = 't-bg';
    d.style.cssText = 'position:absolute;left:0;top:0;width:1920px;height:1080px;transform-origin:0 0;pointer-events:none;';
    ['Image', 'Size', 'Position', 'Repeat', 'Color', 'Origin', 'Clip'].forEach(function (k) { d.style['background' + k] = cs['background' + k]; });
    stage.parentNode.insertBefore(d, stage);
    stage.style.setProperty('background', 'none', 'important');
    var sync = function () { d.style.transform = stage.style.transform; };
    sync();
    try { new MutationObserver(sync).observe(stage, { attributes: true, attributeFilter: ['style'] }); } catch (e) {}
  }

  /* maju: isi tersapu ke kanan lalu slide baru muncul dari kiri; mundur: sebaliknya */
  var HIDE_R = 'inset(0 0 0 100%)', HIDE_L = 'inset(0 100% 0 0)', SHOW = 'inset(0 0 0 0)';
  function sweep(frames, dur, easing, done) {
    if (anim) { try { anim.cancel(); } catch (e) {} }
    anim = stage.animate(frames, { duration: dur, easing: easing, fill: 'forwards' });
    anim.onfinish = function () { if (done) done(); };
  }

  function enter() {
    H.classList.remove('t-pre');
    if (!stage || reduce) return;
    var from = backIn ? HIDE_R : HIDE_L;
    sweep([{ clipPath: from, opacity: 0 }, { clipPath: SHOW, opacity: 1 }], 420, 'cubic-bezier(.2,.8,.2,1)', function () {
      try { anim.cancel(); } catch (e) {} stage.style.clipPath = ''; stage.style.opacity = '';
    });
    if (!stage) H.classList.add('t-in');
  }

  function start() {
    if (IN_FRAME) return;
    stage = D.getElementById('stage');
    if (stage) mkBg();
    if (!stage) { H.classList.remove('t-pre'); H.classList.add('t-in'); }
    else requestAnimationFrame(function () { requestAnimationFrame(enter); });
    addButton();
  }

  /* ───────── Pindah halaman ───────── */
  function num(s) { var m = /SLIDE(\d+)/i.exec(s || ''); return m ? +m[1] : 0; }
  function leave(u) {
    if (leaving || IN_FRAME) { if (IN_FRAME) location.href = u; return; }
    leaving = true;
    var cur = num(location.pathname), tgt = num(u);
    var back = !!(cur && tgt && tgt < cur);
    save();
    var go = function () {
      var sep = u.indexOf('#') < 0 ? '#' : '&';
      location.href = u + sep + 't=' + theme + '&d=' + (back ? 'b' : 'f');
    };
    if (reduce) { go(); return; }
    if (stage) {
      sweep([{ clipPath: SHOW, opacity: 1 }, { clipPath: back ? HIDE_L : HIDE_R, opacity: 0 }], 260, 'cubic-bezier(.5,0,.8,.4)', go);
    } else {
      H.classList.add('t-fade');
      setTimeout(go, 300);
    }
  }

  /* ───────── Tombol tema ───────── */
  var SUN = '<svg class="sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.5v2.4M12 19.1v2.4M2.5 12h2.4M19.1 12h2.4M5.3 5.3L7 7M17 17l1.7 1.7M5.3 18.7L7 17M17 7l1.7-1.7"/></svg>';
  var MOON = '<svg class="moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4a8.2 8.2 0 1 0 10.2 10.2z"/></svg>';
  var btn = null, dockBtn = null;

  function label() {
    var t = theme === 'light' ? 'Mode gelap' : 'Mode terang';
    if (btn) { btn.title = t + ' (T)'; btn.setAttribute('aria-label', t); }
    if (dockBtn) dockBtn.textContent = theme === 'light' ? 'Mode gelap' : 'Mode terang';
  }
  function setTheme(t, animate) {
    theme = t; save();
    if (animate) {
      H.classList.add('t-anim');
      clearTimeout(setTheme._t); setTheme._t = setTimeout(function () { H.classList.remove('t-anim'); }, 700);
    }
    H.setAttribute('data-tema', t); label();
  }
  function toggle() {
    setTheme(theme === 'light' ? 'dark' : 'light', true);
    if (btn) { btn.classList.add('spin'); setTimeout(function () { btn.classList.remove('spin'); }, 520); }
  }
  function addButton() {
    btn = D.createElement('button');
    btn.id = 't-btn'; btn.type = 'button'; btn.innerHTML = SUN + MOON;
    btn.addEventListener('click', function (e) { e.stopPropagation(); toggle(); btn.blur(); });
    D.body.appendChild(btn);
    var ctrl = D.querySelector('#dock .ctrl');
    if (ctrl) {
      dockBtn = D.createElement('button'); dockBtn.className = 'btn'; dockBtn.id = 't-dock'; dockBtn.type = 'button';
      dockBtn.addEventListener('click', function (e) { e.stopPropagation(); toggle(); dockBtn.blur(); });
      ctrl.appendChild(dockBtn);
      var hint = D.querySelector('#dock .hint');
      if (hint && hint.textContent.indexOf('T tema') < 0) hint.textContent += ' · T tema';
    }
    label();
  }
  addEventListener('keydown', function (e) {
    if (IN_FRAME || e.metaKey || e.ctrlKey || e.altKey) return;
    if (e.key === 't' || e.key === 'T') toggle();
  });

  /* Tombol mundur/maju peramban (bfcache): jalankan animasi masuk lagi */
  addEventListener('pageshow', function (e) {
    if (!e.persisted || IN_FRAME) return;
    leaving = false; backIn = true;
    var hs2 = parseHash(); if (hs2.t) theme = hs2.t === 'light' ? 'light' : 'dark';
    var s2 = null; try { s2 = localStorage.getItem(KEY); } catch (er) {}
    if (s2) theme = s2 === 'light' ? 'light' : 'dark';
    H.setAttribute('data-tema', theme); label();
    if (stage && !reduce) enter();
  });

  /* Dengan DOMContentLoaded semua skrip slide sudah jalan; leave() milik slide diganti versi ini. */
  function boot() { window.leave = leave; start(); }
  if (D.readyState === 'loading') D.addEventListener('DOMContentLoaded', boot); else boot();

  /* Untuk pengujian dan pengaturan manual */
  window.TEMA = {
    leave: leave, toggle: toggle, set: function (t) { setTheme(t, false); },
    get theme() { return theme; },
  };
})();
