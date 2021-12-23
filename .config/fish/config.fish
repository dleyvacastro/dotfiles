if status is-interactive
    # Commands to run in interactive sessions can go here
    starship init fish | source
    set fish_greeting
    alias cat "/bin/bat"
    alias catn "/bin/cat"
    alias catnl "/bin/bat --paging=never"
    alias ll='lsd -lh --group-dirs=first'
    alias la='lsd -a --group-dirs=first'
    alias l='lsd --group-dirs=first'
    alias lla='lsd -lha --group-dirs=first'
    alias ls='lsd --group-dirs=first'

    alias theme='sh ~/.config/qtile/settings/theme_loader.sh'
    alias wallpaper='python ~/.config/apthemes/wall_init.py'
    alias config='/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME'
    # neofetch
end
