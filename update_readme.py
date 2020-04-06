#!/usr/bin/python3

import datetime

def izpis(s):
    return str( s + ": " + eval(s))

with open("README.md", 'w') as f:
    f.write("## informacije za študiji na FS v času covid-19. aka VIS(un)link\n")
    f.write("- ta site si prizadeva združiti informacije potrebe za študiji na FS. \n")
    f.write("- trenutno so potrebne informacije razpršene po svetovnem spletu in poskusa centralizacije (še) ni\n")
    f.write("- posnetki predavanj https://drive.google.com/open?id=1IRr_VypWnkjKROawaqUm3SdmUvIXlyR4\n")
    f.write("- če hočeš kaj dodati preberi CONTRIBUTING.md\n")
    
    
    f.write("# ta teden na sporedu:\n")
    f.write("updated: " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n\n")
    
    
    urnik = {"PON":[], "TOR":[], "SRE":[], "CET":[], "PET":[]}
    
    
    # laserski sistemi
    ls_pred_link = "https://global.gotomeeting.com/join/353416765"
    urnik["PET"].append("10:00 - 11:30 LS pred")
    
    ls_vaje_link = "https://global.gotomeeting.com/join/373099509"
    urnik["TOR"].append("07:30 - 09:30 LS vaje")
    urnik["TOR"].append("10:00 - 12:00 LS vaje")
    urnik["TOR"].append("13:00 - 14:30 LS vaje")
    urnik["CET"].append("07:30 - 09:30 LS vaje")
    urnik["CET"].append("10:00 - 12:00 LS vaje")
    urnik["CET"].append("13:00 - 14:30 LS vaje")
    
    # metodika konstruiranja
    mk_pred_link = "https://global.gotomeeting.com/join/143063325"
    urnik["SRE"].append("13:15 - 15:15 MK pred")
    
    mk_vaje_link = ""
    
    # osnove mehatronike
    om_pred_link = "https://youtu.be/0AdcCyeFlfk"
    urnik["PON"].append("08:00 - 10:30 OM pred")
    
    om_vaje_link = "https://global.gotomeeting.com/join/122739893"
    urnik["CET"].append("11:00 - 14:00 OM vaje")
    
    # proizvodni inženirstvo
    pi_pred_link = "https://global.gotomeeting.com/join/496606829"
    urnik["SRE"].append("10:50 - 12:40 PI pred")
    
    pi_vaje_link = "https://global.gotomeeting.com/join/457793757"
    urnik["PON"].append("07:30 - 09:00 PI vaje")
    urnik["PON"].append("09:00 - 10:30 PI vaje")
    urnik["PON"].append("13:00 - 14:30 PI vaje")
    urnik["PON"].append("15:00 - 16:30 PI vaje")
    urnik["PON"].append("17:00 - 18:30 PI vaje")
    urnik["TOR"].append("07:30 - 09:00 PI vaje")
    urnik["TOR"].append("09:00 - 10:30 PI vaje")
    urnik["TOR"].append("13:30 - 14:30 PI vaje")
    urnik["TOR"].append("15:00 - 16:30 PI vaje")
    
    # tribologija
    tr_pred_link = "https://global.gotomeeting.com/join/593007621"
    urnik["PON"].append("11:00 - 12:30 TR vaje")
    
    tr_vaje_link = ""
    

    # izpis linkov
    f.write("## linki:\n")
    f.write("- " + izpis("ls_pred_link") + "\n")
    f.write("- " + izpis("ls_vaje_link") + "\n")
    f.write("- " + izpis("mk_pred_link") + "\n")
    f.write("- " + izpis("mk_vaje_link") + "\n")
    f.write("- " + izpis("om_pred_link") + "\n")
    f.write("- " + izpis("om_vaje_link") + "\n")
    f.write("- " + izpis("pi_pred_link") + "\n")
    f.write("- " + izpis("pi_vaje_link") + "\n")
    f.write("- " + izpis("tr_pred_link") + "\n")
    f.write("\n")

    
    # izpis urnika
    f.write("## urnik:\n")
    for key, dan in urnik.items():
            f.write("- " + key + "\n")
            for event in dan:
                f.write("\t- " + event + "\n")
    f.write("\n")

    f.write("## Licenca\n")
    f.write("THIS FILES PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n")
    f.write("IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n")
    f.write("FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n")
    f.write("AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n")
    f.write("LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n")
    f.write("OUT OF OR IN CONNECTION WITH THE FILES OR THE USE OR OTHER DEALINGS WITH THE FILES.\n")

