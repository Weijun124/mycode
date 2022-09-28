#!/bin/bash

# Start with prompt window for user input -->inputfield
# Then ask user for y/n for create new group or not -->choosetocreate
# Build the user and assign him/her to the assign group-->createuser
# Repeat the process again for user want to continue create user by using while loop with tryAgain

inputfield(){
echo "Please name the new User" 
read USER
echo "Do you want to create a new group? [y/n]"
read NEWGROUP
}

choosetocreate(){
if [ "$NEWGROUP" == "y" ]
then
    echo "Please name the new group to assign"
    read GROUP
    creategroup
else
    echo "Plase assign the exist group to $USER"
    read GROUP
    createuser
fi
}

createuser(){
sudo useradd $USER
echo "$USER is created"
sudo usermod -aG $GROUP $USER
echo "$USER is assigned to the $GROUP"
sleep 1
id $USER
}

creategroup(){
sudo groupadd $GROUP
createuser
}


tryAgain(){
echo "Would you like to add new user? [y/n]"
read ANS
}

while [ "$ANS" != "n" ]
do
    inputfield
    choosetocreate
    tryAgain
done

echo "Bye Bye"
