"""Build both PDF products: 7-Day Launch Checklist (8p) & Faceless Business Marketing Playbook (23p)."""
from common import ROOT, Renderer, doc, write_html
from doc_base import PAGE_CSS
import product_checklist
import product_playbook

OUT = ROOT / "products"


def build(r: Renderer) -> list[tuple[str, dict]]:
    results = []
    # Product 1: Checklist
    html_1 = doc("".join(product_checklist.pages()), PAGE_CSS, "7-Day Digital Product Launch Checklist")
    p1 = write_html("product_checklist.html", html_1)
    out1 = OUT / "7_Day_Digital_Product_Launch_Checklist.pdf"
    rep1 = r.pdf(p1, out1)
    results.append((out1.name, rep1))

    # Product 2: Playbook
    html_2 = doc("".join(product_playbook.pages()), PAGE_CSS, "Faceless Business Marketing Playbook")
    p2 = write_html("product_playbook.html", html_2)
    out2 = OUT / "Faceless_Business_Marketing_Playbook.pdf"
    rep2 = r.pdf(p2, out2)
    results.append((out2.name, rep2))

    return results

