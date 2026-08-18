# PHP & Laravel kursi

O'zbek tilidagi shaxsiy kurs: sof PHP poydevoridan boshlab, ishga tayyor Laravel backend
dasturchi darajasigacha. Bu hujjat — kursning **atamalar lug'ati**: bir tushuncha uchun bir
so'z. 73 dars bo'ylab bir xil atamani ishlatish uchun shu ro'yxatga rioya qilinadi.

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
**«Junior tayyor», 48-dars** (Modul F oxiri).
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
beradi. **Kodda ham o'zbekcha** nom ishlatiladi (`Vakansiya`, `vakansiyalar`) — reja
bosqichida inglizcha nom mo'ljallangan edi, lekin 2026-08-17 da o'zbekcha nomda qolishga
qaror qilindi ([ADR 0004](docs/adr/0004-ozbekcha-nomlar-va-laravel-kelishuvlari.md)).

**Chegara qoidasi (2026-08-18):** o'zbekcha nom faqat **bizning domen** modellarimizga
tegishli. **Laravel'ning o'zi bergan** modellar inglizcha qoladi — birinchi navbatda
`User` (u `Authenticatable` dan meros oladi, `config/auth.php` unga ishora qiladi va
starter kit, Sanctum, parol tiklash, bildirishnomalar hammasi shu nomni kutadi).
Matnda esa u har doim **«foydalanuvchi»** deb ataladi.
Pastdagi jadval o'zbekcha atamani kod nomiga bog'laydi va 73 dars bo'ylab o'zgarmaydi.

**Kompaniya** → `Kompaniya` (jadval `kompaniyalar`):
Vakansiya joylaydigan tashkilot. Bitta `User` (ish beruvchi) ga tegishli.
_Avoid_: tashkilot, firma, ish beruvchi (bu — odam, kompaniya emas)

**Vakansiya** → `Vakansiya` (jadval `vakansiyalar`):
Ochiq ish o'rni e'loni. `Kompaniya` ga tegishli (`kompaniya_id`), muddati bor.
_Avoid_: e'lon, ish, lavozim, job

**Nomzod** → `User` (`rol: nomzod`):
Ariza beradigan foydalanuvchi. Alohida jadval emas — roli bilan ajratiladi.
_Avoid_: talabgor, ishchi, kandidat

**Ish beruvchi** → `User` (`rol: ish_beruvchi`):
Kompaniyaga egalik qiluvchi va vakansiya joylaydigan foydalanuvchi.
_Avoid_: xo'jayin, rekruter, admin

**Ariza** → `Ariza` (jadval `arizalar`):
Nomzodning aynan bitta vakansiyaga topshirgan hujjati. Holati va rezyume fayli bor.
`User` ↔ `Vakansiya` orasidagi bog'lanish shu yozuv orqali amalga oshadi.
_Avoid_: so'rov, zayavka, murojaat, arizacha

**Ko'nikma** → `Konikma` (jadval `konikmalar`):
Vakansiya talab qiladigan qobiliyat (`PHP`, `Laravel`, `SQL`). `Vakansiya` bilan
`belongsToMany`, pivot jadval — `konikma_vakansiya`.
_Avoid_: tag, teg, mahorat, talab
