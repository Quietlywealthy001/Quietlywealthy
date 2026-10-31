"""Render everything (Sprint 1 + Sprint 2). Usage: python src/render_all.py [brand] [carousel] [stories] [products]"""
import sys
import time

from common import Renderer


def main(targets):
    t0 = time.time()
    with Renderer() as r:
        if "brand" in targets:
            import brand_kit
            for p in brand_kit.build(r):
                print("  ✓", p)
        if "carousel" in targets:
            import carousel
            for p in carousel.build(r):
                print("  ✓", p)
        if "stories" in targets:
            import highlight_stories
            for p in highlight_stories.build(r):
                print("  ✓", p)
        if "products" in targets:
            import products
            for name, rep in products.build(r):
                status = "OK" if not rep["overflows"] else f"OVERFLOW {rep['overflows']}"
                print(f"  ✓ {name}: {rep['pages']} pages — {status}")
    print(f"Done in {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main(sys.argv[1:] or ["brand", "carousel", "stories", "products"])

