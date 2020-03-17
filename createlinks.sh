#!/bin/sh

curr_dir=$(pwd)

cln() {
	rm -rf "$2"
	ln -s "$curr_dir/$1" "$2"
}

scln() {
	sudo rm -rf "$2"
	sudo ln -s "$curr_dir/$1" "$2"
}

#    conf-files          | real file
cln i3                   ~/.config/i3
cln Xorg/.xinitrc        ~/.xinitrc
cln Xorg/.Xresources     ~/.Xresources
cln zsh/.zshrc           ~/.zshrc