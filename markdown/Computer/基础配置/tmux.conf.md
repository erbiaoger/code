# .tmux.conf

```bash
#Window操作
# Ctrl+B c //创建一个新窗口
# Ctrl+B & //关闭当前窗口
# Ctrl+B p //切换到上一个窗口
# Ctrl+B n //切换到下一个窗口
# Ctrl+B 窗口号 //使用窗口号切换窗口(例如窗口号为1的, 则C-b 1)
# Ctrl+B , //重命名当前窗口，便于识别各个窗口
#Panel操作
# Ctrl+B % //横向分Terminal(左右)
# Ctrl+B " //纵向分Terminal
# Ctrl+B 方向键 //则会在自由选择各面板
# Ctrl+B x //关闭当前pane
# Ctrl+B q //显示面板编号
#Session操作
# Ctrl+B s //列出所有会话
# Ctrl+B d //detach当前session(可以认为后台运行)

# r 重新加载 ~/.tmux.conf
unbind r
bind r source-file ~/.tmux.conf

# 将按键前缀由 C-b 改为 C-l
# unbind C-b
# set -g prefix C-l

# l 将前缀按键按入客户端窗口
bind-key l send-prefix

# k 关闭 window，关闭前确认
bind-key k confirm kill-window

# K 关闭 server，关闭前确认
bind-key K confirm kill-server

# |/v 水平切分窗口
unbind %
bind-key | splitw -v

# _/-/h 垂直切分窗口
unbind '"'
bind-key - splitw -h

# 历史记录限制
set -g history-limit 5000

# 操作状态栏时的默认键盘布局，可以设置为 vi 或 emacs
set-option -g status-keys vi

# 选择会话
bind-key s choose-tree

# 同步执行命令
bind-key e setw synchronize-panes on
bind-key E setw synchronize-panes off

# 设置tmux状态显示
set-option -g status-left-length 150
set-option -g allow-rename off
set -g status-bg '#333333'
set -g status-fg '#ffffff'
setw -g window-status-current-format '#[bg=#ff0000, fg=#ffffff, bold]*[#I] #W*'
setw -g window-status-format '#[bg=#0000ff, fg=#ffffff] [#I] #W '
set-option -g status-left "#[fg=green]#(echo [)#[fg=cyan]#(/bin/bash /home/bg/install/tmux.sh)#[fg=green]#(echo ][)#[fg=yellow]#{session_name}#[fg=green]#(echo ])"
set-option -g status-right '#[fg=green][#[fg=colour230]#(date)#[fg=green]#(echo ])'
set -g status-interval 1

# 支持鼠标
set -g mouse on

# 复制模式中的默认键盘布局，可以设置为 vi 或 emacs
set-window-option -g mode-keys vi

# 拷贝粘贴
bind p paste-buffer
bind-key -T copy-mode-vi 'v' send -X begin-selection
bind-key -T copy-mode-vi 'y' send -X copy-selection-and-cancel

# Smart pane switching with awareness of Vim splits.
# See: <https://github.com/christoomey/vim-tmux-navigator>
is_vim="ps -o state= -o comm= -t '#{pane_tty}' \\
    | grep -iqE '^[^TXZ ]+ +(\\\\S+\\\\/)?g?(view|n?vim?x?)(diff)?$'"

bind-key -n C-h  if-shell  "$is_vim"  "send-keys C-h"  "select-pane -L"
bind-key -n C-j   if-shell  "$is_vim"  "send-keys C-j"   "select-pane -D"
bind-key -n C-k  if-shell  "$is_vim"  "send-keys C-k"  "select-pane -U"
bind-key -n C-l   if-shell  "$is_vim"  "send-keys C-l"   "select-pane -R"
bind-key -n C-\\\\   if-shell  "$is_vim"  "send-keys C-\\\\"  "select-pane -l"
```