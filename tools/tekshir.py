#!/usr/bin/env python3
"""Kurs sayti uchun avtomatik tekshiruvlar. Ishga tushirish: python3 tools/tekshir.py"""
import re, glob, os, sys
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
LESSONS = sorted(glob.glob('lessons/*.html'))
ALL = LESSONS + ['index.html', 'reference/glossary.html',
                 'reference/kod-varaqasi.html', 'reference/yol-xaritasi.html']
fail = []
def bad(m): fail.append(m); print('❌', m)

# 1) Kirill harflari o'zbekcha matnga aralashib ketmasin
for f in ALL:
    s = open(f).read()
    for m in re.finditer(r'[Ѐ-ӿԀ-ԯ]+', s):
        bad(f"KIRILL {f}: {m.group(0)!r} … {' '.join(s[max(0,m.start()-45):m.end()+25].split())}")

# 2) Quiz: variantlar so'z soni teng + aynan bitta to'g'ri javob
nq = 0
for f in LESSONS:
    s = open(f).read()
    for q in re.finditer(r'<ul class="quiz-options">(.*?)</ul>', s, re.S):
        btns = re.findall(r'<button\s+([^>]*)>(.*?)</button>', q.group(1), re.S)
        wc = [len(re.sub(r'<[^>]+>', '', t).split()) for _, t in btns]
        nq += 1
        if len(set(wc)) != 1:
            bad(f"QUIZ so'z soni {f}: {wc} → {[re.sub(r'<[^>]+>','',t).strip() for _,t in btns]}")
        if sum(1 for a, _ in btns if 'data-correct' in a) != 1:
            bad(f"QUIZ to'g'ri javob soni {f}: {q.group(1)[:60]!r}")
print(f'✔ {nq} quiz bloki')

# 3) Ichki havolalar mavjudmi (kod bloklari hisobga olinmaydi — ular matn)
nl = 0
for f in ALL:
    # kod/misol bloklari matn hisoblanadi — ular havola emas
    s = re.sub(r'<code[^>]*>.*?</code>|<div class="cmd"[^>]*>.*?</div>'
               r'|<span class="eg">.*?</span>|<div class="natija">.*?</div>',
               '', open(f).read(), flags=re.S)
    for m in re.finditer(r'href="([^"#][^"]*?)"', s):
        h = m.group(1)
        if h.startswith(('http', 'mailto')): continue
        nl += 1
        if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(f), h.split('#')[0]))):
            bad(f'HAVOLA {f} → {h}')
print(f'✔ {nl} ichki havola')

# 4) data-cmd atributi to'g'ri yopilganmi (xom yoki \" qo'shtirnoq Copy tugmasini buzadi)
nc = 0
for f in ALL:
    s = open(f).read()
    for m in re.finditer(r'data-cmd="', s):
        nc += 1
        j = s.find('"', m.end())
        if not s[j:j+2] == '">': bad(f'DATA-CMD {f} erta tugadi: …{s[max(0,j-40):j]!r}')
print(f'✔ {nc} data-cmd atributi')

# 5) Dars skeleti to'liqmi
need = [('class="qamrov"','qamrov ro\'yxati'),
        ('callout why','nega'), ('mode-hint','rejim'), ('data-mode="do"','amaliyot'),
        ('class="predict"','taxmin'), ('class="quiz"','quiz'), ('class="recall"','eslab ayting'),
        ('class="recap"','xulosa'), ('primary-source','manba'), ('ask-teacher','savol'),
        ('class="checklist"','ro\'yxat'), ('lesson-nav','navigatsiya'), ('footnotes','izoh')]
for f in LESSONS:
    s = open(f).read()
    miss = [uz for k, uz in need if k not in s]
    if miss: bad(f"SKELET {os.path.basename(f)}: yo'q → {miss}")

# 4b) Shell buyruqlari bash sintaksisidan o'tadimi (data-cmd ichidagi)
import html as _html, subprocess, tempfile
SHELL_BOSH = ('cd ', 'cat ', 'php ', 'git ', 'ls ', 'mkdir ', 'composer ', 'npm ',
              'grep ', 'echo ', 'curl ', 'rm ', 'cp ', 'mv ', 'find ', 'sed ',
              'python3 ', 'printf ', 'for ', 'time ', 'chmod ', 'xdg-open ')
nsh = 0
for f in ALL:
    src = open(f).read()
    # faqat amaliyot bloklari: <div class="cmd"> (kod misollari <code class="cmd"> da)
    for m in re.finditer(r'<div class="cmd" data-cmd="([^"]*)"', src):
        cmd = _html.unescape(m.group(1))
        birinchi = cmd.lstrip().split('\n')[0]
        if not birinchi.startswith(SHELL_BOSH):
            continue
        nsh += 1
        with tempfile.NamedTemporaryFile('w', suffix='.sh', delete=False) as t:
            t.write(cmd + '\n')
            yol = t.name
        r = subprocess.run(['bash', '-n', yol], capture_output=True, text=True)
        os.unlink(yol)
        if r.returncode != 0:
            xato = r.stderr.strip().split('\n')[-1][:90]
            bad(f'BASH SINTAKSIS {os.path.basename(f)}: {birinchi[:40]!r} → {xato}')
print(f'\u2714 {nsh} shell buyrug\'i bash sintaksisidan o\'tdi')

# 5b) Qamrov bloki mazmunli bo'lsin (kamida 5 band, har bandda izoh)
for f in LESSONS:
    s = open(f).read()
    i = s.find('class="qamrov"')
    if i < 0: continue
    blok = s[i:s.find('</div>', i)]
    n = len(re.findall(r'<li><b>', blok))
    izoh = len(re.findall(r'class="nima"', blok))
    if n < 5: bad(f'QAMROV {os.path.basename(f)}: faqat {n} band (kamida 5 kerak)')
    if n != izoh: bad(f'QAMROV {os.path.basename(f)}: {n} band, {izoh} izoh — teng bo\'lishi kerak')

# 6) Teg balansi
for f in ALL:
    s = open(f).read()
    for t in ['div','section','ol','ul','dl','table','details','main','li','tr','dd','dt']:
        o, c = len(re.findall(r'<%s[ >]' % t, s)), len(re.findall(r'</%s>' % t, s))
        if o != c: bad(f'TEG {f}: <{t}> {o} vs </{t}> {c}')

# 7) Fayl raqami sarlavhaga mos
for f in LESSONS:
    n = int(os.path.basename(f)[:4])
    t = open(f).read()
    if ('DARS %d' % n) not in t and ('DARS %02d' % n) not in t:
        bad(f'RAQAM {f}: "DARS {n}" yo\'q')

# 8) Yo'l xaritasi: tayyor darslar soni fayllar soniga teng + nomlar mos
r = open('reference/yol-xaritasi.html').read()
done = re.findall(r'<li class="done">.*?href="\.\./lessons/(\d{4})[^"]*".*?</li>', r, re.S)
if len(done) != len(LESSONS):
    bad(f'XARITA: {len(done)} ta "done" yozuv, lekin {len(LESSONS)} ta dars fayli bor')
for num in done:
    if not glob.glob(f'lessons/{num}-*.html'): bad(f'XARITA: {num} havolasi fayl emas')
tot = len(re.findall(r'road-n">', r))
m = re.search(r'Tayyor darslar: (\d+) / (\d+)', r)
if int(m.group(1)) != len(LESSONS) or int(m.group(2)) != tot:
    bad(f'XARITA hisobi: "{m.group(0)}" — bo\'lishi kerak "{len(LESSONS)} / {tot}"')
nows = len(re.findall(r'<li class="now">', r))
if len(LESSONS) == tot:
    # kurs tugadi — "keyingi dars" bo'lmasligi kerak
    if nows != 0: bad('XARITA: kurs tugagan, "now" bo\'lmasin')
elif nows != 1:
    bad('XARITA: aynan bitta "now" bo\'lishi kerak')
print(f'✔ xarita: {len(done)} tayyor / {tot} jami')

# 9) Bosh sahifadagi dars havolalari fayllarga mos
idx = open('index.html').read()
hrefs = re.findall(r'href="lessons/(\d{4})[^"]*"', idx)
if len(hrefs) != len(LESSONS): bad(f'INDEX: {len(hrefs)} havola, {len(LESSONS)} dars fayli')

# 10) Oldinga raqamli havola bo'lmasin (faqat modul harfi) — keyingi dars mustasno
nxt = len(LESSONS) + 1
for f in LESSONS:
    s = open(f).read()
    for m in re.finditer(r'(\d{1,2})\s*-\s*dars', s):
        n = int(m.group(1))
        if n > nxt: bad(f'OLDINGA HAVOLA {os.path.basename(f)}: {n}-dars — modul harfi ishlatilsin')

print('\n' + ('🎉 HAMMASI TOZA' if not fail else f'⚠️ {len(fail)} ta muammo'))
sys.exit(1 if fail else 0)
