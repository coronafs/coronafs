#!/bin/sh

echo "## informacije za studij na FS v casu covid-19. aka VIS(un)link" > README.md

echo "ta site si prizadeva zdruziti informacije potrebe za studij na FS. " >> README.md
echo >> README.md
echo "trentno so potrebne informacije razprsene po svetovnem spletu in poizkusa centralizacije (se) ni" >> README.md



echo >> README.md
echo "# naslednjih 7dni" >> README.md
echo "updated: $(date '+%Y-%m-%d %H:%M:%S')" >> README.md
echo >> README.md

calcurse --output-datefmt "%A %d/%m/%y" -r7 >> README.md

echo "## Licenca" >> README.md
echo "THIS FILES PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR">> README.md
echo "IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,">> README.md
echo "FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE">> README.md
echo "AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER">> README.md
echo "LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,">> README.md
echo "OUT OF OR IN CONNECTION WITH THE FILES OR THE USE OR OTHER DEALINGS WITH THE FILES." >> README.md

if [ "$#" -eq 1 ]; then
	git add README.md
	git commit -m "update-an README.md z dogodki naslednijih 7dni"
	git push
fi

