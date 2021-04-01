# Lines configured by zsh-newuser-install
HISTFILE=~/.config/zsh/.histfile
HISTSIZE=1000
SAVEHIST=1000
bindkey -e
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/rossb/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall
#
# powerline-shell
powerline-daemon -q
. /usr/share/powerline/bindings/zsh/powerline.zsh


alias ls="exa -lah --color=always --group-directories-first"
alias cat="bat"
alias pip="pip3"

# git
alias gAdd="git add -A"
alias gCommit="git commit -m"
alias gPush="git push"
alias gClone="git clone"

# pacman
alias pm="sudo pacman -S"

figlet GUARDIAN -c
neofetch
