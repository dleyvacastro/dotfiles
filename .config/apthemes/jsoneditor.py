import json
from os.path import join, expanduser

dot_config_path = join(expanduser('~'), ".config")
rofi_path = join(dot_config_path, "rofi")
kitty_path = join(dot_config_path, "kitty")
nvim_path = join(dot_config_path, "nvim")
dg_path = join(dot_config_path,
               'qtile', 'settings', 'default_globals.json')


with open('look.json', 'r') as f:
    a = json.load(f)
    print(a)

for i in a:
    a[i]["nvim"] = "DEFAULT"

with open('look2.json', 'w') as f:
    f.write(json.dumps(a, indent=4))
