#!/usr/bin/env python3
"""Darsni tayyor deb belgilaydi: yo'l xaritasi + index + hisoblar.

Ishlatilishi:
    python3 tools/dars-belgila.py 53 lessons/0053-events-va-listeners.html "Events va Listeners" "make:event · dispatch"
"""
import re
import sys
from pathlib import Path

ILDIZ = Path(__file__).resolve().parent.parent


def xarita(n: int, fayl: str, sarlavha: str, cmds: str | None) -> None:
    p = ILDIZ / 'reference/yol-xaritasi.html'
    s = p.read_text()

    # joriy darsni done qilamiz
    naqsh = (
        r'(      <li class="now">\n        <span class="road-n">%d</span>\n'
        r'        <div class="road-body">\n)          <span class="t">(.*?)</span>\n'
        r'(          <span class="road-win">.*?</span>\n)'
        r'          <span class="road-cmds">(.*?)</span>\n'
        r'(        </div>\n)        <span class="road-state">.*?</span>' % n
    )
    m = re.search(naqsh, s, re.S)
    if not m:
        sys.exit(f'❌ xaritada {n}-dars "now" holatida topilmadi')

    yangi_cmds = cmds if cmds else m.group(4)
    s = s[:m.start()] + (
        f'      <li class="done">\n        <span class="road-n">{n}</span>\n'
        f'        <div class="road-body">\n'
        f'          <a href="../{fayl}">{sarlavha}</a>\n'
        f'{m.group(3)}'
        f'          <span class="road-cmds">{yangi_cmds}</span>\n'
        f'{m.group(5)}        <span class="road-state">Tayyor</span>'
    ) + s[m.end():]

    # keyingi darsni now qilamiz
    keyingi = f'      <li>\n        <span class="road-n">{n + 1}</span>'
    if keyingi in s:
        s = s.replace(keyingi, f'      <li class="now">\n        <span class="road-n">{n + 1}</span>', 1)
        # o'sha blokdagi "Rejada" ni "Keyingi" ga
        i = s.index(f'<span class="road-n">{n + 1}</span>')
        j = s.index('</li>', i)
        blok = s[i:j].replace('<span class="road-state">Rejada</span>',
                              '<span class="road-state">Keyingi</span>', 1)
        s = s[:i] + blok + s[j:]

    s = re.sub(r'Tayyor darslar: \d+ / 73', f'Tayyor darslar: {n} / 73', s)
    p.write_text(s)


def bosh_sahifa(n: int, fayl: str, sarlavha: str, holat: str | None) -> None:
    p = ILDIZ / 'index.html'
    s = p.read_text()

    oldingi = re.search(r'      <li><span class="n">%d</span>.*?</li>' % (n - 1), s)
    if not oldingi:
        sys.exit(f'❌ index.html da {n - 1}-dars qatori topilmadi')

    qator = (f'      <li><span class="n">{n}</span> '
             f'<a href="{fayl}">{sarlavha}</a> '
             f'<span class="tag ok">Tayyor</span></li>')
    s = s[:oldingi.end()] + '\n' + qator + s[oldingi.end():]

    if holat:
        s = re.sub(r'Holat: \d+ / 73 — .*?</span>', f'Holat: {n} / 73 — {holat}</span>', s)
    else:
        s = re.sub(r'Holat: \d+ / 73', f'Holat: {n} / 73', s)
    p.write_text(s)


def main() -> None:
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    n = int(sys.argv[1])
    fayl = sys.argv[2]
    sarlavha = sys.argv[3]
    cmds = sys.argv[4] if len(sys.argv) > 4 else None
    holat = sys.argv[5] if len(sys.argv) > 5 else None

    xarita(n, fayl, sarlavha, cmds)
    bosh_sahifa(n, fayl.replace('lessons/', 'lessons/'), sarlavha, holat)
    print(f'✅ {n}-dars belgilandi: {sarlavha}')


if __name__ == '__main__':
    main()
