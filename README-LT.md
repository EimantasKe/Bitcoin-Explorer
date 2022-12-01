# Bitcoin-Explorer

## Blokų grandinių technologijos – Egzamino užduotis

Naudodami Jums priimtiniausias programavimo priemones (pvz. python/django +python-bitcoinlib + Bitcoin Core) realizuokite stipriai supaprastintą Bitcoin tinklo Blockchain (blokų) explorer'į, kuris yra internetinė programa (angl. web application), veikianti kaip Bitcoin blockchain'o paieškos variklis (angl. Bitcoin search engine), leidžiantis "ištraukti" ir vizualiai pateikti Bitcoin blokchain tinklo informaciją pagal įvairius paieškos kriterijus, kaip kad blokų/transakcijų adresus (hash'us), bloko numerį ir pan.

### Nauduotos priemonės
Flask + Python + Bitcoin Core

### Internetinės programos galimybės
įvėsti – hash, height ar transaction hash, ir gauti informacija apie bloką ar transakciją.

### Programos veikla
Prisijungiama prie Bitcoin Core naudojantis SSH (paramiko).
Naudojantis Flask – render_template ir request, bei sukurtu forms.py failu, vartotojui parodomas index.html (jo skeletas yra base.html), čia vartotojas gali įrašyti string, ir tada paspausti „Search“ mygtuką.
Paspaudus „Search“ mygtuką index.html faile, vartotojas yra nuvedamas į results.html failą, kur rodomą informacija, kuri buvo surinkta pasinaudojus vartotojo įvestimi. Informacija yra renkama getdata() funkcijoje, query‘iant Bitcoin Core.
