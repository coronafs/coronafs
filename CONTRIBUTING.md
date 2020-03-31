## kaj ne delat:
- ne uporabljat pravega imena/osebnih podatkov nikjer (tudi pod commit name/email)
- ne uporabljat git push --force
- ne urejat README.md direktno

---

## kako dela generiranje koledarja?

- vsi appointmenti so v file `apts`. to je native file za `calcurse` (command line ncurses calendar program)
- ko startas `./fscalcurse` calcurse namesto svojega `apts` file-a vzame tega `coronafs/apts`

&nbsp;

- za dodajanje je najlazje dodat stvari v `apts`
- je pa za compatibility vse exportano v `fs.ical` (icalendar file). export se zgodi v `update_readme.md`
- ce spremenis `fs.ical` file ga lahko tudi importas v calcurse `calcurse -i fs.ical`
- potem pa z update_readme.sh generiras README.md (potrebujes calcurse)

