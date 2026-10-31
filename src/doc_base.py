"""Shared paged-document styles + helpers for the PDF products (US Letter, 816x1056 CSS px)."""
from common import BRAND, handle, monogram_svg
from covers import COVER_CSS

PAGE_CSS = COVER_CSS + """
@page{size:8.5in 11in;margin:0}
html,body{background:#0B0D10}
.page{width:816px;height:1056px;position:relative;overflow:hidden;page-break-after:always;break-after:page;
  background:var(--white);color:var(--obsidian);display:flex;flex-direction:column;padding:62px 70px 0}
.page:last-child{page-break-after:auto}
.page.cover{padding:0;font-size:16px}
.page.dark{background:var(--obsidian);color:var(--white)}
.content{flex:1;min-height:0;overflow:hidden;padding-bottom:6px}
.folio{height:64px;flex:none;display:flex;align-items:center;justify-content:space-between;border-top:1px solid rgba(11,13,16,.12);
  font-size:9.5px;letter-spacing:.22em;text-transform:uppercase;color:rgba(11,13,16,.5);font-weight:600}
.dark .folio{border-top-color:rgba(247,245,240,.12);color:rgba(247,245,240,.45)}
.folio .pn{font-family:var(--serif);font-size:14px;letter-spacing:0;color:var(--gold);font-weight:700}
.eyebrow{font-size:11px;font-weight:700;letter-spacing:.3em;text-transform:uppercase;color:rgba(11,13,16,.7);display:flex;align-items:center;gap:10px;margin-bottom:12px}
.dark .eyebrow{color:var(--gold)}
.eyebrow:before{content:"";width:28px;height:2px;background:var(--gold)}
h2{font-family:var(--serif);font-size:34px;line-height:1.1;font-weight:700;letter-spacing:-.005em;margin-bottom:12px}
h2 em{font-style:italic;color:var(--obsidian);font-weight:600;background:linear-gradient(transparent 62%,rgba(229,184,75,.55) 62%)}
.dark h2 em{color:var(--gold);background:none}
h3{font-size:15px;font-weight:800;margin:18px 0 8px;letter-spacing:.005em}
h4{font-size:10.5px;font-weight:800;letter-spacing:.2em;text-transform:uppercase;color:rgba(11,13,16,.55);margin:14px 0 6px}
.dark h4{color:rgba(247,245,240,.5)}
p{font-size:13.2px;line-height:1.58;margin-bottom:9px}
.lede{font-size:15.5px;line-height:1.55;color:rgba(11,13,16,.75);margin-bottom:14px}
.dark .lede{color:rgba(247,245,240,.75)}
b,strong{font-weight:700}
ul.check{list-style:none;margin:6px 0 10px}
ul.check li{position:relative;padding:7px 0 7px 32px;font-size:13px;line-height:1.45;border-bottom:1px dashed rgba(11,13,16,.13)}
ul.check li:before{content:"";position:absolute;left:0;top:8px;width:16px;height:16px;border:2px solid var(--gold);border-radius:3px;background:transparent}
ul.check li b{font-weight:700}
ul.dots{margin:4px 0 10px 18px}
ul.dots li{font-size:13px;line-height:1.5;margin-bottom:5px}
ul.dots li::marker{color:var(--gold)}
ol.num{list-style:none;counter-reset:n;margin:6px 0 10px}
ol.num li{counter-increment:n;position:relative;padding:6px 0 6px 38px;font-size:13px;line-height:1.5}
ol.num li:before{content:counter(n,decimal-leading-zero);position:absolute;left:0;top:5px;font-family:var(--serif);font-weight:700;color:var(--gold);font-size:15px}
.callout{background:rgba(229,184,75,.12);border-left:4px solid var(--gold);padding:14px 18px;border-radius:0 8px 8px 0;margin:12px 0;font-size:13px;line-height:1.55}
.callout b{color:var(--obsidian)}
.callout.green{background:rgba(16,185,129,.10);border-left-color:var(--emerald)}
.box{background:var(--obsidian);color:var(--white);border-radius:12px;padding:18px 22px;margin:12px 0}
.box p,.box li{color:rgba(247,245,240,.85)}
.box h3{margin-top:0;color:var(--gold)}
.dark .box{background:var(--card)}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.grid3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px}
.cell{border:1px solid rgba(11,13,16,.12);border-radius:10px;padding:14px 16px;background:rgba(11,13,16,.025)}
.dark .cell{background:var(--card);border-color:rgba(247,245,240,.08)}
.cell h3{margin-top:0}
.cell p{font-size:12.4px;margin-bottom:4px}
table.t{width:100%;border-collapse:collapse;margin:10px 0 12px;font-size:12px}
table.t th{background:var(--obsidian);color:var(--gold);text-align:left;font-size:9.5px;letter-spacing:.16em;text-transform:uppercase;padding:9px 10px;font-weight:700}
table.t td{padding:8px 10px;border-bottom:1px solid rgba(11,13,16,.1);vertical-align:top;line-height:1.4}
table.t tr:nth-child(even) td{background:rgba(229,184,75,.06)}
table.t td.num{font-variant-numeric:tabular-nums;font-weight:700;text-align:right;white-space:nowrap}
table.t tr.total td{font-weight:800;border-top:2px solid var(--obsidian);background:rgba(16,185,129,.10)}
.dark table.t td{border-bottom-color:rgba(247,245,240,.1)}
.dark table.t tr:nth-child(even) td{background:rgba(247,245,240,.03)}
.g{color:var(--emerald);font-weight:700} .dark .g{color:var(--emerald)}
.gold{color:var(--gold)} .dark .gold{color:var(--gold)}
.stat{border-top:3px solid var(--gold);padding-top:10px}
.stat b{display:block;font-family:var(--serif);font-size:30px;line-height:1.05;color:var(--obsidian)}
.dark .stat b{color:var(--white)}
.stat span{font-size:11.5px;color:rgba(11,13,16,.6);line-height:1.4;display:block;margin-top:4px}
.dark .stat span{color:rgba(247,245,240,.6)}
.script{background:rgba(11,13,16,.035);border:1px solid rgba(11,13,16,.12);border-radius:14px 14px 14px 4px;padding:12px 16px;font-size:12.6px;line-height:1.55;margin:8px 0}
.script .who{font-size:9.5px;font-weight:800;letter-spacing:.2em;text-transform:uppercase;color:var(--gold);margin-bottom:4px}
.dayhead{display:flex;align-items:center;gap:18px;margin-bottom:14px}
.dayhead .d{flex:none;width:78px;height:78px;border-radius:14px;background:var(--obsidian);color:var(--gold);display:flex;flex-direction:column;align-items:center;justify-content:center;font-family:var(--serif);font-size:34px;font-weight:700;line-height:1}
.dayhead .d small{font-family:var(--sans);font-size:9px;letter-spacing:.25em;color:rgba(247,245,240,.6);margin-bottom:4px;font-weight:700}
.dayhead h2{margin:0}
.dayhead .meta{font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:rgba(11,13,16,.5);font-weight:700;margin-top:6px}
.secnum{font-family:var(--serif);font-size:150px;line-height:.9;color:var(--gold);font-weight:700}
.toc{list-style:none;margin-top:10px}
.toc li{display:flex;align-items:baseline;gap:12px;padding:12px 0;border-bottom:1px solid rgba(11,13,16,.1);font-size:15px}
.toc li b{font-family:var(--serif);color:var(--gold);font-size:18px;width:34px}
.toc li span.dots{flex:1;border-bottom:1px dotted rgba(11,13,16,.25);transform:translateY(-4px)}
.toc li i{font-style:normal;font-weight:700;font-variant-numeric:tabular-nums}
.flowrow{display:flex;align-items:stretch;gap:0;margin:12px 0}
.flowrow div{flex:1;background:var(--obsidian);color:var(--white);padding:12px 10px;font-size:11.5px;line-height:1.35;text-align:center;position:relative;margin-right:14px;border-radius:8px}
.flowrow div b{display:block;color:var(--gold);font-size:10px;letter-spacing:.15em;text-transform:uppercase;margin-bottom:4px}
.flowrow div:after{content:"";position:absolute;right:-12px;top:50%;margin-top:-6px;border:6px solid transparent;border-left:8px solid var(--gold)}
.flowrow div:last-child{margin-right:0;background:var(--emerald);color:var(--obsidian)}
.flowrow div:last-child b{color:var(--obsidian)}
.flowrow div:last-child:after{display:none}
.small{font-size:11.5px;color:rgba(11,13,16,.6);line-height:1.5}
.dark .small{color:rgba(247,245,240,.55)}
.sig{display:flex;align-items:center;gap:14px;margin-top:16px}
"""


def page(content: str, n: int, label: str, dark: bool = False, total: int | None = None) -> str:
    cls = "page dark" if dark else "page"
    return (f'<section class="{cls}"><div class="content">{content}</div>'
            f'<div class="folio"><span>{BRAND["brand_name"]} · {label}</span><span>{handle()}</span>'
            f'<span class="pn">{n:02d}</span></div></section>')


def cover_page(cover_html: str) -> str:
    return f'<section class="page cover">{cover_html}</section>'


def mark(size=46, bg=None):
    return monogram_svg(size, 24, bg=bg)


