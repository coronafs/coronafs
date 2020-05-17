#!/usr/bin/python3

import datetime

class Link:
    _registry = []

    def __init__(self, ime):
        self._registry.append(self)
        self.ime = ime
        self.link = ""
        self.urnik = {"PON":[], "TOR":[], "SRE":[], "CET":[], "PET":[]}
        return 

    def set_link(self, link):
        self.link = link
        return 

    def append_event(self, dan, ura):
        self.urnik[dan].append(ura)
        return 


# laserski sistemi
ls_pred = Link("LS pred")
ls_pred.set_link("https://global.gotomeeting.com/join/370091797")
ls_pred.append_event("PET", "10:00 - 11:30")

ls_vaje = Link("LS vaje")
ls_vaje.set_link("https://global.gotomeeting.com/join/494126645")
ls_vaje.append_event("TOR", "07:30 - 09:30")
ls_vaje.append_event("TOR", "10:00 - 12:00")
ls_vaje.append_event("TOR", "13:00 - 14:30")
ls_vaje.append_event("CET", "07:30 - 09:30")
ls_vaje.append_event("CET", "10:00 - 12:00")
ls_vaje.append_event("CET", "13:00 - 14:30")


# metodika konstruiranja
mk_pred = Link("MK pred")
mk_pred.set_link("https://global.gotomeeting.com/join/735010005")
mk_pred.append_event("SRE", "13:15 - 15:15")

mk1_emba = Link("MK vaje emabalaza 1")
mk1_emba.set_link("https://global.gotomeeting.com/join/229719629")
mk1_emba.append_event("TOR", "09:30 - 11:00")

mk3_emba = Link("MK vaje emabalaza 3")
mk3_emba.set_link("https://global.gotomeeting.com/join/579016605")
mk3_emba.append_event("TOR", "15:00 - 16:30")

mk4_emba = Link("MK vaje emabalaza 4")
mk4_emba.set_link("https://global.gotomeeting.com/join/757295093")
mk4_emba.append_event("TOR", "16:30 - 18:00")


# osnove mehatronike
om_pred = Link("OM pred")
om_pred.set_link("https://youtu.be/Ps_nCduMbM8")
om_pred.append_event("PON", "08:00 - 10:30")

om_vaje = Link("OM vaje")
om_vaje.set_link("https://global.gotomeeting.com/join/122739893")
om_vaje.append_event("CET", "11:00 - 14:00")

om_vaje_PID = Link("OM vaje PID")
om_vaje_PID.set_link("https://global.gotomeeting.com/join/593909597")
om_vaje_PID.append_event("CET", "11:00 - 14:00")

# proizvodni inženirstvo
pi_pred = Link("PI pred")
 
pi_pred.set_link("https://global.gotomeeting.com/join/873596485")
pi_pred.append_event("SRE", "10:50 - 12:40")

pi_vaje_2del = Link("PI 2. lab SMED in FMEA")
pi_vaje_2del.set_link("https://global.gotomeeting.com/join/365824213")

pi_vaje = Link("PI vaje")
pi_vaje.set_link("https://global.gotomeeting.com/join/457793757")
pi_vaje.append_event("PON", "07:30 - 09:00")
pi_vaje.append_event("PON", "09:00 - 10:30")
pi_vaje.append_event("PON", "13:00 - 14:30")
pi_vaje.append_event("PON", "15:00 - 16:30")
pi_vaje.append_event("PON", "17:00 - 18:30")
pi_vaje.append_event("TOR", "07:30 - 09:00")
pi_vaje.append_event("TOR", "09:00 - 10:30")
pi_vaje.append_event("TOR", "13:30 - 14:30")
pi_vaje.append_event("TOR", "15:00 - 16:30")


# tribologija
tr_pred = Link("TR pred")
tr_pred.set_link("https://global.gotomeeting.com/join/593007621")
tr_pred.append_event("PON", "11:00 - 12:30")
    

with open("README.md", 'w') as f:
    f.write("## informacije za študiji na FS v času covid-19. aka VIS(un)link\n")
    f.write("- ta stran si prizadeva združiti informacije za študiji na FS\n")
    f.write("- trenutno so potrebne informacije razpršene po svetovnem spletu in poskusa centralizacije (še) ni\n")
    f.write("- posnetki predavanj https://drive.google.com/open?id=1IRr_VypWnkjKROawaqUm3SdmUvIXlyR4\n")
    f.write("- če hočeš kaj dodati preberi CONTRIBUTING.md\n")
    
    
    f.write("# ta teden na sporedu:\n")
    f.write("updated: " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n\n")
    
    
    f.write("## samo linki:\n")
    for instance in Link._registry:
        f.write ("- " + instance.ime + ": " + instance.link + "\n")

    f.write("\n")

    f.write("## cel urnik:\n")
    for dan in ["PON", "TOR", "SRE", "CET", "PET"]:
        f.write("- " + dan + "\n")
        for instance in Link._registry:
            if instance.urnik[dan]:
                f.write ("\t- " + instance.ime + ": " + instance.link + "\n")
                [f.write("\t\t- " + i + "\n") for i in instance.urnik[dan]]



    f.write("\n")
    f.write("## Licenca\n")
    f.write("THIS FILES PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n")
    f.write("IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n")
    f.write("FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n")
    f.write("AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n")
    f.write("LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n")
    f.write("OUT OF OR IN CONNECTION WITH THE FILES OR THE USE OR OTHER DEALINGS WITH THE FILES.\n")

