#!/usr/bin/env python3
"""Quiz variantlaridagi so'z sonini tekshiradi (yozishdan oldin).

    python3 tools/quiz-sana.py "variant bir" "variant ikki" "variant uch"
"""
import sys

if len(sys.argv) < 2:
    sys.exit(__doc__)

sonlar = [len(v.split()) for v in sys.argv[1:]]
for v, n in zip(sys.argv[1:], sonlar):
    print(f'{n:>3}  {v}')
print('✅ teng' if len(set(sonlar)) == 1 else f'❌ TENG EMAS: {sonlar}')
