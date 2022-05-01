#!/usr/bin/bash

function file_count() {
	local count=$(find $1 -maxdepth 1 -type f | wc -l)
	echo "${1}: ${count}"
}

file_count ~/playground
file_count ~/dotfiles
file_count ~/playground/learn
