"""Build the profile's original SVG artwork. Python standard library only."""
from html import escape
from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent / 'assets'
BG = '#0b1220'
INK = '#edf5f5'
MUTED = '#9aafbe'
TEAL = '#65e1c6'
BLUE = '#8cb8ff'
PURPLE = '#b9a6ff'
FONT = 'Inter,Segoe UI,Arial,sans-serif'
MONO = 'ui-monospace,SFMono-Regular,Consolas,monospace'


def text(x, y, content, size=16, fill=INK, weight=400, extra=''):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-weight="{weight}" {extra}>{escape(content)}</text>'


def svg(filename, width, height, title, body, css=''):
    ASSETS.mkdir(exist_ok=True)
    (ASSETS / filename).write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title>
<desc id="desc">Original artwork for Ridjan Xhika's GitHub profile. Animations respect reduced-motion preferences.</desc>
<style>
text {{ font-family: {FONT}; }}
.mono {{ font-family: {MONO}; }}
{css}
@media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} }}
</style>
{body}
</svg>\n''')


def hero():
    stars = ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{TEAL}" opacity=".35"/>'
                    for x, y, r in [(580,46,1),(883,64,2),(622,250,1),(855,260,1),(522,292,1),(680,34,2),(922,200,1),(550,143,1)])
    svg('hero.svg', 960, 340, 'Ridjan Xhika — software, security and systems', f'''
<defs>
  <linearGradient id="background" x2="1" y2="1"><stop stop-color="#0e1929"/><stop offset="1" stop-color="#0b1220"/></linearGradient>
  <radialGradient id="halo"><stop stop-color="#3cbcaf" stop-opacity=".2"/><stop offset="1" stop-color="#3cbcaf" stop-opacity="0"/></radialGradient>
  <linearGradient id="orb" x2="1" y2="1"><stop stop-color="#236c76"/><stop offset=".6" stop-color="#122a40"/><stop offset="1" stop-color="#251c46"/></linearGradient>
  <linearGradient id="border"><stop stop-color="#65e1c6"/><stop offset="1" stop-color="#9aabff"/></linearGradient>
  <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="#8cb8ff" stroke-opacity=".035"/></pattern>
  <clipPath id="frame"><rect x="1" y="1" width="958" height="338" rx="24"/></clipPath>
</defs>
<rect x="1" y="1" width="958" height="338" rx="24" fill="url(#background)" stroke="#24364a"/>
<g clip-path="url(#frame)"><rect width="960" height="340" fill="url(#grid)"/>
<circle cx="757" cy="166" r="211" fill="url(#halo)"/>{stars}
<path d="M532 340V300H568V318H596V284H624V303H647V271H668V302H702V286H738V316H764V279H795V295H825V258H840V276H858V304H884V287H918V267H942V298H960V340Z" fill="#142638" opacity=".8"/>
<path d="M590 314H609M636 324H655M717 314H729M803 319H818M876 330H885M928 292H935" stroke="#65e1c6" stroke-opacity=".28" stroke-width="3"/>
<g class="float">
  <circle cx="754" cy="165" r="119" fill="none" stroke="#314a61" stroke-dasharray="2 10"/>
  <g class="orbit"><ellipse cx="754" cy="165" rx="143" ry="60" fill="none" stroke="#719ec0" stroke-opacity=".45" transform="rotate(-28 754 165)"/><circle cx="881" cy="103" r="4" fill="{TEAL}"/></g>
  <circle cx="754" cy="165" r="86" fill="url(#orb)" stroke="url(#border)" stroke-width="1.5"/>
  <circle cx="754" cy="165" r="75" fill="none" stroke="#bddbdc" stroke-opacity=".09"/>
  {text(754,185,'RX',55,INK,750,'text-anchor="middle" letter-spacing="-3"')}
  <path d="M725 203H783" stroke="{TEAL}" stroke-width="2" stroke-linecap="round"/>
  <circle cx="675" cy="198" r="5" fill="{TEAL}" class="pulse"/>
</g>
</g>
<rect x="42" y="42" width="6" height="6" rx="2" fill="{TEAL}"/>
{text(60,49,'SOFTWARE / SECURITY / SYSTEMS',11,TEAL,600,'class="mono" letter-spacing="1.5"')}
{text(42,131,'RIDJAN',67,INK,800,'letter-spacing="-2"')}
{text(42,201,'XHIKA',67,INK,800,'letter-spacing="-2"')}
{text(44,245,'Curious about how it works.',20,'#b2c6d3')}
{text(44,274,'Driven to build something useful.',20,'#b2c6d3')}
{text(44,311,'EPITECH STUDENT  ·  LINUX ENTHUSIAST',10,'#6f899c',500,'class="mono" letter-spacing="1"')}
<rect x="891" y="291" width="29" height="2" rx="1" fill="{TEAL}" class="blink"/>
''', '''
.float { animation: drift 8s ease-in-out infinite; }
.orbit { transform-origin: 754px 165px; animation: orbit 45s linear infinite; }
.pulse { animation: pulse 3.5s ease-in-out infinite; }
.blink { animation: blink 2s steps(2,end) infinite; }
@keyframes drift { 50% { transform: translateY(-7px); } }
@keyframes orbit { to { transform: rotate(360deg); } }
@keyframes pulse { 50% { opacity:.35; } }
@keyframes blink { 50% { opacity:0; } }
''')


def project_card(filename, number, name, category, lines, tags, accent, art, css=''):
    body = f'''<defs><linearGradient id="surface" x2="1" y2="1"><stop stop-color="#111e2f"/><stop offset="1" stop-color="{BG}"/></linearGradient></defs>
<rect x="1" y="1" width="466" height="212" rx="17" fill="url(#surface)" stroke="#26364b"/>
<path d="M24 26H48" stroke="{accent}" stroke-width="3" stroke-linecap="round"/>
{text(24,53,category,10,accent,600,'class="mono" letter-spacing="1.2"')}
{text(24,91,name,29,INK,700)}
{text(24,126,lines[0],14,MUTED)}
{text(24,148,lines[1],14,MUTED)}
<path d="M24 169H444" stroke="#223347"/>
{text(24,192,tags,11,accent,500,'class="mono"')}
{text(425,192,'↗',19,accent)}
<g transform="translate(365 32)">{art}</g>'''
    svg(filename, 468, 214, f'{name} — {" ".join(lines)}', body, css)


def projects():
    waveform = ''.join(f'<rect class="wave w{i}" x="{i*9}" y="{25-height/2}" width="4" height="{height}" rx="2" fill="{TEAL}"/>'
                       for i,height in enumerate([13,27,42,55,36,21,11]))
    project_card('project-jki.svg', '01', 'JKI / Jake', '01 — DESKTOP COMPANION',
                 ['A voice for your Linux desktop.', 'Wake word, local speech, real actions.'],
                 'PYTHON · GTK · CODEX', TEAL, waveform,
                 ''.join(f'.w{i} {{ transform-origin: {i*9+2}px 25px; animation: wave {1.1+i*.14}s ease-in-out infinite; }}' for i in range(7))+
                 '@keyframes wave { 50% { transform:scaleY(.3);opacity:.6; } }')
    pixels = ''.join(f'<rect class="pixel" x="{(i%4)*13}" y="{(i//4)*13}" width="10" height="10" rx="2" fill="{[PURPLE,TEAL,BLUE][i%3]}" opacity="{.25+(i%4)*.2}" style="animation-delay:-{i*.25}s"/>' for i in range(16))
    project_card('project-mygimp.svg', '02', 'MyGimp', '02 — CREATIVE TOOLS',
                 ['A GPU-powered pixel editor in Rust.', 'Draw, paint and turn pixels into ideas.'],
                 'RUST · WGPU · WINIT', PURPLE, pixels,
                 '.pixel { animation:pixel 4s ease-in-out infinite; } @keyframes pixel { 50% { opacity:.2; } }')
    radar = f'<circle cx="28" cy="26" r="26" fill="none" stroke="{BLUE}" opacity=".3"/><circle cx="28" cy="26" r="15" fill="none" stroke="{BLUE}" opacity=".3"/><g class="sweep"><path d="M28 26V0" stroke="{BLUE}" stroke-width="2"/><path d="M28 26L5 13A26 26 0 0 1 28 0Z" fill="{BLUE}" opacity=".15"/></g><circle cx="42" cy="15" r="3" fill="{BLUE}"/>'
    project_card('project-eagleeye.svg', '03', 'EagleEye', '03 — SECURITY RESEARCH',
                 ['Exploring networks through C.', 'An educational security project.'],
                 'C · NETWORKS · RESEARCH', BLUE, radar,
                 '.sweep { transform-origin:28px 26px; animation:sweep 6s linear infinite; } @keyframes sweep { to { transform:rotate(360deg); } }')
    window = f'<rect width="62" height="49" rx="6" fill="none" stroke="{TEAL}" opacity=".65"/><path d="M0 13H62" stroke="{TEAL}" opacity=".4"/><circle cx="8" cy="7" r="1.5" fill="{TEAL}"/><circle cx="14" cy="7" r="1.5" fill="{TEAL}"/><path d="M17 24L11 30L17 36M44 24L50 30L44 36M34 22L27 38" fill="none" stroke="{TEAL}" stroke-width="2" stroke-linecap="round"/>'
    project_card('project-portfolio.svg', '04', 'Portfolio', '04 — AROUND THE WEB',
                 ['More about me and the things I build.', 'A place to explore beyond the README.'],
                 'WEB · PROJECTS · ABOUT', TEAL, window)


def toolkit(columns=4):
    tools = [('C','Systems programming'),('Rust','Graphics & native tools'),('Python','Automation & voice'),('JavaScript','Web applications'),('TypeScript','Typed web development'),('Linux','My everyday environment'),('Git','Version control'),('GTK','Desktop interfaces')]
    body=''
    for i,(name,description) in enumerate(tools):
        x=(i%columns)*242
        y=(i//columns)*91
        body += f'<rect x="{x+1}" y="{y+1}" width="232" height="81" rx="12" fill="{BG}" stroke="#253649"/>'
        body += f'<rect x="{x+16}" y="{y+19}" width="3" height="19" rx="1.5" fill="{TEAL if i%2==0 else BLUE}"/>'
        body += text(x+28,y+35,name,17,INK,600)
        body += text(x+17,y+61,description,11,MUTED)
    filename='toolkit.svg' if columns==4 else 'toolkit-mobile.svg'
    svg(filename,columns*242-8,(len(tools)//columns)*91-9,
        'Toolkit: C, Rust, Python, JavaScript, TypeScript, Linux, Git and GTK',body)


def spotify():
    bars=''.join(f'<rect class="bar b{i}" x="{680+i*11}" y="{113-h}" width="5" height="{h}" rx="2" fill="#1ed760" opacity=".8"/>' for i,h in enumerate([17,29,22,47,33,61,45,29,39,20,32,13]))
    svg('spotify.svg',960,224,'Coding soundtrack — Best of Anime Now 2025, curated by Spotify. Open playlist on Spotify.',f'''
<defs>
<linearGradient id="music" x2="1" y2=".4"><stop stop-color="#101e26"/><stop offset="1" stop-color="#0b1821"/></linearGradient>
<linearGradient id="sleeve" x2="1" y2="1"><stop stop-color="#36567c"/><stop offset=".5" stop-color="#222c53"/><stop offset="1" stop-color="#487a7a"/></linearGradient>
<clipPath id="cover"><rect x="24" y="24" width="176" height="176" rx="12"/></clipPath>
</defs>
<rect x="1" y="1" width="958" height="222" rx="20" fill="url(#music)" stroke="#284334"/>
<g clip-path="url(#cover)">
<rect x="24" y="24" width="176" height="176" fill="url(#sleeve)"/>
<circle cx="144" cy="69" r="28" fill="#e4f2ca" opacity=".85"/>
<circle cx="153" cy="59" r="27" fill="#303d63"/>
<path d="M24 177V144H45V164H63V124H79V140H90V110H114V154H128V135H150V161H161V119H178V144H200V200H24Z" fill="#101d32"/>
<path d="M66 145H73M98 130H105M98 140H105M166 139H174M167 151H174" stroke="#83d6c7" stroke-width="2" opacity=".7"/>
<path class="star" d="M47 71L87 45" stroke="#c6eaff" stroke-width="1.5" stroke-linecap="round"/>
{text(38,189,'AFTER HOURS',10,INK,600,'class="mono" letter-spacing="1.4"')}
</g>
<circle cx="235" cy="39" r="4" fill="#1ed760"/>
{text(249,43,'THE CODING SOUNDTRACK',11,'#8ce7a6',600,'class="mono" letter-spacing="1"')}
{text(231,87,'Anime on repeat.',31,INK,700)}
{text(232,115,'Best of Anime Now 2025',18,'#c0d2d7')}
{text(232,140,'A featured playlist, curated by Spotify.',13,MUTED)}
<rect x="232" y="162" width="165" height="34" rx="17" fill="#1ed760"/>
<path d="M248 173L248 185L258 179Z" fill="#0b2012"/>
{text(268,184,'Open on Spotify',12,'#0b2012',650)}
{bars}
<circle cx="890" cy="178" r="21" fill="none" stroke="#638d79" stroke-opacity=".45"/>
<path d="M883 178H897M891 172L897 178L891 184" fill="none" stroke="#96cba7" stroke-width="1.5" stroke-linecap="round"/>
''',''.join(f'.b{i} {{ transform-origin:{682+i*11}px 113px; animation:level {1.3+i*.13}s ease-in-out infinite; }}' for i in range(12))+'''
@keyframes level { 50% { transform:scaleY(.35);opacity:.45; } }
.star { animation:shoot 9s ease-in-out infinite; }
@keyframes shoot { 0%,70%,100% { opacity:0;transform:translate(0,0); } 75% { opacity:.8; } 90% { opacity:0;transform:translate(72px,45px); } }
''')


def footer():
    svg('footer.svg',960,88,'Thanks for stopping by. Keep building. Keep learning.',f'''
<path d="M0 1H960" stroke="#294554"/>
{text(0,38,'KEEP BUILDING. KEEP LEARNING.',13,TEAL,600,'class="mono" letter-spacing="1.4"')}
{text(0,65,'Thanks for stopping by — Ridjan',13,MUTED)}
<g fill="{TEAL}"><circle cx="908" cy="48" r="3" opacity=".3"/><circle cx="925" cy="48" r="3" opacity=".6"/><circle cx="942" cy="48" r="3" class="pulse"/></g>
''','.pulse { animation:pulse 3s ease-in-out infinite; } @keyframes pulse { 50% { opacity:.3; } }')


if __name__ == '__main__':
    hero()
    projects()
    toolkit()
    toolkit(columns=2)
    spotify()
    footer()
    print('Built 9 profile SVGs.')
