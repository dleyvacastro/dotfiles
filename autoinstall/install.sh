echo "-----AutoInstall Script-----"
printf "Welcome to the Autoinstall process."

printf "Install system basics? [y/n]"
read sysbas
if [ $sysbas == 'y'  ]
then
    sudo sh ./system_basic.sh
fi

printf "Install basic dependences by pacman and yay? [y/n]"
read dep
if [ $dep == 'y' ]
then
    sudo sh ./depS.sh
fi

printf "Install def? [y/n]"
read def
if [ $def == 'y' ]
then
    sudo sh ./defS.sh
    sh ./def.sh
fi
