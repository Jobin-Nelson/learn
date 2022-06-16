#!/usr/bin/bash

flatpak run com.skype.Client &
if ! tmux has-session -t Rappel; then
    cd ~/playground/dev/Rappel
    tmux new -s Rappel -d
    tmux new-window -t Rappel:1
    tmux rename-window -t Rappel:0 Editor
    tmux rename-window -t Rappel:1 Flask
    tmux send-keys -t Rappel:0 '. venv/bin/activate' Enter
    tmux send-keys -t Rappel:1 '. venv/bin/activate' Enter
    tmux send-keys -t Rappel:0 'nvim' Enter
    tmux select-window -t Rappel:0
fi
tmux attach -t Rappel
exit 0
