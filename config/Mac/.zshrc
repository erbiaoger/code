# 网络配置
DEFAULT_USER="user"
ZSH_DISABLE_COMPFIX="true"
export all_proxy=socks5://127.0.0.1:7890
host_ip=$(cat /etc/resolv.conf |grep "nameserver" |cut -f 2 -d " ")
export ALL_PROXY="http://$host_ip:7890"
# export DISPLAY=:0.0


if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# zinit 配置
if [[ ! -f ~/.zinit/bin/zinit.zsh ]]; then
	mkdir ~/.zinit
	git clone https://github.com/zdharma-continuum/zinit.git ~/.zinit/bin
fi
source ~/.zinit/bin/zinit.zsh
zinit snippet 'https://github.com/robbyrussell/oh-my-zsh/raw/master/plugins/git/git.plugin.zsh'
zinit snippet 'https://github.com/sorin-ionescu/prezto/blob/master/modules/helper/init.zsh'

# Powerlevel10k
zinit ice depth=1
zinit light romkatv/powerlevel10k

# 快速目录跳转
zinit ice lucid wait='1'
# Turbo mode with "wait"
zinit light-mode lucid wait for \
  is-snippet OMZ::lib/history.zsh \
  MichaelAquilina/zsh-you-should-use \
  zdharma-continuum/history-search-multi-word \
#   atload"alias zi='zinit'"

# zinit ice wait"2" as"command" from"gh-r" lucid \
#   mv"zoxide*/zoxide -> zoxide" \
#   atclone"./zoxide init zsh > init.zsh" \
#   atpull"%atclone" src"init.zsh" nocompile'!'
# zinit light ajeetdsouza/zoxide

# binary release, unpack provide fzf
zinit ice from"gh-r" as"program"
zinit light junegunn/fzf
zinit light Aloxaf/fzf-tab

# zinit ice from"gh-r" as"program" mv"docker* -> docker-compose" bpick"*linux*"
# zinit load docker/compose
# zinit ice as"program" from"gh-r" mv"docker-c* -> docker-compose"
# zinit light "docker/compose"

zinit load agkozak/zsh-z
# Ref: zdharma/fast-syntax-highlighting
# Note: Use wait 1 second works for kubectl
#zinit wait lucid for \
#  atinit"ZINIT[COMPINIT_OPTS]=-C; zicompinit; zicdreplay" \
#    zdharma-continuum/fast-syntax-highlighting \
##  atload"zpcdreplay" wait"1" \
#    #OMZP::kubectl \
#  blockf \
#    zsh-users/zsh-completions \
#  atload"!_zsh_autosuggest_start" \
#    zsh-users/zsh-autosuggestions \
#  as"completion" is-snippet \
#    https://github.com/docker/cli/blob/master/contrib/completion/zsh/_docker \
#    https://github.com/docker/compose/blob/master/contrib/completion/zsh/_docker-compose

# 语法高亮
zinit ice lucid wait='0' atinit='zpcompinit'
zinit light zdharma-continuum/fast-syntax-highlighting

# 自动建议
zinit ice lucid wait="0" atload='_zsh_autosuggest_start'
zinit light zsh-users/zsh-autosuggestions

# 补全
zinit ice lucid wait='0'
zinit light zsh-users/zsh-completions

# 加载 OMZ 框架及部分插件
zinit snippet OMZ::lib/completion.zsh
zinit snippet OMZ::lib/history.zsh
zinit snippet OMZ::lib/key-bindings.zsh
zinit snippet OMZ::lib/theme-and-appearance.zsh
zinit snippet OMZ::plugins/colored-man-pages/colored-man-pages.plugin.zsh
zinit snippet OMZ::plugins/sudo/sudo.plugin.zsh
#zinit snippet OMZ::plugins/git-flow/git-flow.plugin.zsh
zinit snippet OMZ::plugins/mvn/mvn.plugin.zsh
zinit snippet OMZ::plugins/tmux/tmux.plugin.zsh
#zinit snippet OMZ::plugins/tmuxinator/tmuxinator.plugin.zsh
zinit snippet OMZ::plugins/command-not-found/command-not-found.plugin.zsh
zinit snippet OMZ::plugins/pip/pip.plugin.zsh

zinit ice lucid wait='1'
zinit snippet OMZ::plugins/git/git.plugin.zsh

# Gitignore plugin – commands gii and gi
zinit ice wait"2" lucid
zinit load voronkovich/gitignore.plugin.zsh

zinit load djui/alias-tips

# Load a few important annexes, without Turbo
# (this is currently required for annexes)
zinit light-mode for \
    zdharma-continuum/zinit-annex-as-monitor \
    zdharma-continuum/zinit-annex-bin-gem-node \
    zdharma-continuum/zinit-annex-patch-dl \
    zdharma-continuum/zinit-annex-rust

### End of Zinit's installer chunk

eval "$(fasd --init auto)"

# 网络配置
DEFAULT_USER="user"
ZSH_DISABLE_COMPFIX="true"
export all_proxy=socks5://127.0.0.1:7890
host_ip=$(cat /etc/resolv.conf |grep "nameserver" |cut -f 2 -d " ")
export ALL_PROXY="http://$host_ip:7890"
# export DISPLAY=:0.0


# fzf
export FZF_DEFAULT_OPTS='--height 40% --layout=reverse --border'
export FZF_DEFAULT_OPTS="--height 40% --layout=reverse --preview '(highlight -O ansi {} || cat {}) 2> /dev/null | head -500'"
[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh
# Modified version where you can press
#   - CTRL-O to open with `open` command,
#   - CTRL-E or Enter key to open with the $EDITOR
fo() {
  IFS=$'\n' out=("$(fzf --preview 'cat {}' --query="$1" --exit-0 --expect=ctrl-o,ctrl-e)")
  key=$(head -1 <<< "$out")
  file=$(head -2 <<< "$out" | tail -1)
  if [ -n "$file" ]; then
    [ "$key" = ctrl-o ] && open "$file" || ${EDITOR:-vim} "$file"
  fi
}
# cd to selected directory
fd() {
  local dir
  dir=$(find ${1:-.} -path '*/\.*' -prune \
                  -o -type d -print 2> /dev/null | fzf +m) &&
  cd "$dir"
}
fe() {
  local files
  IFS=$'\n' files=($(fzf-tmux --query="$1" --multi --select-1 --exit-0))
  [[ -n "$files" ]] && ${EDITOR:-vim} "${files[@]}"
}


export PATH=$PATH:/home/erbiaoger/Seisflows/specfem2d/bin
# matlab
export PATH=/home/erbiaoger/.local/share/matlab/bin:$PATH
alias matlab="/home/erbiaoger/.local/share/matlab/bin/matlab"
# ranger
export RANGER_LOAD_DEFAULT_RC=FALSE
alias nav='ranger --choosedir=$HOME/.rangerdir; LASTDIR=`cat $HOME/.rangerdir`; cd "$LASTDIR"'
# fd2dmpi
export PATH=~/MyProjects/SWIT-1.0/bin:$PATH
export PYTHONPATH=~/MyProjects/SWIT-1.0/toolbox

# 映射 
alias nas='ssh -p 22 CSIM@192.168.3.26'
alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'
alias od='cd /Users/erbiaoger/Library/Group\ Containers/UBF8T346G9.OneDriveSyncClientSuite/OneDrive.noindex/OneDrive/Document/Obsidian'
alias toc='gh-md-toc --insert'
alias sshuser='ssh -NfL 1111:localhost:3333 user@192.168.3.10'
alias sshzhangzhiyu='ssh -NfL 2222:localhost:2222 zhangzhiyu@192.168.3.10'
alias md='mkdir -p'
alias m='matlab -nodesktop -nosplash -nodisplay -r'
alias p='python'
alias ls='exa -lm --icons --time-style=iso --no-permissions --no-user'
alias ld='exa -lm --icons --time-style=iso --no-permissions --no-user -D'
alias ll='exa -lm --icons --time-style=iso --no-permissions --no-user | grep "^-"'
alias l='exa -lm --icons --time-style=iso --no-permissions --no-user -s type'
alias lt='exa -lm --icons --time-style=iso --no-permissions --no-user --tree --level=2'
alias tn='tmux new -s'
alias tl='tmux ls'
alias ta='tmux attach -t'
alias tk='tmux kill-session -t'
alias ts='tmux switch -t'
alias tj='tmux split-window'
alias th='tmux split-window -h'
alias d='vimdiff'
alias dc='vimdiff -c'
alias du='vimdiff -u'
alias dg='git diff'
alias ins='sudo apt install'
alias ya='yay -S'
alias doc='cd /mnt/c/Users/erbia/OneDrive/文档'
alias dow='cd /mnt/c/Users/erbia/Downloads'
alias mt='matlab -nodesktop -nosplash -nodisplay'
alias mtr='matlab -nodesktop -nosplash -nodisplay -r'
alias mp='matlab -nodesktop -nosplash'
alias mpr='matlab -nodesktop -nosplash -r'
alias nv='nvim'
alias jan='fasd -a'        # any
alias js='fasd -si'       # show / search / select
alias jd='fasd -d'        # directory
alias jf='fasd -f'        # file
alias jsd='fasd -sid'     # interactive directory selection
alias jsf='fasd -sif'     # interactive file selection
alias j='fasd_cd -d'     # cd, same functionality as j in autojump
alias jz='fasd_cd -d -i' # cd with interactive selection
alias jdd='fasd -D' # 删除一个路径

alias v='jf -e vim'
#alias nv='jf -e nvim'
alias batf='jf -e bat'
alias catf='jf -e cat'
alias py3f="jf -e python3"
alias lsf="jd -e ls"
alias shf='jf -e sh'
alias commandf='jf -e command'

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/Users/zhangzhiyu/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/Users/zhangzhiyu/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/Users/zhangzhiyu/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/Users/zhangzhiyu/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

# 网络配置
DEFAULT_USER="user"
ZSH_DISABLE_COMPFIX="true"
export all_proxy=socks5://127.0.0.1:7890
host_ip=$(cat /etc/resolv.conf |grep "nameserver" |cut -f 2 -d " ")
export ALL_PROXY="http://$host_ip:7890"
# export DISPLAY=:0.0


# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

