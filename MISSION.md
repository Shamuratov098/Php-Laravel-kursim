# Mission: PHP va Laravel (backend dasturchi bo'lib ishga kirish)

## Why (Nega)
Junior/mid **Laravel backend dasturchi** bo'lib ishga kirish. Bugun Laravel loyihalarini
AI yordamida qura olaman va kodni o'qiy olaman — lekin «nega aynan shunday ishlaydi?»,
«bu qatorni o'chirsam nima buziladi?» degan savollarga javob bera olmayman. Maqsad —
shu bog'liqlikni yo'qotib, kodning egasi bo'lish.

## Success looks like (Muvaffaqiyat belgilari)
- Kompaniya bergan **texnik topshiriqni** (auth + CRUD + API + validatsiya, 3–4 soat)
  boshidan oxirigacha **AI yordamisiz** o'zim yozib topshiraman
- Intervyu savollariga o'z so'zim bilan, misol keltirib javob beraman: so'rov Laravel
  ichida qanday sayohat qiladi · N+1 nima va qanday topiladi · Service Container nima
  uchun kerak · Gate va Policy farqi · middleware qachon ishlaydi
- **Notanish** Laravel loyihasi berilsa: tuzilishini tushunaman, so'rov qaysi yo'ldan
  borishini aytaman va berilgan bug'ni o'zim topib tuzataman
- **IshTop** loyihasi real domenda, HTTPS bilan ishlab turadi — queue worker, scheduler
  va log to'g'ri sozlangan; havolasi rezyumemda

## Constraints (Cheklovlar)
- Kuniga **~1–2 soat, har kuni** → 73 dars ≈ 2.5–3 oy. Muntazamlik zarbadan muhim.
- Til: **o'zbekcha**; PHP/Laravel atamalari **inglizcha** qoladi (`route`, `middleware`,
  `migration`...) — batafsil: [[CONTEXT.md]]
- **Faqat bepul manbalar** (asosiy: `laravel.com/docs/13.x`)
- Muhit: Ubuntu 24.04 · **PHP 8.3** · Laravel 13 · SQLite → keyinroq MySQL · terminal asosida
- Har dars **qisqa** va bitta aniq g'alaba beradi — ishchi xotira kichik
- Boshlanish ishqalanishi nolga yaqin bo'lishi shart (oldingi urinish boshlanmagani
  uchun barbod bo'lgan)

## Out of scope (Hozircha kerak emas)
- Frontend framework — React, Vue, Inertia (backend fokus)
- Livewire — faqat kurs oxirida ixtiyoriy bonus sifatida
- Broadcasting / WebSocket, Octane, Nova, Cashier (to'lov), MongoDB, Scout
- Chuqur DevOps — Kubernetes, Terraform, mikroservis arxitekturasi
- Package development (o'z Composer paketini nashr qilish)
