## česa ne delat:
- ne uporabljat pravega imena/osebnih podatkov nikjer (tudi pod commit name/email)
- ne uporabljat `git push --force` - preberi si npr. https://rogerdudler.github.io/git-guide/
- ne urejat `README.md` direktno

---

## kako dela generiranje koledarja?

- za generiranje `README.md` potrebujes `calcurse` (command line ncurses calendar program - na voljo za Linux, BSD ter macOS)
- vsi appointmenti so v file `apts`. to je native file za `calcurse`
- ko startas `./fscalcurse` calcurse namesto svojega `apts` file-a (ki je verjetno v `~/.calcurse/apts`) vzame tega `coronafs/apts`

&nbsp;

- za dodajanje je najlazje dodat stvari v `apts`. to naredis z calcurse (lahko pa tudi rocno)
- je pa za compatibility vse exportano v `fs.ical` (icalendar file). export se zgodi v `update_readme.sh`
- ce spremenis `fs.ical` file ga lahko tudi importas v calcurse `./fscalcurse -i fs.ical`

&nbsp;

- ko startas `./update_readme.sh` se iz `apts` generira `fs.ical` ter iz `apts` se export-ajo vsi eventi za naslednjih 7dni.
- ce startas `./update_readme.sh` z dodatni argumentom (npr. `./update_readme.sh neki`) potem se zgodi tudi avtomatski commit `apts`, `fs.ical` ter `README.md`, ki mu sledi push na origin/master.

