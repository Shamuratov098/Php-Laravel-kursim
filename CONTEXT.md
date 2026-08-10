# PHP & Laravel kursi

O'zbek tilidagi shaxsiy kurs: sof PHP poydevoridan boshlab, ishga tayyor Laravel backend
dasturchi darajasigacha. Bu hujjat — kursning **atamalar lug'ati**: bir tushuncha uchun bir
so'z. 72 dars bo'ylab bir xil atamani ishlatish uchun shu ro'yxatga rioya qilinadi.

## Til siyosati

O'zbekcha matn + **inglizcha texnik atama**. Atama tarjima qilinmaydi (`route` «yo'nalish»
emas, `route` bo'lib qoladi), chunki foydalanuvchi hujjatlarni, xato xabarlarini va ish
e'lonlarini inglizcha o'qiydi. Atama birinchi marta uchraganda: inglizcha nomi + bir
qatorli o'zbekcha izoh + glossary'ga havola.

## Kurs atamalari

**Dars**:
Bitta HTML fayl, bitta aniq g'alaba beruvchi o'quv birligi. `lessons/NNNN-*.html`.
_Avoid_: mavzu, bo'lim, darslik, urok

**Modul**:
Bir maqsadga xizmat qiluvchi darslar guruhi (A–J).
_Avoid_: bosqich, qism, blok

**G'alaba**:
Darsdan keyin foydalanuvchi qila oladigan aniq, kuzatiladigan bitta narsa. Har darsda bittasi.
_Avoid_: natija, maqsad, outcome

**Marra**:
Kursdagi oraliq nuqta, u yerga yetganda yangi imkoniyat ochiladi. Yagona marra —
**«Junior tayyor», 47-dars**.
_Avoid_: nuqta, checkpoint, bosqich

**Rejim**:
Darsning ikki ko'rinishi: 📱 **o'qish** (telefon, bilim va takrorlash) va 💻 **amaliyot**
(kompyuter, kod yozish). `data-mode="read|do"` bilan belgilanadi.
_Avoid_: versiya, ko'rinish, holat

**Amaliyot**:
Darsning 💻 rejimidagi qismi — qadam-baqadam real kod yoziladi va natija tekshiriladi.
_Avoid_: praktika, mashg'ulot, laboratoriya

**Mashq**:
Qisqa, eslab aytishga majburlaydigan topshiriq: «natijani taxmin qiling», «xatoni toping»,
«shu funksiyani yozing». Har darsda 2–4 ta.
_Avoid_: test, savol, uy vazifasi, topshiriq

**Poydevor**:
Modul A — Laravel'ga tegmasdan o'rganiladigan sof PHP qismi.
_Avoid_: asoslar, basics, kirish

**Mini-framework**:
A12–A13 darslarida foydalanuvchi **o'z qo'li bilan** yozadigan ~100 qatorlik front
controller + router + container. Kursning kaliti: keyinchalik Laravel'ning har bir
«sehri» shu kodga qaytarib bog'lanadi.
_Avoid_: o'z framework, kichik Laravel, freymvork

**Sehr**:
Foydalanuvchi tushunmaydigan, «o'zi ishlab ketadigan» Laravel xatti-harakati. Kursning
maqsadi — har bir sehrni ochib, mexanizmga aylantirish. Dars ichida ochiq atama sifatida
ishlatiladi («bu sehr emas, mana nima bo'lyapti»).
_Avoid_: magic, avtomatika

**Umurtqa loyiha**:
Butun kurs bo'ylab o'sib boradigan yagona loyiha — **IshTop**. Mayda mashqlardan farqli,
u hech qachon tashlanmaydi.
_Avoid_: asosiy loyiha, katta loyiha, final loyiha

**Zanjir**:
Har darsning amaliyoti oldingi darsning natijasi ustida ishlashi qoidasi. Buzilmaydi.
_Avoid_: ketma-ketlik, bog'lanish

## IshTop domeni

Kurs davomida quriladigan ilova: ish beruvchilar vakansiya joylaydi, nomzodlar ariza
beradi. Matnda o'zbekcha atama, **kodda inglizcha** nom ishlatiladi — ikkisi bu jadval
orqali bog'lanadi va 72 dars bo'ylab o'zgarmaydi.

**Kompaniya** → `Company`:
Vakansiya joylaydigan tashkilot. Bitta `User` (ish beruvchi) ga tegishli.
_Avoid_: tashkilot, firma, ish beruvchi (bu — odam, kompaniya emas)

**Vakansiya** → `Vacancy`:
Ochiq ish o'rni e'loni. `Company` ga tegishli, muddati (`expires_at`) bor.
_Avoid_: e'lon, ish, lavozim, job

**Nomzod** → `User` (`role: candidate`):
Ariza beradigan foydalanuvchi. Alohida jadval emas — roli bilan ajratiladi.
_Avoid_: talabgor, ishchi, kandidat

**Ish beruvchi** → `User` (`role: employer`):
Kompaniyaga egalik qiluvchi va vakansiya joylaydigan foydalanuvchi.
_Avoid_: xo'jayin, rekruter, admin

**Ariza** → `Application`:
Nomzodning aynan bitta vakansiyaga topshirgan hujjati. Statusi (`status`) va rezyume
fayli bor. `User` ↔ `Vacancy` orasidagi bog'lanish shu yozuv orqali amalga oshadi.
_Avoid_: so'rov, zayavka, murojaat, arizacha

**Ko'nikma** → `Skill`:
Vakansiya talab qiladigan qobiliyat (`PHP`, `Laravel`, `SQL`). `Vacancy` bilan
`belongsToMany`.
_Avoid_: tag, teg, mahorat, talab
