# .zshrc

```bash
 # install ripgrep
 # sudo apt install ripgrep
 
 DEFAULT_USER="user"
 ZSH_DISABLE_COMPFIX="true"
 export all_proxy=socks5://127.0.0.1:7890
 
 export PATH=$PATH:~/.config/nvim/nvim/bin
 # Path to your oh-my-zsh installation.
 export ZSH=$HOME/.oh-my-zsh
 
 ZSH_THEME="ys"
 
 # Add wisely, as too many plugins slow down shell startup.
 plugins=(
 git
 pip
 sudo
 
 # 代码错误修正
 # thefuck
 
 # sudo apt install autojump
 autojump
 
 # 直接在终端使用浏览器搜索，可以百度 谷歌
 web-search
 
 #可以记录我退出终端时所在的路径，再次打开时还在这个路径
 last-working-dir
 
 # 输入指令高度显示
 # git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
 zsh-syntax-highlighting
 
 # 自动补全
 # git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
 zsh-autosuggestions
 
 )
 source $ZSH/oh-my-zsh.sh
 
 export PATH=$PATH:~/.local/bin
 
 # echo '1511' | sudo -S cp -f ~/.vimrc ~/.zshrc ~/.condarc ~/.tmux.conf /mnt/e/BaiduNetdiskWorkspace/Linux > /dev/null 2>&1
 cd
 
 
 host_ip=$(cat /etc/resolv.conf |grep "nameserver" |cut -f 2 -d " ")
 export ALL_PROXY="http://$host_ip:7890"
 
 # export DISPLAY=:0.0
 
 # conda
 export PATH=$PATH:/home/erbiaoger/anacoda/bin
 
 # fzf
 export FZF_DEFAULT_OPTS='--height 40% --layout=reverse --border'
 export FZF_DEFAULT_OPTS="--height 40% --layout=reverse --preview '(highlight -O ansi {} || cat {}) 2> /dev/null | head -500'"
 [ -f ~/.fzf.zsh ] && source ~/.fzf.zsh
 # Modified version where you can press
 #   - CTRL-O to open with `open` command,
 #   - CTRL-E or Enter key to open with the $EDITOR
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
 [[ -s ~/.autojump/etc/profile.d/autojump.sh ]] && . ~/.autojump/etc/profile.d/autojump.sh
 # exa
 export PATH=$PATH:~/.local/share/exa/bin/
 # su
 export CWPROOT=/home/erbiaoger/geotools/su
 export PATH=$PATH:$CWPROOT/bin
 # specfem2d
 export PATH=$PATH:/home/erbiaoger/Seisflows/specfem2d/bin
 # matlab
 export PATH=/home/erbiaoger/.local/share/matlab/bin:$PATH
 alias matlab="/home/erbiaoger/.local/share/matlab/bin/matlab"
 # ranger
 export RANGER_LOAD_DEFAULT_RC=FALSE
 alias nav='ranger --choosedir=$HOME/.rangerdir; LASTDIR=`cat $HOME/.rangerdir`; cd "$LASTDIR"'
 
 ###----------------------------* Seisflows *----------------------------------##
 
 # Seisflows
 # export PATH=$PATH:~/Seisflows/SeisFlows-2DWD/scripts
 # export PYTHONPATH=~/Seisflows/SeisFlows-2DWD
 
 # export PATH=$PATH:/home/erbiaoger/Seisflows/seisflows-devel/scripts
 # export PYTHONPATH=/home/erbiaoger/Seisflows/seisflows-devel
 
 # export PATH=$PATH:~/Seisflows/seisflows/scripts
 # export PYTHONPATH=~/Seisflows/seisflows
 
 export PATH=$PATH:/home/erbiaoger/Seisflows/SeisFlows-Elastic-Foothill-Checkerboard/scripts
 export PYTHONPATH=/home/erbiaoger/Seisflows/SeisFlows-Elastic-Foothill-Checkerboard
 
 ##----------------------------------------------------------------------------##
 
 # 映射
 alias rg='ranger'
 alias v='vim'
 alias Q='exit'
 alias md='mkdir -p'
 alias m='matlab -nodesktop -nosplash -nodisplay -r'
 alias p='python'
 alias p3='python3'
 alias ipy='ipython3'
 alias sz='source ~/.zshrc'
 alias vz='vim ~/.zshrc'
 alias vv='vim ~/.vimrc'
 alias casf='conda activate seisflows'
 alias capy='conda activate python38'
 
 alias run='sfclean && sfsubmit'
 alias ter='gnome-terminal'
 
 alias l='exa -l'
 alias la='exa -al'
 alias laf='exa -al | fzf'
 alias ls='exa -l'
 alias lsf='exa -l | fzf'
 alias lt='exa -bghHliS'
 alias ltr='exa --tree --level=2'
 alias tn='tmux new -s'
 alias tl='tmux ls'
 alias ta='tmux attach -t'
 alias tk='tmux kill-session -t'
 alias ts='tmux switch -t'
 alias tj='tmux split-window'
 alias th='tmux split-window -h'
 alias d='diff'
 alias dc='diff -c'
 alias du='diff -u'
 alias dg='git diff'
 alias ins='sudo apt install'
 alias ya='yay -S'
 alias obs='cd /mnt/e/BaiduNetdiskWorkspace/Obsidian'
 alias bd='cd /mnt/e/BaiduNetdiskWorkspace'
 alias doc='cd /mnt/c/Users/erbia/OneDrive/文档'
 alias dow='cd /mnt/c/Users/erbia/Downloads'
 alias vd='vim DATA/Par_file'
 alias g='git'
 alias gcl='git clone'
 alias ga='git add'
 alias gcm='git commit -m'
 alias gpu='git push'
 alias grf='git reflog'
 alias gch='git checkout'
 alias mt='matlab -nodesktop -nosplash -nodisplay'
 alias mtr='matlab -nodesktop -nosplash -nodisplay -r'
 alias mp='matlab -nodesktop -nosplash'
 alias mpr='matlab -nodesktop -nosplash -r'
 alias nv='nvim'
 
 
 # madagascar
 # export DATAPATH=~/geotools/RSFDATA/
 # export RSFROOT=~/geotools/RSFSRC/rsf
 # source $RSFROOT/share/madagascar/etc/env.sh
 
 
 export NVM_DIR="$HOME/.nvm"
 [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
 [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
 
 # >>> conda initialize >>>
 # !! Contents within this block are managed by 'conda init' !!
 __conda_setup="$('/Users/erbiaoger/anaconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
 if [ $? -eq 0 ]; then
     eval "$__conda_setup"
 else
     if [ -f "/Users/erbiaoger/anaconda3/etc/profile.d/conda.sh" ]; then
         . "/Users/erbiaoger/anaconda3/etc/profile.d/conda.sh"
     else
         export PATH="/Users/erbiaoger/anaconda3/bin:$PATH"
     fi
 fi
 unset __conda_setup
 # <<< conda initialize <<<
 
 
 
```



