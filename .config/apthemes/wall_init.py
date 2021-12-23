from os import listdir
from os.path import join, expanduser
from random import sample
import subprocess

wp_path = join(expanduser('~'), 'Imágenes', 'Wallpapers')
xrandr = "xrandr | grep -w 'connected' | cut -d ' ' -f 2 | wc -l"
rw = sample(listdir(wp_path), 1)[0]
ws_path = join(wp_path, rw)

command = subprocess.run(
    xrandr,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

if command.returncode != 0:
    error = command.stderr.decode("UTF-8")
    connected_monitors = 1
else:
    connected_monitors = int(command.stdout.decode("UTF-8"))
print(connected_monitors)
print(rw)

for i in range(connected_monitors):
    nitrogen = f"nitrogen --set-scaled --head={i} {ws_path}"
    subprocess.run(nitrogen, shell=True)
