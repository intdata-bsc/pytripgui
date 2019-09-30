from pytripgui import __version__ as pytripgui_version
from pytrip import __version__ as pytrip_version

about_txt_en = ""
about_txt_en += "PyTRipGUI Version: " + pytripgui_version + "\n"
about_txt_en += "PyTRiP Version:" + pytrip_version + "\n"
about_txt_en += "\n"
about_txt_en += "(c) 2012 - 2018 PyTRiP98 Developers\n"
about_txt_en += "    Niels Bassler\n"
about_txt_en += "    Leszek Grzanka\n"
about_txt_en += "\n"
about_txt_en += "Previous contributors:\n"
about_txt_en += "    Jakob Toftegaard\n"

InfoMessages_en = {
    "about": ["PyTRiPGUI", about_txt_en],
    "addNewPatient": ["Add new Patient", "Before continue, you should create or import Patient"],
    "loadCtxVdx": ["Load CTX and VDX file", "Before continue, you should have loaded CTX and VDX data"],
    "addOneField": ["Add at least one field", "Before conntinue, you should add at least one field to selected plan"]
}

InfoMessages = InfoMessages_en
