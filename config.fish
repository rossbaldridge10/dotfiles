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

# git
alias gAdd "git add -A"
alias gCommit "git commit -m"
alias gPush "git push"
alias gClone "git clone"

