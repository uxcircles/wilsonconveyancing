/* Wilson Conveyancing concept: menu, live dates, opening hours, quote form, Stamp Duty. */
(() => {
  document.documentElement.classList.add('js');
  const zh = document.documentElement.lang.startsWith('zh');
  const T = (en, z) => (zh ? z : en);
  const WA = '447830315714';
  const gbp = (n) => '£' + Math.round(n).toLocaleString('en-GB');
  const MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  const MONTH = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
  const fmt = (d, short) => (zh ? `${d.getMonth() + 1}月${d.getDate()}日` : `${d.getDate()} ${(short ? MON : MONTH)[d.getMonth()]}`);
  const addWeeks = (d, w) => { const x = new Date(d); x.setDate(x.getDate() + w * 7); return x; };

  /* ---------- menu ---------- */
  const btn = document.querySelector('.menu-btn');
  const menu = document.getElementById('menu');
  if (btn && menu) {
    const set = (open) => {
      btn.setAttribute('aria-expanded', open);
      menu.hidden = !open;
      document.body.classList.toggle('menu-open', open);
      btn.textContent = open ? T('Close', '關閉') : T('Menu', '選單');
    };
    btn.addEventListener('click', () => set(menu.hidden));
    menu.addEventListener('click', (e) => { if (e.target.closest('a')) set(false); });
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && !menu.hidden) { set(false); btn.focus(); } });
    window.matchMedia('(min-width: 1081px)').addEventListener('change', (m) => { if (m.matches) set(false); });
  }

  /* ---------- opening hours, in London time: Mon–Fri 9:30–17:00 ---------- */
  const london = () => {
    const p = Object.fromEntries(new Intl.DateTimeFormat('en-GB', { timeZone: 'Europe/London', weekday: 'short', hour: '2-digit', minute: '2-digit', hourCycle: 'h23' })
      .formatToParts(new Date()).map((x) => [x.type, x.value]));
    return { day: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'].indexOf(p.weekday), mins: +p.hour * 60 + +p.minute };
  };
  const status = () => {
    const { day, mins } = london();
    const weekday = day >= 1 && day <= 5;
    if (weekday && mins >= 570 && mins < 1020) return ['open', T('Open now, until 17:00 UK time', '現正辦公，英國時間下午 5:00 前')];
    let next;
    if (weekday && mins < 570) next = T('today at 9:30', '今日上午 9:30');
    else if (day >= 1 && day <= 4) next = T('tomorrow at 9:30', '明日上午 9:30');
    else next = T('Monday at 9:30', '星期一上午 9:30');
    return ['closed', T(`Closed now. Opens ${next} UK time. WhatsApp any time`, `現已休息，英國時間${next}再辦公，WhatsApp 可隨時留言`)];
  };
  document.querySelectorAll('[data-open]').forEach((el) => { const [s, t] = status(); el.dataset.state = s; el.textContent = t; });

  /* ---------- the calendar: every date follows the offer date ---------- */
  const when = document.querySelector('[data-when]');
  const track = document.querySelector('.track');
  const draw = () => {
    const input = when && when.elements.offer;
    const start = input && input.value ? new Date(input.value + 'T12:00:00') : new Date();
    const k1 = document.querySelector('[data-k1]');
    const k2 = document.querySelector('[data-k2]');
    if (k1) k1.textContent = fmt(addWeeks(start, 8));
    if (k2) k2.textContent = fmt(addWeeks(start, 12));
    const today = document.querySelector('[data-today]');
    if (today) today.textContent = fmt(start, true);
    const h1a = document.querySelector('[data-h1a]');
    const isToday = start.toDateString() === new Date().toDateString();
    if (h1a) h1a.textContent = isToday ? T('Offer accepted today?', '今日 offer 獲接受') : T(`Offer accepted on ${fmt(start)}?`, `${fmt(start)} offer 獲接受`);
    document.querySelectorAll('.track [data-range]').forEach((el) => {
      const li = el.closest('li');
      const a = addWeeks(start, +li.dataset.from);
      const b = addWeeks(start, +li.dataset.to);
      el.textContent = zh ? `${fmt(a)} 至 ${fmt(b)}` : `${fmt(a, true)} – ${fmt(b, true)}`;
    });
  };
  if (when) {
    const iso = (d) => `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
    when.elements.offer.value = iso(new Date());
    when.addEventListener('input', draw);
    draw();
  }
  if (track) {
    if ('IntersectionObserver' in window) {
      const io = new IntersectionObserver((es) => es.forEach((e) => { if (e.isIntersecting) { track.classList.add('drawn'); io.disconnect(); } }), { threshold: 0.2 });
      io.observe(track);
    } else track.classList.add('drawn');
  }

  /* ---------- money inputs: keep digits, show commas ---------- */
  const money = (input, cb) => input.addEventListener('input', () => {
    const digits = input.value.replace(/\D/g, '').slice(0, 9);
    input.value = digits ? Number(digits).toLocaleString('en-GB') : '';
    if (cb) cb();
  });
  const num = (v) => Number(String(v).replace(/[^\d]/g, '')) || 0;

  /* ---------- quote form → WhatsApp ---------- */
  document.querySelectorAll('[data-quote]').forEach((form) => {
    money(form.elements.price);
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = form.elements.name.value.trim();
      const contact = form.elements.contact.value.trim();
      const err = form.querySelector('[data-err]');
      if (!name || !contact) {
        err.hidden = false;
        (name ? form.elements.contact : form.elements.name).focus();
        return;
      }
      err.hidden = true;
      const label = (inp) => inp.closest('label').querySelector('span').textContent;
      const need = label(form.querySelector('input[name=need]:checked'));
      const flags = [...form.querySelectorAll('input[name=flag]:checked')].map(label);
      const price = num(form.elements.price.value);
      const lines = [
        T('Hello Wilson, I would like a conveyancing quote.', '你好 Wilson，我想索取物業轉讓報價。'),
        `${T('Service', '服務')}: ${need}`,
        price ? `${T('Price', '樓價')}: ${gbp(price)}` : '',
        form.elements.where.value.trim() ? `${T('Property in', '物業位置')}: ${form.elements.where.value.trim()}` : '',
        flags.length ? `${T('Details', '情況')}: ${flags.join(', ')}` : '',
        form.elements.note.value.trim() ? `${T('Note', '補充')}: ${form.elements.note.value.trim()}` : '',
        `${T('Name', '名字')}: ${name}`,
        `${T('Contact', '聯絡')}: ${contact}`,
      ].filter(Boolean);
      window.open(`https://wa.me/${WA}?text=${encodeURIComponent(lines.join('\n'))}`, '_blank', 'noopener');
    });
  });

  /* ---------- Stamp Duty (England, residential, rates from 1 April 2025) ---------- */
  const STD = [[125000, 0], [250000, 0.02], [925000, 0.05], [1500000, 0.10], [Infinity, 0.12]];
  const FTB = [[300000, 0], [500000, 0.05]];
  const band = (lo, hi) => (hi === Infinity ? T(`Over ${gbp(lo)}`, `${gbp(lo)} 以上`) : `${gbp(lo === 0 ? 0 : lo + 1)} – ${gbp(hi)}`);
  function sdlt(price, type, nonres) {
    const notes = [];
    let bands = STD;
    let extra = 0;
    if (type === 'ftb') {
      if (price <= 500000) bands = FTB;
      else notes.push(T('Over £500,000 there is no first-time buyer relief, so standard rates apply.', '樓價超過 £500,000，不能使用首次置業寬減，須按一般稅率計算。'));
    }
    if (type === 'add') {
      if (price >= 40000) {
        extra += 0.05;
        notes.push(T('Includes the 5% higher rates for additional homes. If this replaces your main home and you sell the old one within 36 months, you can usually claim the 5% back.', '已包括額外物業 5% 附加。如新物業取代你的主要住所，並在 36 個月內賣出舊居，一般可申請退回這 5%。'));
      } else notes.push(T('Under £40,000 the higher rates do not apply.', '樓價低於 £40,000，不須付額外物業附加。'));
    }
    if (nonres) {
      extra += 0.02;
      notes.push(T('Includes the 2% non-resident surcharge. If you spend 183 days in the UK in a 365-day period around the purchase, you can usually claim it back.', '已包括非居民 2% 附加費。如在購買前後的 365 日內在英國住滿 183 日，一般可申請退回。'));
    }
    if (type !== 'add') notes.push(T('A home you own in Hong Kong or anywhere else in the world counts. Still own one? Choose “More than one home”.', '在香港或世界其他地方擁有的物業也會計算在內。如仍持有，請選「多於一個物業」。'));
    const rows = [];
    let lo = 0;
    let total = 0;
    for (const [hi, r] of bands) {
      if (price <= lo) break;
      const rate = r + extra;
      const tax = (Math.min(price, hi) - lo) * rate;
      total += tax;
      rows.push([band(lo, hi), (Math.round(rate * 1000) / 10) + '%', tax]);
      lo = hi;
    }
    return { rows, total: Math.floor(total), notes };
  }
  document.querySelectorAll('[data-sdlt]').forEach((form) => {
    const out = document.querySelector('.calc-out');
    const run = () => {
      const price = num(form.elements.price.value);
      const type = form.elements.type.value;
      const nonres = form.elements.nonres.checked;
      const r = sdlt(price, type, nonres);
      out.querySelector('[data-total]').textContent = gbp(r.total);
      out.querySelector('[data-eff]').textContent = price ? T(`${(r.total / price * 100).toFixed(2)}% of ${gbp(price)}`, `相當於樓價 ${gbp(price)} 的 ${(r.total / price * 100).toFixed(2)}%`) : T('Enter a price', '請輸入樓價');
      out.querySelector('[data-rows]').innerHTML = r.rows.map(([b, rate, tax]) => `<tr><td>${b}</td><td>${rate}</td><td>${gbp(tax)}</td></tr>`).join('');
      out.querySelector('[data-notes]').innerHTML = r.notes.map((n) => `<p>${n}</p>`).join('');
      const own = { ftb: T('My first home ever', '首次置業'), home: T('Only this home', '只有這一個物業'), add: T('More than one home', '多於一個物業') }[type];
      const msg = T(
        `Hello Wilson, could you check my Stamp Duty?\nPrice: ${gbp(price)}\nAfter buying I will own: ${own}\nNon-UK resident: ${nonres ? 'Yes' : 'No'}\nWebsite estimate: ${gbp(r.total)}`,
        `你好 Wilson，想請你確認我的印花稅：\n樓價：${gbp(price)}\n買入後：${own}\n非英國居民：${nonres ? '是' : '否'}\n網站估算：${gbp(r.total)}`);
      out.querySelector('[data-wa-sdlt]').href = `https://wa.me/${WA}?text=${encodeURIComponent(msg)}`;
    };
    money(form.elements.price, run);
    form.addEventListener('change', run);
    run();
  });
})();
