#!/bin/sh

echo "## informacije za studij na FS v casu covid-19" > README.md
echo >> README.md
echo "# naslednjih 7dni" >> README.md
echo "updated: $(date '+%Y-%m-%d %H:%M:%S')" >> README.md
echo >> README.md

calcurse --output-datefmt %d/%m/%y -r7 >> README.md

if [ "$#" -eq 1 ]; then
	git add README.md
	git commit -m "update-an README.md z dogodki za danes"
	git push
fi

