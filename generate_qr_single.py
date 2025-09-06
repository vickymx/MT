# Generate one QR code for the GitHub Pages site
import qrcode, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "qr"
OUT.mkdir(exist_ok=True)

SITE_URL = "https://vickymx.github.io/Multilingua/"  # your GitHub Pages root

if __name__ == "__main__":
    img = qrcode.make(SITE_URL)
    out = OUT / "qr_multilingual.png"
    img.save(out)
    print("Saved QR:", out)
    print("Scan to open:", SITE_URL)
