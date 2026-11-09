"""Repo banner (1280x640), rendered by headless Chrome. python3 banner.py -> banner.png"""
import pathlib, subprocess
HERE = pathlib.Path(__file__).parent
STEPS = ["8–10 ideas", "Structural", "Economic", "Competitive", "One to build"]
FLOW = ' <b>→</b> '.join(f"<span>{s}</span>" for s in STEPS)
banner = f"""<!doctype html><html><head><meta charset=utf-8>
<link rel=stylesheet href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;600;700&display=block"><style>
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1280px;height:640px;background:#f6f4f0;color:#171614;font-family:'Hanken Grotesk',sans-serif;overflow:hidden}}
.wrap{{padding:84px 80px}}
h1{{font-size:120px;font-weight:600;letter-spacing:-0.045em;line-height:.92}}
p{{font-size:36px;line-height:1.3;margin-top:28px;max-width:1000px;letter-spacing:-0.01em}}
.flow{{display:flex;align-items:center;gap:18px;margin-top:40px}}
.flow span{{font-size:30px;font-weight:600}}.flow span:last-child{{background:#ffe14a;padding:2px 8px}}
.flow b{{font-size:30px;font-weight:400;color:#8a857c}}
.bar{{position:absolute;left:80px;bottom:72px;background:#ffe14a;padding:18px 26px;font-size:30px;font-weight:600}}
.bar i{{font-style:normal;font-weight:400}}
</style></head><body><div class=wrap>
<h1>Venture Screen</h1>
<p>A Claude Code skill that screens business ideas in minutes and ends with one worth building.</p>
<div class=flow>{FLOW}</div>
</div><div class=bar>Installs in 1 minute <i>· free and open source</i></div></body></html>"""

src = HERE / "banner.html"; src.write_text(banner)
subprocess.run(["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", "--headless=new", "--hide-scrollbars",
                "--force-device-scale-factor=1", "--window-size=1280,640", "--virtual-time-budget=8000",
                f"--screenshot={HERE / 'banner.png'}", src.as_uri()], check=True, capture_output=True)
src.unlink()
print(HERE / "banner.png")
