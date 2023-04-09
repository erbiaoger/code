# Fig pre block. Keep at the top of this file.
[[ -f "$HOME/.fig/shell/zshrc.pre.zsh" ]] && builtin source "$HOME/.fig/shell/zshrc.pre.zsh"
# 网络配置
DEFAULT_USER="user"
ZSH_DISABLE_COMPFIX="true"
export all_proxy=socks5://127.0.0.1:7890
host_ip=$(cat /etc/resolv.conf |grep "nameserver" |cut -f 2 -d " ")
export ALL_PROXY="http://$host_ip:7890"
export DISPLAY=:0.0
export http_proxy=http://127.0.0.1:7890
export https_proxy=http://127.0.0.1:7890
export no_proxy="localhost, 127.0.0.1"


# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
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
#
# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
# export PATH="~/anaconda3/bin:$PATH"  # commented out by conda initialize
# export PATH="~/anaconda3/bin:$PATH"  # commented out by conda initialize



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
# autojump
# [[ -s ~/.autojump/etc/profile.d/autojump.sh ]] && . ~/.autojump/etc/profile.d/autojump.sh
export PATH=$PATH:/usr/share/miniconda3/bin/
# su
export CWPROOT=/home/erbiaoger/MyProjects/Seisflows/su
export PATH=$PATH:$CWPROOT/bin
# specfem2d
# export PATH=$PATH:/home/erbiaoger/Seisflows/specfem2d/bin
# matlab
# export PATH=/home/erbiaoger/.local/share/matlab/bin:$PATH
# alias matlab="/home/erbiaoger/.local/share/matlab/bin/matlab"
# ranger
export RANGER_LOAD_DEFAULT_RC=FALSE
alias nav='ranger --choosedir=$HOME/.rangerdir; LASTDIR=`cat $HOME/.rangerdir`; cd "$LASTDIR"'


# 映射 
alias sf='seisflows'
alias GUI='python -m http.server 8800'
alias ip=ipython
alias md='mkdir -p'
alias m='matlab -nodesktop -nosplash -nodisplay -r'
alias p='python'
alias python='python3'
alias sz='source ~/.zshrc'
alias vz='vim ~/.zshrc'
alias la='exa -lm --icons --time-style=long-iso --no-permissions --no-user -a'
alias ls='exa -lm --icons --time-style=long-iso --no-permissions --no-user'
alias l='exa -lm --icons --time-style=long-iso --no-permissions'
alias lf='exa -lm --icons --time-style=long-iso --no-permissions --no-user | fzf'
alias lt='exa -lm --icons --time-style=long-iso --no-permissions --no-user --changed'
alias tr='exa -lm --icons --time-style=long-iso --no-permissions --no-user --tree --level=2'
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
alias ca='conda activate'



# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/erbiaoger/miniconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/erbiaoger/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/home/erbiaoger/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/erbiaoger/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<


export PATH="$HOME/.yarn/bin:$HOME/.config/yarn/global/node_modules/.bin:$PATH"

# Load a few important annexes, without Turbo
# (this is currently required for annexes)
zinit light-mode for \
    zdharma-continuum/zinit-annex-as-monitor \
    zdharma-continuum/zinit-annex-bin-gem-node \
    zdharma-continuum/zinit-annex-patch-dl \
    zdharma-continuum/zinit-annex-rust

### End of Zinit's installer chunk
#
#
# 这里两条都要放入配置文件里 ---start
#alias 'proxy'='export all_proxy=socks5://127.0.0.1:7891' # 打开代理
#alias 'unproxy'='unset all_proxy' # 关闭代理
# 这里两条都要放入配置文件里 ---end

# Fig post block. Keep at the bottom of this file.
[[ -f "$HOME/.fig/shell/zshrc.post.zsh" ]] && builtin source "$HOME/.fig/shell/zshrc.post.zsh"

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
