set fish_greeting ""
#htop
echo ""
figlet -c GUARDIAN | lolcat
neofetch

# configure prompt
function fish_prompt
		 printf '\n'
 		 powerline-shell --shell bare $status
#                set_color 00d787
#                printf '\n%s  %s\n' (whoami) (hostname)
#                set_color 5fd7ff 
#                printf '\n%s   ' (pwd)
          end

# set aliases
alias ls "exa -alh --color=always --group-directories-first"
alias PC "sh _PyCharm.sh"
alias cat "batcat"
alias pip "pip3"

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
#eval /home/rossb/anaconda3/bin/conda "shell.fish" "hook" $argv | source
# <<< conda initialize <<<

