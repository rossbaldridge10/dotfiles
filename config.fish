set fish_greeting ""
#htop
echo ""
figlet -c GUARDIAN | lolcat
neofetch

# configure prompt
function fish_prompt
		 printf '\n'
 		 powerline-shell --shell bare $status
          end

# set aliases
alias ls "exa -alh --color=always --group-directories-first"
alias cat "bat"
alias pip "pip3"

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
#eval /home/rossb/anaconda3/bin/conda "shell.fish" "hook" $argv | source
# <<< conda initialize <<<

