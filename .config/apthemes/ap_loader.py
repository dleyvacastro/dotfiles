import json
from os.path import join, expanduser

dot_config_path = join(expanduser('~'), ".config")
rofi_path = join(dot_config_path, "rofi")
kitty_path = join(dot_config_path, "kitty")
nvim_path = join(dot_config_path, "nvim")
dg_path = join(dot_config_path,
               'qtile', 'settings', 'default_globals.json')
apthemes_path = join(expanduser('~'), '.config', 'apthemes')
look_path = join(apthemes_path, 'look.json')
test_path = join(apthemes_path, 'test.conf')


def config2list(file: str):
    with open(join(file), 'r') as f:
        return f.read().split('\n')


def get_sw_line(rl: list, sw: str) -> int:
    for i in rl:
        if i.startswith(sw):
            return rl.index(i)
    raise ValueError('Line not found')


def write_changes(file: str, rl: list) -> None:
    with open(file, 'w') as f:
        f.write('\n'.join(rl))


def update_theme(config_file_path, sw, theme_format) -> None:
    rl = config2list(config_file_path)
    tl = get_sw_line(rl, sw)
    rl[tl] = theme_format
    write_changes(config_file_path, rl)


def rofi(cs):
    config_file_path = join(rofi_path, 'config.rasi')
    update_theme(config_file_path, '@theme', f'@theme "{cs}"')


def kitty(cs):
    config_file_path = join(kitty_path, 'kitty.conf')
    update_theme(config_file_path, 'include themes',
                 f'include themes/{cs}.conf')


def nvim(cs):
    config_file_path = join(nvim_path, 'init.vim')
    sw = 'source $HOME/.config/nvim/themes/'
    theme_format = f'source $HOME/.config/nvim/themes/{cs}.vim'
    update_theme(config_file_path, sw, theme_format)


def main():
    defaultcsk = 'Argonaut'
    defaultcsr = 'material-ocean'
    defaultcsn = 'oceanic-material'
    with open(dg_path, 'r') as f:
        dg = json.load(f)
    with open(look_path, 'r') as f:
        look = json.load(f)

    acs = dg["colors"][:-5]
    csk = look[acs]["kitty"]
    csr = look[acs]["rofi"]
    csn = look[acs]["nvim"]
    if csk == "DEFAULT":
        csk = defaultcsk
    if csr == "DEFAULT":
        csr = defaultcsr
    if csn == "DEFAULT":
        csn = defaultcsn
    kitty(csk)
    rofi(csr)
    nvim(csn)


if __name__ == '__main__':
    main()
