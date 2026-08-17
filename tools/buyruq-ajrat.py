#!/usr/bin/env python3
"""Darsdagi Copy tugmasi beradigan matnni ajratib oladi — uni AYNAN shu holda
ishga tushirib ko'rish uchun. HTML escaping xatolarini shu usul tutadi.

Ishlatish:
    python3 tools/buyruq-ajrat.py lessons/0021-sql-oqish.html /tmp/copy
    cd ~/loyiha && bash /tmp/copy/step2.sh
"""
import re, html, os, sys

if len(sys.argv) < 3:
    sys.exit(__doc__)
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
s = open(src).read()
i = s.find('<div data-mode="do">')          # faqat amaliyot qismi
do = s[i:] if i >= 0 else s
n = 0
for m in re.finditer(r'data-cmd="([^"]*)"', do):
    n += 1
    cmd = html.unescape(m.group(1))
    p = os.path.join(out, f'step{n}.sh')
    open(p, 'w').write(cmd + '\n')
    print(f'{p}  |  {cmd.splitlines()[0][:80]}')
print(f'\n{n} ta buyruq ajratildi. Ularni loyiha papkasida `bash` bilan sinab ko\'ring.')
