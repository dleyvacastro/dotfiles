<div style="text-align: justify">
# Dotfiles
# Table of contents
- [General Info](#general-info)
- [Window Manager](#qtile)
    - [Terminal Emulator](#kitty)
    - [Shell](#fish)
    - [Prompt](#starship)
- [Text Editor](#text-editor)
- [Terminal](#terminal)
- [Rofi](#rofi)
- [Software Used](#sofware-used)
- [Custom Scripts](#custom-scripts)
- [Autoinstall](#autoinstall)
# General Info
![alt text](/img/Endeavour_logo.png) \
I'm actually using [EndeavourOS](https://endeavouros.com/) with the Xfce desktop enviroment base.
This is an user friendly Arch Based distro. Xcfe provides all the basic utilities like network managment, file manager, etc. But 
it's only used as base, thus, my usual enviroment is composed by a stad alone Tiling Window Manager and
some dependences like Nitrogen, Picom and some theming. \

New Target Distro: [Arch Linux](https://archlinux.org/)
The objective is being capable of set working full-featured and minimalist work enviroment from base arch.

# [Qtile](https://github.com/dleyvacastro/qtile)
[Qtile](#window-manager) is a stand alone Tiling window manager written in python. \
At this point i've setted all basic utilities and a dynamic workflow, you can see all my configs in [its own repo](https://github.com/dleyvacastro/qtile). \

My configs are highly inspired in [Antonio Sarosi's files](https://github.com/antoniosarosi/dotfiles/tree/master/.config/qtile).

# [Neovim](https://github.com/dleyvacastro/nvim)
The config are basiclly the same as some guy on yt with some minor changes.
[Go to my nvim repo](https://github.com/dleyvacastro/nvim)

# Terminal
I use [kitty](https://sw.kovidgoyal.net/kitty/) as my preference terminal emulator with [fish](https://fishshell.com/) as my shell.
## Kitty
My [Kitty config files](/.config/kitty) are composed by a few files and a theme folder.
### Font config
- Font: [VictorMono Nerd Font](https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/VictorMono.zip).
- Font size: 11.
- Ligatures: Yes, only disble when are focused by the cursor.
### General config
- Some url tweeks opened with [Brave](brave.com).
- `control + c`: Copy or interrupt function.
- Opacity: 85%.
### Themes 
All the themes used come from [this repo](https://github.com/dexpota/kitty-themes). \
CS used:
- [ayu](/.config/kitty/themes/ayu.conf).
- [OneDark](/.config/kitty/themes/OneDark.conf).
- [ayu_mirage](/.config/kitty/themes/ayu_mirage.conf).
- [Dracula](/.config/kitty/themes/Dracula.conf).
- [Blazer](/.config/kitty/themes/Blazer.conf).
- [MaterialDark](/.config/kitty/themes/MaterialDark.conf).
- [Obsidian](/.config/kitty/themes/Obsidian.conf).
- [Bright_Lights](/.config/kitty/themes/Bright_Lights.conf).
- [Argonaut](/.config/kitty/themes/Argonaut.conf). (Default)
- [SpaceGray](/.config/kitty/themes/SpaceGray.conf).
- [MonaLisa](/.config/kitty/themes/MonaLisa.conf).
- [Spacedust](/.config/kitty/themes/Spacedust.conf).
- [Ollie](/.config/kitty/themes/Ollie.conf).
- [polar](/.config/kitty/themes/polar.conf).
- [nord](/.config/kitty/themes/nord.conf).

The theme is applied acording to the current [Master Color Scheme]().
## Fish
Basiclly my [Fish config]((.config/fish)) consist in setting up the [starship prompt]("starship") and some aliases
for [custom scripts](#custom-scripts) and the config command for this repo.
## Starship
I took Antonio Sarosi's [Starship](https://starship.rs/) config file: [check it out](https://github.com/antoniosarosi/dotfiles/blob/master/.config/starship.toml).
# Rofi
I use [rofi](https://github.com/davatorium/rofi) as a launching and switching app menu, using themes some internet themes, matching with the current [Master Color Scheme]().
Font used: [VictorMono Nerd Font](https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/VictorMono.zip).
## Themes & Color Schemes
- [nord](/.config/rofi/themes/nord.rasi).
- [material-ocean](/.config/rofi/themes/material-ocean.rasi). (Default)
- [dracula](/.config/rofi/themes/dracula.rasi).
- [material](/.config/rofi/themes/material.rasi).
- [onedark](/.config/rofi/themes/onedark.rasi).
- [slate](/.config/rofi/themes/slate.rasi).
# Software Used
## System utilities
- [libnotify]().
- [Notification-deamon]().
- [Thunar]().
- [Nitrogen]().
- [Picom - jonaburg fork](https://github.com/jonaburg/picom).
- [Lxappereance]().
- [Volumeicon]().
- [Cbatticon]().
- [TimeShift]().
- [Grub customizer]().
- [Gparted]().
- [Lightdm]().
## Comun Apps
- Browser: [Brave](brave.com).
- Social:
    - [WhatDesk]().
    - [Telegram Desktop]().
    - [Discord]().
    - [Rambox]().
- Mail Manager: [Thunderbird]().
- Music: [Spotify]().
- Clipboard manager: [Diodon]().
- [KDE Connect]().
- Offimatica suite: [OnlyOffice]().
# Custom Scripts
I've created some python and bash scripts to automatice and trigger some changes mainly related to qtile thememing
</div>
