# Aplikácia GpxPod pre Nextcloud

Zobrazuje, analyzuje, porovnáva a zdieľa súbory záznamov z GPS.

🌍 Pomôžte nám preložiť túto aplikáciu na [GpxPod Crowdin project](https://crowdin.com/project/gpxpod) (slovenčina by Peter Michnica).

GpxPod :

* 🗺 dokáže zobraziť súbory gpx/kml/tcx/igc/fit kdekoľvek vo vašich súboroch, súboroch, ktoré sú s vami zdieľané a súboroch v priečinkoch, ktoré sú s vami zdieľané. fit súbory budú skonvertované a zobrazené len ak na serveri bude nájdený **GpsBabel**
* 📏 podporuje metrické, anglické a námorné merné systémy
* 🗠 zobrazuje interaktívne grafy s nadmorskou výškou, rýchlosťou alebo tempom
* 🗠 umožňuje vyfarbovať čiary trás podľa rýchlosti, nadmorskej výšky alebo tempa
* 🗠 zobrazuje štatistiky záznamov trás
* ⛛ filtruje záznamy trás podľa dátumu, celkovej vzdialenosti...
* 🖻 zobrazuje otagované obrázky nájdené vo zvolených adresároch
* 🖧 generuje verejné odkazy na trasy/adresáre. Tento odkaz môže byť použitý ak je súbor/adresár zdieľaný pomocou verejného odkazu
* 🗁 umožňuje vám presúvať zvolené súbory záznamov trás
* 🗠 dokáže opraviť nadmorskú výšku záznamu trasy ak je na servri nájdený SRTM.py (gpxelevations)
* ⚖ dokáže globálne porovnať viacero záznamov trás
* ⚖ poskytuje vizuálne porovnanie odchýlok častí podobných trás
* 🀆 umožňuje používateľom pridávať vlastné mapové servery
* ⚙ ukladá/obnovuje hodnoty nastavení používateľa
* 🖍 umožňuje používateľovi manuálne nastaviť farby záznamov
* 🕑 detekuje časové pásmo prehliadača
* 🗬 načítava doplnkové symboly z GpxEdit, ak je nainštalovaný
* 🔒 funguje so šifrovaným priečinkom (šifrovanie na strane servera)
* 🍂 hrdo používa Leaflet s množstvom pluginov na zobrazenie mapy
* 🖴 je kompatibilný s databázami SQLite, MySQL a PostgreSQL
* 🗁 pridáva možnosť zobrazovania .gpx súborov priamo z aplikácie 'Súbory'

This app is tested under Nextcloud 16 with Firefox and Chromium.

## Inštalácia

See the [AdminDoc](https://gitlab.com/eneiluj/gpxpod-oc/wikis/admindoc) for installation details

## Známe problémy

* [FIXED] bad management of file names including simple or double quotes
* *UPOZORNENIE*: kml konverzie NEBUDÚ pracovať s najnovšími kml súbormi používajúcimi proprietárne rozširujúce značky "gx:track".

Any feedback will be appreciated.