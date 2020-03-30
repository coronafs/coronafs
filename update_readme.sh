#!/bin/sh

echo "## informacije za študiji na FS v času covid-19. aka VIS(un)link" > README.md

echo "ta site si prizadeva združiti informacije potrebe za študiji na FS. " >> README.md
echo >> README.md
echo "trenutno so potrebne informacije razpršene po svetovnem spletu in poskusa centralizacije (še) ni" >> README.md
echo >> README.md
echo "če hočeš kaj dodati preberi CONTRIBUTING" >> README.md
echo >> README.md
echo "posnetki predavanj https://drive.google.com/open?id=1IRr_VypWnkjKROawaqUm3SdmUvIXlyR4" >> README.md


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
	git add README.md fs.ical
	git commit
	git push
fi

