"""Build the Wilson Conveyancing concept site (no dependencies).

    python3 _build/pages.py && python3 _build/fonts.py

English at /, Traditional Chinese (Hong Kong) at /zh/. Every string is written as L(english, chinese).
"""
import datetime
import os
import urllib.parse

BUILD = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BUILD)
V = "3"  # cache-bust: bump on every CSS/JS change
LANG = "en"


def L(en, zh):
    return en if LANG == "en" else zh


# ------------------------------------------------------------------ facts (source: wilsonconveyancing.com, Nov 2026)
PHONE = "+44 7830 315714"
TEL = "+447830315714"
WA = "447830315714"
LICENCE = "13589"
OFFICIAL = "https://www.wilsonconveyancing.com/"
TRUSTPILOT = "https://uk.trustpilot.com/review/wilsonconveyancing.com"
GFORM = "https://docs.google.com/forms/d/e/1FAIpQLSc4QtbSvw-BhrDXk7WS0zhD2-UsG5Y28SyGAZ3gGmLEoxiXWg/viewform"
UXC = "https://ux-circles.com/professionals"
BASE = "https://uxcircles.github.io/wilsonconveyancing/"

# The firm's own mark (house + heart, one vermilion line), redrawn as SVG so it scales.
HOUSE_D = ("M5 103 L120 7 L235 103 M34 79 V205 Q34 218 47 218 H193 Q206 218 206 205 V79 "
           "M120 196 C72 162 60 132 74 113 C88 95 110 99 120 117 C130 99 152 95 166 113 C180 132 168 162 120 196 Z")


def house(cls="house", label=None):
    a = f'role="img" aria-label="{label}"' if label else 'aria-hidden="true"'
    return f'<svg class="{cls}" viewBox="0 0 240 225" {a}><path d="{HOUSE_D}"/></svg>'


# ------------------------------------------------------------------ the seven stages (their own list, FAQ page)
# weeks after the offer is accepted: indicative, from their own "8 to 12 weeks" answer
STAGES = [
    (0, 1, "Property information and title review", "業權審查",
     "A detailed look at the title and legal documents to confirm ownership and spot problems early.",
     "細閱業權及法律文件，確認誰是業主，及早發現問題。"),
    (1, 4, "Property searches", "物業查冊",
     "Searches with the local authority and other bodies: planning, roads, drainage, environmental risks.",
     "向地方政府及有關機構查冊：規劃、道路、排水、環境風險。"),
    (2, 6, "Mortgage conveyancing", "按揭手續",
     "Working with your lender on the legal side of the mortgage offer and its registration.",
     "與銀行處理按揭批核後的法律手續及登記。"),
    (5, 8, "Signing contracts", "簽署合約",
     "Contracts prepared and checked so every term is clear before you sign.",
     "準備及核對合約，確保每項條款清楚，才請你簽名。"),
    (7, 10, "Exchanging contracts", "交換合約",
     "The moment it becomes legally binding for buyer and seller. The completion date is fixed here.",
     "買賣雙方從此受法律約束，成交日期亦在此時訂定。"),
    (8, 12, "Completion", "成交，拎鎖匙",
     "Funds move, ownership passes and you collect the keys.",
     "款項過戶、業權轉移，你可以拎鎖匙。"),
    (12, 16, "Post-completion", "成交後手續",
     "Stamp Duty paid where due and the property registered with HM Land Registry.",
     "如需繳付印花稅會代為處理，並在英國土地註冊處登記業權。"),
]

TODAY = datetime.date.today()


def fmt(d, short=False):
    if LANG == "en":
        return f"{d.day} {d.strftime('%b' if short else '%B')}"
    return f"{d.month}月{d.day}日"


def rng(a, b):
    da, db = TODAY + datetime.timedelta(weeks=a), TODAY + datetime.timedelta(weeks=b)
    return L(f"{fmt(da, True)} – {fmt(db, True)}", f"{fmt(da)} 至 {fmt(db)}")


def get_services():
  return [
    ("buy", L("Buying and selling", "買賣物業"), [
        L("Buying and selling property", "買樓及賣樓"),
        L("Freehold properties", "永久業權物業（Freehold）"),
        L("Leasehold properties", "租賃業權物業（Leasehold）"),
        L("New-build property", "新樓（New-build）"),
        L("Auction property", "拍賣物業"),
        L("Buy-to-let investments", "買樓收租"),
    ]),
    ("money", L("Mortgages and money", "按揭及資金"), [
        L("Mortgaging and remortgaging", "按揭及轉按"),
        L("Gifted deposits", "親友贈予首期"),
        L("Help to Buy", "Help to Buy 置業援助"),
        L("Shared ownership transactions", "共有業權（Shared Ownership）"),
        L("Right to Buy", "Right to Buy 優先購買權"),
    ]),
    ("owners", L("Changing who owns it", "更改業權"), [
        L("Transfer of equity", "業權轉讓（加名或除名）"),
        L("Matrimonial transfers of ownership", "婚姻或離婚後的業權轉移"),
    ]),
    ("lease", L("Leases and freeholds", "租約及地權"), [
        L("Lease extensions", "延長租約（Lease Extension）"),
        L("Freehold ground rent services", "永久業權地租服務"),
    ]),
]

def get_why():
  return [
    (L("Your lawyer, not an assistant", "直接同律師傾，不經助理"),
     L("You have direct contact with the lawyer handling your case, so you can ask and get answers without being passed along.",
       "由開始到成交，你都直接聯絡負責你個案的律師，問題唔使經人轉達。")),
    (L("Updates before you ask", "未問先報進度"),
     L("You hear about each stage as it happens, not after you chase.", "每一步有進展都會主動通知你，唔使你追。")),
    (L("Fixed, clear fees", "收費清楚，定額報價"),
     L("A written estimate of fees and disbursements before you start, with no hidden charges.",
       "開始之前先給你書面報價，列明律師費及代支費用，沒有隱藏收費。")),
    (L("Chains, gifts and mortgages", "連環交易、贈款、按揭"),
     L("Experience with property chains, gifted deposits, money from abroad and lender requirements.",
       "熟悉連環買賣、親友贈予首期、海外匯款及銀行按揭要求。")),
]

# Reviews: transcribed from the screenshots Wilson Conveyancing publishes on its own homepage (Trustpilot)
REVIEWS = [
    ("Professional and trustworthy", "4 January 2025",
     "He is very professional during the whole transaction process and gives quick and useful responses to our questions. very polite and patient to explain details where we had concerns. smooth and trustworthy in the process."),
    ("As a first time buyer", "19 October 2023",
     "As a first time buyer. Wilson gave me lots of help with very clear guidance and every procedures, keeping me update of the progress. He work according to schedule and the deal is completed within the timeline. […] The process would be difficult and complicated as I am in overseas, but Wilson helped made it easy and worry free."),
    ("Made my right choice", "22 May 2024",
     "We just bought our first property in the UK few months ago. […] Wilson worked with all parties in a timely manner. We never expected the house purchase could be completed within 3 months! (considering it was with chains)"),
    ("Wilson provided clear and professional…", "13 January 2025",
     "Wilson provided clear and professional support throughout our house purchase. He was efficient, responsive, and made the process straightforward. I would recommend his services."),
]

def get_faqs():
  return [
    (L("What is the conveyancing process?", "物業轉讓（Conveyancing）有甚麼步驟？"),
     L("<p>Conveyancing is the legal process of transferring property ownership from one party to another. It has seven stages, and each one matters:</p>",
       "<p>物業轉讓是把物業業權由一方轉給另一方的法律程序，共有七個步驟，每一步都重要：</p>")
     + "<ol class='faq-steps'>" + "".join(f"<li><strong>{L(s[2], s[3])}</strong> {L(s[4], s[5])}</li>" for s in STAGES) + "</ol>"),
    (L("How long does conveyancing take?", "辦理物業轉讓要幾耐？"),
     L("<p>Typically 8 to 12 weeks from the time an offer is accepted until completion. It can vary with:</p><ul>"
       "<li><strong>How complex it is.</strong> Leasehold properties or titles with unresolved issues may take longer.</li>"
       "<li><strong>Searches and enquiries.</strong> Delays can happen if more searches or answers are needed.</li>"
       "<li><strong>The mortgage.</strong> Getting and processing a mortgage offer affects the timeline.</li>"
       "<li><strong>The chain.</strong> If another sale in the chain is delayed, your completion date may move.</li></ul>"
       "<p>We keep you informed at every stage and work to deal with problems as soon as they appear.</p>",
       "<p>一般由 offer 獲接受到成交，大約需要 8 至 12 星期，視乎：</p><ul>"
       "<li><strong>交易有幾複雜：</strong>Leasehold 物業或業權有未解決問題，可能需時較長。</li>"
       "<li><strong>查冊及查詢：</strong>如要加查或等對方回覆，會有延誤。</li>"
       "<li><strong>按揭：</strong>銀行批核及處理按揭需時。</li>"
       "<li><strong>連環交易：</strong>鏈中其他買賣有延誤，你的成交日期亦可能受影響。</li></ul>"
       "<p>每個階段我們都會通知你，一有問題即時處理。</p>")),
    (L("How can a conveyancer help me?", "物業轉讓律師可以幫我做甚麼？"),
     L("<ul><li><strong>Legal documents:</strong> drafting, reviewing and managing contracts.</li>"
       "<li><strong>Property searches:</strong> finding issues such as planning restrictions or disputes.</li>"
       "<li><strong>Advice:</strong> explaining legal terms and answering your questions throughout.</li>"
       "<li><strong>Funds:</strong> moving deposits, mortgage money and final payments securely.</li>"
       "<li><strong>Third parties:</strong> dealing with lenders, estate agents and the other side’s lawyers for you.</li>"
       "<li><strong>Registration:</strong> registering your ownership with HM Land Registry after completion.</li></ul>",
       "<ul><li><strong>法律文件：</strong>草擬、審閱及管理合約。</li>"
       "<li><strong>物業查冊：</strong>找出規劃限制、糾紛等問題。</li>"
       "<li><strong>專業意見：</strong>解釋法律用語，隨時解答你的問題。</li>"
       "<li><strong>資金：</strong>安全處理訂金、按揭款項及餘款。</li>"
       "<li><strong>聯絡各方：</strong>代你與銀行、地產代理及對方律師溝通。</li>"
       "<li><strong>登記業權：</strong>成交後在英國土地註冊處登記你的業權。</li></ul>")),
    (L("Must I use a local solicitor for conveyancing?", "一定要用物業所在地的律師嗎？"),
     L("<p>No. Most conveyancing can be handled remotely, by email, phone and online, so you can work with a lawyer anywhere in England and Wales, or from abroad. What matters most is the lawyer’s experience with your kind of transaction.</p>",
       "<p>不用。大部分手續都可以透過電郵、電話及網上處理，所以你可以委託英格蘭及威爾斯任何地方的律師，人在海外都得。最重要是律師熟悉你這類交易。</p>")),
    (L("Can conveyancing fees be negotiated?", "律師費可以傾嗎？"),
     L("<p>Our fees are fully transparent, with no hidden charges. If you have questions about your quote, we’re happy to go through a detailed breakdown with you and look for ways to save.</p>",
       "<p>我們的收費完全透明，沒有隱藏收費。對報價有疑問，我們樂意逐項同你講解，一起看看有沒有可以慳的地方。</p>")),
    (L("Why use Wilson Conveyancing?", "點解揀 Wilson Conveyancing？"),
     "<ul>" + "".join(f"<li><strong>{t}.</strong> {d}</li>" if LANG == "en" else f"<li><strong>{t}：</strong>{d}</li>" for t, d in get_why()) + "</ul>"),
]


# ------------------------------------------------------------------ shared pieces
PFX = ""  # prefix to site root (assets)
SLUG = ""


def wa_link(msg):
    return f"https://wa.me/{WA}?text=" + urllib.parse.quote(msg)


def alt_url(slug):
    s = "" if slug == "index.html" else slug
    return (BASE + "zh/" + s) if LANG == "en" else (BASE + s)


def head(title, desc):
    s = "" if SLUG == "index.html" else SLUG
    return f'''<!doctype html>
<html lang="{L('en-GB', 'zh-Hant-HK')}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="alternate" hreflang="en" href="{BASE}{s}">
<link rel="alternate" hreflang="zh-Hant" href="{BASE}zh/{s}">
<link rel="icon" type="image/png" href="{PFX}assets/img/favicon.png">
<link rel="apple-touch-icon" href="{PFX}assets/img/apple-touch-icon.png">
<meta name="theme-color" content="#0e0d0c">
<link rel="preload" href="{PFX}assets/fonts/sora.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{PFX}assets/fonts/onest.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{PFX}assets/site.css?v={V}">
<script defer src="{PFX}assets/site.js?v={V}"></script>
</head>
'''


def nav_items():
    return [
        ("services.html", L("Services", "服務")),
        ("stamp-duty.html", L("Stamp Duty", "印花稅")),
        ("faqs.html", L("FAQs", "常見問題")),
        ("index.html#quote", L("Free quote", "免費報價")),
    ]


def switch():
    s = "" if SLUG in ("index.html", "404.html") else SLUG
    href = (PFX + "zh/" + s) if LANG == "en" else (PFX + s)
    if not href:
        href = "./"
    return f'<a class="lang" href="{href}" lang="{L("zh-Hant", "en")}" hreflang="{L("zh-Hant", "en")}">{L("中文", "English")}</a>'


def pg(h):
    """Link to a page in the current language."""
    base = PFX + ("zh/" if LANG == "zh" else "")
    if h.startswith("index.html"):
        h = h.replace("index.html", "") or ""
        return (base or "./") + h if h else (base or "./")
    return base + h


def header():
    links = "".join(
        f'<a href="{pg(h)}"{" aria-current=page" if h == SLUG else ""}>{t}</a>' for h, t in nav_items())
    return f'''<body>
<a class="skip" href="#main">{L("Skip to content", "跳至內容")}</a>
<div class="concept-bar" role="note">
  <div class="wrap concept-inner">
    <p><span class="concept-tag">{L("Concept", "概念")}</span><span class="concept-long">{L('Redesign concept. Not the <a href="' + OFFICIAL + '" target="_blank" rel="noopener">official Wilson Conveyancing website</a>.', '網站改版概念設計，並非 <a href="' + OFFICIAL + '" target="_blank" rel="noopener">Wilson Conveyancing 官方網站</a>。')}</span></p>
    <a href="{UXC}" target="_blank" rel="noopener"><span class="concept-by">Designed by </span><strong>UX CIRCLES</strong> <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9"/></svg></a>
  </div>
</div>
<header class="site-head">
  <div class="wrap head-in">
    <a class="brand" href="{pg('index.html')}" aria-label="{L('Wilson Conveyancing, home', 'Wilson Conveyancing 首頁')}">
      {house("brand-mark")}
      <span class="brand-name">Wilson<br>Conveyancing</span>
    </a>
    <nav class="nav" aria-label="{L('Main', '主選單')}">{links}</nav>
    {switch()}
    <a class="head-call" href="tel:{TEL}">{PHONE}</a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="menu">{L('Menu', '選單')}</button>
  </div>
  <div class="menu" id="menu" hidden>
    <nav class="wrap" aria-label="{L('Menu', '選單')}">
      {links}
      <a href="tel:{TEL}">{L('Call', '致電')} {PHONE}</a>
      <a href="{wa_link(L('Hello Wilson, I have a conveyancing question.', '你好 Wilson，我想查詢物業轉讓。'))}">WhatsApp</a>
      {switch()}
    </nav>
  </div>
</header>
'''


def mbar():
    return f'''<nav class="mbar" aria-label="{L('Quick actions', '快捷操作')}">
  <a href="tel:{TEL}">{L('Call', '致電')}</a>
  <a href="{wa_link(L('Hello Wilson, I have a conveyancing question.', '你好 Wilson，我想查詢物業轉讓。'))}">WhatsApp</a>
  <a href="{pg('index.html#quote')}">{L('Free quote', '免費報價')}</a>
</nav>'''


def footer():
    return f'''<footer class="foot">
  <div class="wrap foot-grid">
    <div class="foot-brand">
      {house("foot-mark")}
      <p class="foot-name">Wilson Conveyancing</p>
      <p>{L('CLC Licensed Conveyancing Lawyer', 'CLC 持牌物業轉讓律師')}<br>{L('Licence number', '牌照號碼')} {LICENCE} · {L('England and Wales', '英格蘭及威爾斯')}</p>
    </div>
    <div>
      <p><a href="tel:{TEL}">{PHONE}</a><br>{L('Phone and WhatsApp', '電話及 WhatsApp')}</p>
      <p>{L('Monday to Friday, 9:30 to 17:00', '星期一至五 上午 9:30 至下午 5:00')}<br><span class="open-now" data-open></span></p>
      <p><a href="{TRUSTPILOT}" target="_blank" rel="noopener">{L('Reviews on Trustpilot', 'Trustpilot 評語')} ↗</a></p>
    </div>
    <div>
      <p><a href="{pg('services.html')}">{L('Services', '服務')}</a> · <a href="{pg('stamp-duty.html')}">{L('Stamp Duty', '印花稅')}</a> · <a href="{pg('faqs.html')}">{L('FAQs', '常見問題')}</a></p>
      <p><a href="{pg('privacy.html')}">{L('Privacy and accessibility', '私隱及無障礙')}</a> · {switch()}</p>
      <p class="small">{L('Calculators on this site give estimates, not legal or tax advice.', '本網站的計算工具只提供估算，並非法律或稅務意見。')}</p>
      <p class="small">{L('Unofficial redesign concept by', '非官方概念設計：')} <a href="{UXC}" target="_blank" rel="noopener">UX CIRCLES</a></p>
    </div>
  </div>
</footer>
{mbar()}
</body>
</html>
'''


def write(slug, title, desc, body):
    global PFX, SLUG
    SLUG = slug
    PFX = "../" if LANG == "zh" else ""
    if slug == "404.html":
        PFX = "/wilsonconveyancing/"
    html = head(title, desc) + header() + f'<main id="main">\n{body()}\n</main>\n' + footer()
    out = os.path.join(ROOT, "zh" if LANG == "zh" else "", slug)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(html)


# ------------------------------------------------------------------ pages
def track():
    items = []
    for i, (a, b, en, zh, den, dzh) in enumerate(STAGES):
        key = " is-keys" if i == 5 else ""
        items.append(f'''<li class="stop{key}" data-from="{a}" data-to="{b}">
        <span class="stop-n">{i + 1}</span>
        <span class="stop-name">{L(en, zh)}</span>
        <time class="stop-date" data-range>{rng(a, b)}</time>
      </li>''')
    return "\n      ".join(items)


def home():
    k1 = TODAY + datetime.timedelta(weeks=8)
    k2 = TODAY + datetime.timedelta(weeks=12)
    reviews = "".join(f'''<figure class="review">
        <div class="stars" role="img" aria-label="{L('5 out of 5 stars', '5 星（滿分 5 星）')}">★★★★★</div>
        <blockquote lang="en"><p class="review-t">{t}</p><p>{q}</p></blockquote>
        <figcaption>Trustpilot · {d}</figcaption>
      </figure>''' for t, d, q in REVIEWS)
    svc = "".join(f'''<div class="svc-group">
        <h3>{g}</h3>
        <ul>{"".join(f"<li>{x}</li>" for x in items)}</ul>
      </div>''' for _, g, items in get_services())
    why = "".join(f'<li><h3>{t}</h3><p>{d}</p></li>' for t, d in get_why())
    return f'''<section class="hero" aria-labelledby="h1">
  <div class="wrap">
    <p class="licence">{L(f'CLC Licensed Conveyancing Lawyer · Licence {LICENCE} · England and Wales', f'CLC 持牌物業轉讓律師 · 牌照 {LICENCE} · 英格蘭及威爾斯')}</p>
    <h1 id="h1"><span data-h1a>{L('Offer accepted today?', '今日 offer 獲接受')}</span><br><span class="h1-2">{L('Keys between <span data-k1>' + fmt(k1) + '</span> and <span data-k2>' + fmt(k2) + '</span>', '<span data-k1>' + fmt(k1) + '</span>至<span data-k2>' + fmt(k2) + '</span>拎鎖匙')}</span></h1>
    <div class="hero-act">
      <a class="btn btn-red" href="#quote">{L('Get a free quote', '索取免費報價')}</a>
      <a class="btn btn-line" href="{wa_link(L('Hello Wilson, my offer has been accepted and I need a conveyancer.', '你好 Wilson，我的 offer 已獲接受，想委託你辦理物業轉讓。'))}">WhatsApp {PHONE}</a>
      <p class="open-now" data-open></p>
    </div>
    <form class="when" data-when onsubmit="return false">
      <label for="offer">{L('Offer accepted on', 'Offer 獲接受日期')}</label>
      <input id="offer" name="offer" type="date" value="{TODAY.isoformat()}">
      <p class="when-note">{L('Dates follow Wilson’s usual 8 to 12 weeks. Leasehold, long chains and mortgage offers can move them.', '日期按一般 8 至 12 星期估算。Leasehold、連環交易及按揭批核都可能令時間有變。')}</p>
    </form>
    <ol class="track" aria-label="{L('The seven stages, with estimated dates', '七個步驟及預計日期')}">
      <li class="stop is-today"><span class="stop-n" aria-hidden="true"></span><span class="stop-name">{L('Offer accepted', 'Offer 獲接受')}</span><time class="stop-date" data-today>{fmt(TODAY, True) if LANG == 'en' else fmt(TODAY)}</time></li>
      {track()}
      <li class="stop is-home">{house("track-house")}<span class="sr">{L('Your new home', '你的新居')}</span></li>
    </ol>
  </div>
</section>

<section class="why" aria-labelledby="why-h">
  <div class="wrap why-in">
    <h2 id="why-h">{L('From the first call to completion, you deal with Wilson', '由第一個電話到成交，都係 Wilson 親自跟進')}</h2>
    <ul class="why-list">{why}</ul>
  </div>
</section>

<section class="svc" aria-labelledby="svc-h">
  <div class="wrap">
    <div class="sec-head">
      <h2 id="svc-h">{L('What Wilson handles', 'Wilson 處理的物業手續')}</h2>
      <a class="more" href="{pg('services.html')}">{L('All services and fees', '全部服務及收費')} →</a>
    </div>
    <div class="svc-grid">{svc}</div>
  </div>
</section>

<section class="abroad" aria-labelledby="abroad-h">
  <div class="wrap abroad-in">
    <div>
      <h2 id="abroad-h">{L('Buying from Hong Kong, or anywhere outside the UK', '人在香港或海外，一樣可以喺英國買樓')}</h2>
      <p>{L('You don’t need a local solicitor, or to be in England, for most of the process. Documents, questions and updates go by email, phone and WhatsApp.', '大部分手續都唔需要你身在英國，亦唔一定要搵當地律師。文件、查詢同進度都可以經電郵、電話及 WhatsApp 處理。')}</p>
      <ul class="ticks">
        <li>{L('Gifted deposits and money sent from abroad: what lenders and the law ask to see', '親友贈予首期及海外匯款：銀行及法例要求的證明文件')}</li>
        <li>{L('The 2% Stamp Duty surcharge for non-UK residents, and when it can be claimed back', '非英國居民 2% 印花稅附加費，以及何時可以申請退回')}</li>
        <li>{L('First homes in the UK, with every step explained', '第一次喺英國置業，每一步都同你講清楚')}</li>
      </ul>
      <a class="btn btn-ink" href="{pg('stamp-duty.html')}">{L('Work out your Stamp Duty', '計算你的印花稅')}</a>
    </div>
  </div>
</section>

<section class="reviews" aria-labelledby="rev-h">
  <div class="wrap">
    <div class="sec-head">
      <h2 id="rev-h">{L('Rated Excellent, 4.9 on Trustpilot', 'Trustpilot 評分 4.9，「Excellent」')}</h2>
      <a class="more" href="{TRUSTPILOT}" target="_blank" rel="noopener">{L('Read every review', '閱讀全部評語')} ↗</a>
    </div>
    {'' if LANG == 'en' else '<p class="rev-note">評語保留客戶英文原文。</p>'}
    <div class="rev-grid">{reviews}</div>
  </div>
</section>

{quote_form()}
'''


def quote_form():
    needs = [("buy", L("Buying", "買樓")), ("sell", L("Selling", "賣樓")), ("both", L("Buying and selling", "賣舊買新")),
             ("remortgage", L("Remortgage", "轉按")), ("equity", L("Transfer of equity", "加名或除名")), ("other", L("Something else", "其他"))]
    flags = [("leasehold", L("Leasehold", "Leasehold 物業")), ("newbuild", L("New build", "新樓")), ("mortgage", L("With a mortgage", "需要按揭")),
             ("ftb", L("First-time buyer", "首次置業")), ("gift", L("Gifted deposit", "親友贈予首期")), ("abroad", L("I live outside the UK", "我住在英國以外")),
             ("shared", L("Shared ownership", "共有業權"))]
    radios = "".join(f'<label class="pill"><input type="radio" name="need" value="{v}"{" checked" if i == 0 else ""}><span>{t}</span></label>' for i, (v, t) in enumerate(needs))
    checks = "".join(f'<label class="pill"><input type="checkbox" name="flag" value="{v}"><span>{t}</span></label>' for v, t in flags)
    return f'''<section class="quote" id="quote" aria-labelledby="quote-h">
  <div class="wrap quote-in">
    <div class="quote-intro">
      <h2 id="quote-h">{L('Free, no-obligation estimate of fees and disbursements', '免費報價：律師費及代支費用，不收分毫，不用承諾')}</h2>
      <p>{L('Tell Wilson about the property. The answers open as a WhatsApp message you can check before sending.', '填寫物業資料，答案會變成一段 WhatsApp 訊息，你可以先檢查再發送。')}</p>
      <p class="small">{L('Nothing is stored on this website.', '本網站不會儲存任何資料。')} {L('Prefer the current form?', '想用現有表格？')} <a href="{GFORM}" target="_blank" rel="noopener">{L('Open it on Google Forms', '在 Google Forms 開啟')} ↗</a></p>
    </div>
    <form class="qform" data-quote novalidate>
      <fieldset><legend>{L('What do you need?', '你需要甚麼服務？')}</legend><div class="pills">{radios}</div></fieldset>
      <div class="row2">
        <label><span>{L('Property price', '樓價')}</span><span class="money"><span aria-hidden="true">£</span><input name="price" inputmode="numeric" autocomplete="off" placeholder="350,000"></span></label>
        <label><span>{L('Town or postcode', '物業所在城市或郵區')} <span class="opt">{L('optional', '可不填')}</span></span><input name="where" autocomplete="off"></label>
      </div>
      <fieldset><legend>{L('Anything that applies', '適用的情況（可多選）')}</legend><div class="pills">{checks}</div></fieldset>
      <div class="row2">
        <label>{L('Your name', '你的名字')}<input name="name" autocomplete="name" required></label>
        <label>{L('Phone or email', '電話或電郵')}<input name="contact" autocomplete="email" required></label>
      </div>
      <label><span>{L('Anything else', '其他補充')} <span class="opt">{L('optional', '可不填')}</span></span><textarea name="note" rows="3"></textarea></label>
      <p class="form-err" data-err role="alert" hidden>{L('Please add your name and a phone number or email.', '請填寫名字及電話或電郵。')}</p>
      <button class="btn btn-red" type="submit">{L('Send on WhatsApp', '經 WhatsApp 發送')}</button>
    </form>
  </div>
</section>'''


def services():
    blocks = "".join(f'''<section class="svc-block" id="{k}">
      <h2>{g}</h2>
      <ul>{"".join(f"<li>{x}</li>" for x in items)}</ul>
    </section>''' for k, g, items in get_services())
    return f'''<section class="page-head">
  <div class="wrap">
    <h1>{L('Services and fees', '服務及收費')}</h1>
    <p class="lede">{L('Residential conveyancing across England and Wales. Every case starts with a free, written estimate of fees and disbursements, so you know the cost before anything begins.', '英格蘭及威爾斯住宅物業轉讓。每個個案都先提供免費書面報價，列明律師費及代支費用，開始之前已清楚成本。')}</p>
  </div>
</section>
<div class="wrap svc-page">
  {blocks}
  <section class="svc-block fees" id="fees">
    <h2>{L('What a quote covers', '報價包括甚麼')}</h2>
    <dl class="fee-list">
      <div><dt>{L('Legal fee', '律師費')}</dt><dd>{L('Wilson’s fixed fee for the work, agreed before you start.', 'Wilson 處理你個案的定額收費，開始前講好。')}</dd></div>
      <div><dt>{L('Disbursements', '代支費用')}</dt><dd>{L('Costs paid to others on your behalf, such as property searches and the HM Land Registry fee.', '代你支付給第三方的費用，例如物業查冊費及英國土地註冊處登記費。')}</dd></div>
      <div><dt>{L('Stamp Duty', '印花稅')}</dt><dd>{L('Paid to HMRC if due. <a href="stamp-duty.html">Estimate it here</a>.', '如需繳付，交給英國稅局。<a href="stamp-duty.html">在此估算</a>。')}</dd></div>
    </dl>
    <p class="small">{L('Exact figures depend on the property and the lender, so the estimate is written for your case. Wilson Conveyancing does not publish a price list.', '實際金額視乎物業及按揭銀行，所以報價按你的個案計算。Wilson Conveyancing 沒有公開價目表。')}</p>
  </section>
</div>
{quote_form()}
'''


def stamp_duty():
    return f'''<section class="page-head">
  <div class="wrap">
    <h1>{L('Stamp Duty calculator', '印花稅計算機')}</h1>
    <p class="lede">{L('Residential Stamp Duty Land Tax in England, at the rates in force since 1 April 2025. Includes first-time buyer relief, the 5% higher rates for additional homes and the 2% non-resident surcharge.', '英格蘭住宅物業印花稅（SDLT），按 2025 年 4 月 1 日起生效的稅率計算，包括首次置業寬減、額外物業 5% 附加及非居民 2% 附加費。')}</p>
  </div>
</section>
<section class="calc-sec">
  <div class="wrap calc-in">
    <form class="calc" data-sdlt onsubmit="return false">
      <label for="sd-price">{L('Purchase price', '樓價')}</label>
      <span class="money big"><span aria-hidden="true">£</span><input id="sd-price" name="price" inputmode="numeric" autocomplete="off" value="350,000"></span>
      <fieldset><legend>{L('After buying, you will own', '買入後，你會擁有')}</legend><div class="pills">
        <label class="pill"><input type="radio" name="type" value="ftb"><span>{L('My first home ever', '首次置業')}</span></label>
        <label class="pill"><input type="radio" name="type" value="home" checked><span>{L('Only this home', '只有這一個物業')}</span></label>
        <label class="pill"><input type="radio" name="type" value="add"><span>{L('More than one home', '多於一個物業')}</span></label>
      </div></fieldset>
      <label class="pill"><input type="checkbox" name="nonres"><span>{L('I am not UK resident', '我不是英國居民')}</span></label>
    </form>
    <div class="calc-out" aria-live="polite">
      <p class="calc-k">{L('Estimated Stamp Duty', '估算印花稅')}</p>
      <p class="calc-total" data-total>£0</p>
      <p class="calc-eff" data-eff></p>
      <table class="bands"><thead><tr><th>{L('Band', '樓價區間')}</th><th>{L('Rate', '稅率')}</th><th>{L('Tax', '稅款')}</th></tr></thead><tbody data-rows></tbody></table>
      <div class="calc-notes" data-notes></div>
      <a class="btn btn-red" data-wa-sdlt href="{wa_link(L('Hello Wilson, could you check my Stamp Duty?', '你好 Wilson，想請你確認我的印花稅。'))}">{L('Ask Wilson to check it', '請 Wilson 確認')}</a>
    </div>
  </div>
  <div class="wrap">
    <p class="small calc-foot">{L('An estimate, not advice. Rates checked against GOV.UK in November 2026. Property in Wales pays Land Transaction Tax instead, which this calculator does not cover. Reliefs, mixed-use and properties over £500,000 bought through a company follow other rules.', '只供估算，並非專業意見。稅率已於 2026 年 11 月按 GOV.UK 核對。威爾斯物業須繳付 Land Transaction Tax，本計算機並不適用。各類寬減、商住兩用物業，以及經公司購買超過 £500,000 的物業另有規則。')}</p>
  </div>
</section>
'''


def faqs():
    items = "".join(f'''<details class="faq"{" open" if i == 0 else ""}>
      <summary><h2>{q}</h2></summary>
      <div class="faq-a">{a}</div>
    </details>''' for i, (q, a) in enumerate(get_faqs()))
    return f'''<section class="page-head">
  <div class="wrap">
    <h1>{L('Frequently asked questions', '常見問題')}</h1>
  </div>
</section>
<div class="wrap faq-list">{items}</div>
<section class="cta-band">
  <div class="wrap cta-in">
    <h2>{L('Still wondering about your case?', '仲有問題想問？')}</h2>
    <a class="btn btn-red" href="{wa_link(L('Hello Wilson, I have a conveyancing question.', '你好 Wilson，我想查詢物業轉讓。'))}">{L('WhatsApp Wilson', 'WhatsApp Wilson')}</a>
    <a class="btn btn-line" href="tel:{TEL}">{PHONE}</a>
  </div>
</section>
'''


def privacy():
    return f'''<section class="page-head">
  <div class="wrap">
    <h1>{L('Privacy and accessibility', '私隱及無障礙')}</h1>
    <p class="lede">{L('Draft for Wilson Conveyancing to review before use.', '草稿，需經 Wilson Conveyancing 審閱後方可使用。')}</p>
  </div>
</section>
<div class="wrap prose">
  <h2>{L('What this website collects', '本網站收集甚麼資料')}</h2>
  <p>{L('Nothing. The quote form and calculators run in your browser. When you press “Send on WhatsApp”, your answers open in WhatsApp and you choose whether to send them. There are no cookies, analytics or tracking scripts.', '不收集任何資料。報價表格及計算機只在你的瀏覽器內運作。按下「經 WhatsApp 發送」後，答案會在 WhatsApp 打開，由你決定是否發送。本網站不使用 cookies、分析或追蹤程式。')}</p>
  <h2>{L('When you contact Wilson Conveyancing', '當你聯絡 Wilson Conveyancing')}</h2>
  <p>{L('Messages, calls and documents you send are used to give you a quote and, if you instruct us, to act on your property transaction, including identity and anti-money-laundering checks required by law. They are kept for as long as the law and our regulator, the Council for Licensed Conveyancers, require. You can ask to see, correct or delete your information, and complain to the Information Commissioner’s Office (ico.org.uk).', '你發送的訊息、通話及文件，只用作報價；如你委託我們，亦用於處理你的物業交易，包括法例要求的身份及反洗錢核查。資料按法例及監管機構 Council for Licensed Conveyancers 的要求保存。你可要求查閱、更正或刪除資料，亦可向英國資訊專員辦公室（ico.org.uk）投訴。')}</p>
  <h2>{L('Accessibility', '無障礙')}</h2>
  <p>{L('This site aims to meet WCAG 2.2 AA: it works with a keyboard and screen readers, respects reduced-motion settings and keeps text contrast high. If something doesn’t work for you, call or WhatsApp', '本網站以 WCAG 2.2 AA 為目標：支援鍵盤及螢幕閱讀器，尊重減少動畫設定，並保持文字對比清晰。如有任何部分不方便使用，請致電或 WhatsApp')} <a href="tel:{TEL}">{PHONE}</a>.</p>
</div>
'''


def notfound():
    return f'''<section class="lost">
  <div class="wrap lost-in">
    <svg class="lost-line" viewBox="0 0 600 120" aria-hidden="true"><path d="M0 60 H250 M330 60 H600"/><circle cx="250" cy="60" r="7"/><circle cx="330" cy="60" r="7"/></svg>
    <h1>{L('This page fell out of the chain', '呢一頁甩咗鏈')}</h1>
    <p>{L('The link is broken or the page has moved.', '連結已失效，或頁面已搬走。')}</p>
    <a class="btn btn-red" href="{PFX}">{L('Back to the home page', '返回首頁')}</a>
    <a class="btn btn-line" href="{PFX}zh/">中文首頁</a>
  </div>
</section>
'''


def build():
    global LANG
    for LANG in ("en", "zh"):
        write("index.html", L("Wilson Conveyancing · CLC licensed conveyancing lawyer", "Wilson Conveyancing · CLC 持牌物業轉讓律師"),
              L("Conveyancing for buyers and sellers in England and Wales, with direct access to your lawyer. Free estimate of fees and disbursements.",
                "英格蘭及威爾斯物業轉讓，直接聯絡負責律師。免費報價。"), home)
        write("services.html", L("Services and fees · Wilson Conveyancing", "服務及收費 · Wilson Conveyancing"),
              L("Buying, selling, remortgage, transfer of equity, leasehold, shared ownership and more.", "買賣物業、轉按、加名除名、Leasehold、共有業權等。"), services)
        write("stamp-duty.html", L("Stamp Duty calculator · Wilson Conveyancing", "印花稅計算機 · Wilson Conveyancing"),
              L("Estimate Stamp Duty in England, including first-time buyer relief and the non-resident surcharge.", "估算英格蘭印花稅，包括首次置業寬減及非居民附加費。"), stamp_duty)
        write("faqs.html", L("FAQs · Wilson Conveyancing", "常見問題 · Wilson Conveyancing"),
              L("How conveyancing works, how long it takes and how fees are set.", "物業轉讓的步驟、所需時間及收費。"), faqs)
        write("privacy.html", L("Privacy and accessibility · Wilson Conveyancing", "私隱及無障礙 · Wilson Conveyancing"),
              L("Privacy notice and accessibility statement.", "私隱聲明及無障礙聲明。"), privacy)
    LANG = "en"
    write("404.html", "Page not found · Wilson Conveyancing", "Page not found.", notfound)
    open(os.path.join(ROOT, "robots.txt"), "w").write("User-agent: *\nDisallow: /\n")
    open(os.path.join(ROOT, ".nojekyll"), "w").write("")
    print("built", TODAY)


if __name__ == "__main__":
    build()
