pacman -S lightdm
pacman -S lightdm-gtk-greeter

systemctl enable lightdm

#AUR
pacman -S base-devel
git clone https://aur.archlinux.org/yay-git.git
cd yay-git
makepkg -si
cd

# Fonts
pacman -S ttf-dejavu ttf-liberation noto-fonts
# Audio
pacman -S pulseaudio pavucontrol
pacman -S pamixer
# Mount
pacman -S udiskie ntfs-3g
# Net
pacman -S network-manager-applet
# Volume
pacman -S volumeicon cbatticon
# Notification
pacman libnotify notification-daemon
