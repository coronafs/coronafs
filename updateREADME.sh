#!/bin/sh

echo "## informacije za studij na FS v casu covid-19" > README.md
echo >> README.md
echo "# today's special " >> README.md
echo "updated: $(date '+%Y-%m-%d %H:%M:%S')" >> README.md
echo >> README.md

calcurse -r >> README.md

if [ "$#" -eq 1 ]; then
	git add README.md
	git commit -m "update-an README.md z dogodki za danes"
	git push
fi

