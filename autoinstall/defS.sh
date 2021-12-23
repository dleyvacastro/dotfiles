pacman -S bat --noconfirm
pacman -S cmatrix --noconfirm
pacman -S discord --noconfirm
pacman -S gparted --noconfirm
pacman -S grub-customizer --noconfirm
pacman -S hollywood --noconfirm
pacman -S htop --noconfirm
pacman -S kdeconnect --noconfirm
pacman -S lsd --noconfirm
pacman -S lxappearance --noconfirm
pacman -S neofetch --noconfirm
pacman -S nitrogen --noconfirm
pacman -S nodejs --noconfirm
pacman -S notepadqq --noconfirm
pacman -S npm --noconfirm
pacman -S papirus-icon-theme --noconfirm
pacman -S ranger --noconfirm
pacman -S ruby --noconfirm
pacman -S spotifyd --noconfirm
pacman -S sqlite --noconfirm
pacman -S starship --noconfirm
pacman -S telegram-desktop --noconfirm
pacman -S vlc --noconfirm
pacman -S xclip --noconfirm
pacman -S zsh --noconfirm

git clone https://aur.archlinux.org/snapd.git
cd snapd
makepkg -si
systemctl enable --now snapd.socket
cd
