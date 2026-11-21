// Record a walkthrough of the intern-agent dashboard (made-up demo data) and write the
// captions as an ASS subtitle file next to the video.
//   node record.js <outdir>
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const OUT = process.argv[2];
const BASE = 'http://127.0.0.1:8765';
const W = 1280, H = 800;

const CURSOR = `
(() => {
  if (document.getElementById('demo-cursor')) return;
  const c = document.createElement('div');
  c.id = 'demo-cursor';
  c.innerHTML = '<svg width="26" height="26" viewBox="0 0 24 24"><path d="M4 2l16 9-7 2-3 7z" fill="#fff" stroke="#111" stroke-width="1.5" stroke-linejoin="round"/></svg>';
  Object.assign(c.style, {position:'fixed', left:'0', top:'0', zIndex:2147483647, pointerEvents:'none', transition:'transform 0.6s cubic-bezier(.4,0,.2,1)', transform:'translate(720px,450px)', filter:'drop-shadow(0 2px 3px rgba(0,0,0,.5))'});
  document.body.appendChild(c);
  const ring = document.createElement('div');
  ring.id = 'demo-ring';
  Object.assign(ring.style, {position:'fixed', width:'34px', height:'34px', borderRadius:'50%', border:'2px solid #a5b4fc', zIndex:2147483646, pointerEvents:'none', opacity:'0', transition:'opacity .35s, transform .35s'});
  document.body.appendChild(ring);
  // The "add your Gmail" setup hint is not part of the demo.
  const style = document.createElement('style');
  style.textContent = '#demo-hide{display:none!important} #ask-open{display:none!important}';
  document.head.appendChild(style);
  // The demo has no Gmail connected; its setup hints are not what a configured
  // dashboard shows, so they are hidden whenever the app renders them.
  const hide = () => {
    for (const el of document.querySelectorAll('p, div, span'))
      if (el.style.display !== 'none' && el.textContent.length < 240 && /Add GMAIL_ADDRESS|Sending is off until Gmail/.test(el.textContent)) el.style.display = 'none';
  };
  hide();
  new MutationObserver(hide).observe(document.body, { childList: true, subtree: true });
})()`;

const captions = [];
let t0 = 0;
const now = () => (Date.now() - t0) / 1000;
let open = null;
function caption(text) {
  if (open) { open.end = now(); captions.push(open); }
  open = text ? { start: now(), text } : null;
}
const wait = (ms) => new Promise((r) => setTimeout(r, ms));

async function cursorTo(page, x, y) {
  await page.evaluate(([x, y]) => { const c = document.getElementById('demo-cursor'); if (c) c.style.transform = `translate(${x}px,${y}px)`; }, [x, y]);
  await wait(700);
}
async function clickOn(page, locator) {
  const box = await locator.boundingBox();
  const x = box.x + Math.min(box.width / 2, 60), y = box.y + box.height / 2;
  await cursorTo(page, x, y);
  await page.evaluate(([x, y]) => { const r = document.getElementById('demo-ring'); r.style.left = (x - 17) + 'px'; r.style.top = (y - 17) + 'px'; r.style.opacity = '1'; setTimeout(() => r.style.opacity = '0', 350); }, [x, y]);
  await locator.click();
  await wait(500);
  await page.evaluate(CURSOR);
}
async function scrollRows(page, to, ms = 2500) {
  await page.evaluate(([to, ms]) => new Promise((done) => {
    const el = document.getElementById('rows');
    const from = el.scrollTop, start = performance.now();
    const target = typeof to === 'number' ? to : (() => { const t = [...el.querySelectorAll('*')].find((n) => n.children.length === 0 && n.textContent.trim() === to); return t ? el.scrollTop + t.getBoundingClientRect().top - el.getBoundingClientRect().top - 24 : from; })();
    const step = (t) => { const k = Math.min(1, (t - start) / ms); const e = k < .5 ? 2 * k * k : 1 - Math.pow(-2 * k + 2, 2) / 2; el.scrollTop = from + (target - from) * e; k < 1 ? requestAnimationFrame(step) : done(); };
    requestAnimationFrame(step);
  }), [to, ms]);
}
async function scrollDetail(page, text, ms = 2000) {
  await page.evaluate(([text, ms]) => new Promise((done) => {
    const t = [...document.querySelectorAll('*')].find((n) => n.children.length === 0 && n.textContent.trim() === text && n.getBoundingClientRect().left > window.innerWidth * 0.6);
    if (!t) return done();
    let el = t.parentElement; while (el && !(el.scrollHeight > el.clientHeight + 20 && /auto|scroll/.test(getComputedStyle(el).overflowY))) el = el.parentElement;
    if (!el) return done();
    const from = el.scrollTop, target = from + t.getBoundingClientRect().top - el.getBoundingClientRect().top - 40, start = performance.now();
    const step = (s) => { const k = Math.min(1, (s - start) / ms); const e = k < .5 ? 2 * k * k : 1 - Math.pow(-2 * k + 2, 2) / 2; el.scrollTop = from + (target - from) * e; k < 1 ? requestAnimationFrame(step) : done(); };
    requestAnimationFrame(step);
  }), [text, ms]);
}
async function go(page, label) {
  await clickOn(page, page.locator('#nav').getByText(label, { exact: true }).first());
  await page.waitForLoadState('networkidle');
  await wait(400);
  await page.evaluate(CURSOR);
}

(async () => {
  const browser = await chromium.launch();
  const context = await browser.newContext({ viewport: { width: W, height: H }, deviceScaleFactor: 1, recordVideo: { dir: OUT, size: { width: W, height: H } } });
  const page = await context.newPage();
  t0 = Date.now();
  await page.goto(BASE + '/#/', { waitUntil: 'networkidle' });
  await page.evaluate(CURSOR);
  await wait(600);

  caption('The intern-agent dashboard. Every company and person here is made up.');
  await wait(3500);
  caption('Each morning it shows what both agents found, and what needs you.');
  await cursorTo(page, 520, 350); await wait(2300);

  await go(page, 'Job pipeline');
  caption('Job pipeline: everything emailed or applied to, moved along by what comes back to Gmail.');
  await wait(3200);
  caption('Emailed, delivered, replied, interview: the funnel shows where things drop.');
  await scrollRows(page, 'Outreach', 1800); await wait(2200);
  caption('Takeaways are computed from the numbers, not written by AI.');
  await scrollRows(page, 'What this says', 1500); await wait(2800);
  caption('One column per stage: waiting, replied, assessment, interview, offer, rejected, bounced.');
  await scrollRows(page, 99999, 3000); await wait(1200);
  const board = page.locator('.pipe-board');
  if (await board.count()) { await board.first().scrollIntoViewIfNeeded(); await wait(1600); }

  caption('Open a card for the lead and its inbox timeline.');
  const card = page.locator('.pipe-card.link').filter({ hasText: 'Quillpath' }).first();
  if (await card.count()) { await clickOn(page, card); }
  await wait(2200);
  await scrollDetail(page, 'Inbox', 1500); await wait(2200);

  await go(page, 'All leads');
  caption('All leads: where each one was found, the address emailed, and what came back.');
  await scrollRows(page, 'Leads', 2000); await wait(1500);
  const row = page.locator('#rows [data-key]').filter({ hasText: 'Brightkeel' }).first();
  if (await row.count()) await clickOn(page, row);
  caption('Every lead is scored 0 to 100 against the resume, with reasons and talking points.');
  await wait(3800);
  caption('Then the drafted email: the batches send these on their own, 200+ a day.');
  await scrollDetail(page, 'Subject', 1800); await wait(3400);

  await go(page, 'Today');
  caption('Today: the replies and interviews waiting on you. That part is yours.');
  await wait(4200);

  await go(page, 'Calendar');
  caption('Calendar: apply-by dates, events and every follow-up, exportable as .ics.');
  await wait(4200);
  caption(null);
  await wait(300);
  const video = page.video();
  await context.close();
  await browser.close();
  const raw = await video.path();
  fs.renameSync(raw, path.join(OUT, 'walkthrough-raw.webm'));
  fs.writeFileSync(path.join(OUT, 'captions.json'), JSON.stringify(captions, null, 1));
  console.log('recorded', captions.length, 'captions,', now().toFixed(1), 's');
})();
