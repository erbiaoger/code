````shell
" 背景配色  R65  G: 68  U: 65
call plug#begin('~/.vim/plugged')
Plug 'azabiong/vim-highlighter'
let HiSet   = 'f<CR>'           " normal, visual
let HiErase = 'f<BS>'           " normal, visual
let HiClear = 'f<C-L>'          " normal
let HiFind  = 'f<Tab>'          " normal, visual

Plug 'dhruvasagar/vim-table-mode'
let g:table_mode_corner='|'
function! s:isAtStartOfLine(mapping)
	  let text_before_cursor = getline('.')[0 : col('.')-1]
	    let mapping_pattern = '\\V' . escape(a:mapping, '\\')
		  let comment_pattern = '\\V' . escape(substitute(&l:commentstring, '%s.*$', '', ''), '\\')
		    return (text_before_cursor =~? '^' . ('\\v(' . comment_pattern . '\\v)?') . '\\s*\\v' . mapping_pattern . '\\v$')
		endfunction

		inoreabbrev <expr> <bar><bar>
		          \\ <SID>isAtStartOfLine('\\|\\|') ?
		          \\ '<c-o>:TableModeEnable<cr><bar><space><bar><left><left>' : '<bar><bar>'
		inoreabbrev <expr> __
		          \\ <SID>isAtStartOfLine('__') ?
		          \\ '<c-o>:silent! TableModeDisable<cr>' : '__'

" tmux-vim
Plug 'christoomey/vim-tmux-navigator'
let g:tmux_navigator_no_mappings = 1
nnoremap <silent> <c-l> :TmuxNavigateLeft<cr>
nnoremap <silent> <c-j> :TmuxNavigateDown<cr>
nnoremap <silent> <c-k> :TmuxNavigateUp<cr>
nnoremap <silent> <c-h> :TmuxNavigateRight<cr>
nnoremap <silent> <c-p> :TmuxNavigatePrevious<cr>
let g:tmux_navigator_save_on_switch = 2

" fzf
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
nnoremap <leader>fo :Files<CR>
nnoremap <leader>fif :Rg<CR>

" vimtex
Plug 'lervag/vimtex'
let g:tex_flavor = 'latex'
let g:vimtex_compiler_latexmk_engines={'_':'-xelatex'}
let g:vimtex_compiler_latexrun_engines={'_':'xelatex'}
let g:vimtex_view_method='zathura'
let g:vimtex_quickfix_mode = 1
set conceallevel=1
let g:tex_conceal='abdmg'

" nerdtree
Plug 'preservim/nerdtree'
nnoremap <C-n> :NERDTreeToggle<CR>
nnoremap <C-f> :NERDTreeFind<CR>
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 1 && isdirectory(argv()[0]) && !exists('s:std_in') |
    \\ execute 'NERDTree' argv()[0] | wincmd p | enew | execute 'cd '.argv()[0] | endif
let g:NERDTreeDirArrowExpandable = '▸'
let g:NERDTreeDirArrowCollapsible = '▾'

"markdown插件
Plug 'godlygeek/tabular'
Plug 'plasticboy/vim-markdown'
let g:vim_markdown_math = 1
let g:vim_markdown_folding_level = 5
let g:vim_markdown_folding_disabled = 1


" markdown-toc
Plug 'mzlogin/vim-markdown-toc'
let g:vmt_auto_update_on_save = 0

" markdown-preview
Plug 'iamcco/markdown-preview.nvim', { 'do': { -> mkdp#util#install() }, 'for': ['markdown', 'vim-plug']}
let g:mkdp_auto_start = 0
let g:mkdp_auto_close = 1
let g:mkdp_refresh_slow = 0
let g:mkdp_command_for_global = 0
let g:mkdp_open_to_the_world = 0
let g:mkdp_open_ip = ''
let g:mkdp_browser = ''
let g:mkdp_echo_preview_url = 0
let g:mkdp_browserfunc = ''
let g:mkdp_preview_options = {
    \\ 'mkit': {},
    \\ 'katex': {},
    \\ 'uml': {},
    \\ 'maid': {},
    \\ 'disable_sync_scroll': 0,
    \\ 'sync_scroll_type': 'middle',
    \\ 'hide_yaml_meta': 1,
    \\ 'sequence_diagrams': {},
    \\ 'flowchart_diagrams': {},
    \\ 'content_editable': v:false,
    \\ 'disable_filename': 0
    \\ }
let g:mkdp_markdown_css = ''
let g:mkdp_highlight_css = ''
let g:mkdp_port = ''
let g:mkdp_page_title = '「${name}」'
let g:mkdp_filetypes = ['markdown']
nmap <C-m> <Plug>MarkdownPreviewToggle

" gruvbox
Plug 'morhetz/gruvbox'

" YouCompleteMe
"apt install build-essential cmake vim-nox python3-dev
"apt install mono-complete golang node\\sigma default-\\deltak npm
Plug 'ycm-core/YouCompleteMe'

"	"安装代码(python)规范插件
"	Plug 'tell-k/vim-autopep8'
"	autocmd FileType python noremap <buffer> <F8> :call Autopep8()<CR>

"	"安装代码(python)补全插件
"	Plug 'davidhalter/jedi-vim'
"
"安装底部状态栏
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#left_sep = ' '
let g:airline#extensions#tabline#left_alt_sep = '|'
let g:airline#extensions#tabline#formatter = 'unique_tail_improved'

```
Plug 'preservim/tagbar'

```

call plug#end()

colorscheme gruvbox
set t_Co=256
let g:gruvbox_contrast_dark='hard'
set background=dark    " Setting dark

set number			" 设置左侧行号
set hlsearch		" 设置高亮搜索
hi Search ctermbg=DarkRed
set wrapscan
set relativenumber	" 设置以所在行为编号0的行号
set ruler			" 设置标尺
syntax on
set wrap			" 设置自动换行
set wildmenu
set showmode
set showcmd
"set statusline=%-0120.120(%F%m%)%-0120.120([%l,%c]%)%p%%
set laststatus=2
set history=100
set cursorline
hi CursorLine ctermbg=black
set cursorcolumn
hi CursorColumn ctermbg=black
" set list
" set listchars=tab:>-
" set listchars=eol:$,tab:>-
hi SpecialKey ctermfg=DarkRed guifg=grey70
set noexpandtab
set shiftwidth=4
set tabstop=4				" 一个Tab的大小
set softtabstop=4
set autoindent
set scrolloff=8				" 光标滚动是距离底的行数
set autowrite
set showmatch				" 光标遇到括号高亮另一半
set cc=100					" 标尺线
set encoding=utf-8

" noremap <M-l> :tabp<CR>
" noremap <M-h> <C-PageDown>

autocmd BufNewFile * exec ":call SetTitle()"
func SetTitle()
if expand("%:e")=='sh' || expand("%:e")=='py'
if expand("%:e")=='sh'
call setline(1,"#!/usr/bin/zsh")
call setline(2,"#")
elseif expand("%:e")=='py'
call setline(1,"#!/usr/bin/env python")
call setline(2,"#")
endif
call setline(3,"#**#")
call setline(4,"#Author:		erbiaoger")
call setline(5,"#Email:			[643747954@qq.com](mailto:643747954@qq.com)")
call setline(6,"#Date:			".strftime("%Y-%m-%d"))
call setline(7,"#FileName:		".expand("%"))
call setline(8,"#Description:	The purpose of the script is")
call setline(9,"#Copyright(C):	".strftime("%Y")." All rights reserved")
call setline(10,"#**#")
call setline(11,"#")
call setline(12,"")
elseif expand("%:e")=='c' || expand("%:e")=='cpp'
call setline(1,"//**#")
call setline(2,"//Author:		erbiaoger")
call setline(3,"//Email:		[643747954@qq.com](mailto:643747954@qq.com)")
call setline(4,"//Date:			".strftime("%Y-%m-%d"))
call setline(5,"//FileName:		".expand("%"))
call setline(6,"//Description:	The purpose of the script is")
call setline(7,"//Copyright(C):	".strftime("%Y")." All rights reserved")
call setline(8,"//**#")
if expand("%:e")=='c'
call setline(9,"#include <stdio.h>")
call setline(10,"")
elseif expand("%:e")=='cpp'
call setline(9,"#include <iostream>")
call setline(10,"using namespace std;")
endif
call setline(11,"")
call setline(12,"")
call setline(13,"int main(void)")
call setline(14,"{")
call setline(15,"	")
call setline(16,"	")
if expand("%:e")=='c'
call setline(17,"	return 0;")
call setline(18,"}")
elseif expand("%:e")=='cpp'
call setline(17,"	system(\"pause\")")
call setline(18,"	return 0;")
call setline(19,"}")
endif
endif
endfunc
autocmd BufNewFile * normal G

func! CompileRunGccr()
exec "w"
if &filetype == 'c'
set splitbelow
exec "!gcc % -o %<"
:term ./%< && rm ./%<
" :normal i
elseif &filetype == 'cpp'
set splitbelow
exec "!g++ -std=c++11 % -Wall -o %<"
:term ./%< && rm ./%<
" :normal i
elseif &filetype == 'sh'
:!time bash %
elseif &filetype == 'python'
set splitbelow
:term python %
" :normal i
elseif &filetype == 'matlab'
set splitbelow
:term
" :normal i
elseif &filetype == 'javascript'
set splitbelow
:term node %
" :normal i
elseif &filetype == 'typescript'
set splitbelow
:term node %<.js
" :normal i
elseif &filetype == 'go'
set splitbelow
:term go run %
" :normal i
elseif &filetype == 'rust'
set splitbelow
:term cargo run
" :normal i
elseif &filetype == 'html'
silent! exec "!reload -p 4444&"
silent! exec "!vimb 127.0.0.1:4444"
elseif &filetype == 'markdown'
exec "MarkdownPreview"
endif
endfunc
func! CompileRunGccR()
exec "w"
if &filetype == 'c'
set splitbelow
exec "!gcc % -o %<"
:sp
:res -10
:term ./%< && rm ./%<
" :normal i
elseif &filetype == 'cpp'
set splitbelow
exec "!g++ -std=c++11 % -Wall -o %<"
:sp
:res -10
:term ./%< && rm ./%<
" :normal i
elseif &filetype == 'sh'
:!time bash %
elseif &filetype == 'python'
set splitbelow
:sp
:res -10
:term python %
" :normal i
elseif &filetype == 'matlab'
set splitbelow
:sp
:res -10
:term
" :normal i
elseif &filetype == 'javascript'
set splitbelow
:sp
:res -10
:term node %
" :normal i
elseif &filetype == 'typescript'
set splitbelow
:sp
:res -10
:term node %<.js
" :normal i
elseif &filetype == 'go'
set splitbelow
:sp
:res -10
:term go run %
" :normal i
elseif &filetype == 'rust'
set splitbelow
:sp
:res -5
:term cargo run
" :normal i
elseif &filetype == 'html'
silent! exec "!reload -p 4444&"
silent! exec "!vimb 127.0.0.1:4444"
elseif &filetype == 'markdown'
exec "MarkdownPreview"
endif
endfunc
map <silent> <leader>r :call CompileRunGccr()<CR>
map <silent> <leader>R :call CompileRunGccR()<CR>


map <silent> C "+y
map <silent> P "+p
map <silent> H ^
map <silent> L $
map <silent> J 5j
map <silent> K 5k
nnoremap <silent> S :w<CR>
nnoremap <silent> Q :q<CR>
nnoremap <silent> T :term<CR>
nnoremap <silent> <C-t> :tabnew<CR>
inoremap <A-h> <Left>
inoremap <A-l> <Right>
inoremap <A-j> <Down>
inoremap <A-l> <Up>
inoremap <silent> <C-h> <Left>
inoremap <silent> <C-l> <Right>
inoremap <silent> <C-j> <Down>
inoremap <silent> <C-l> <Up>
inoremap <buffer> <silent> ;o <Esc>o
inoremap <buffer> <silent> ;E ''<++><Esc>4hi
inoremap <buffer> <silent> ;e ""<++><Esc>4hi
inoremap <buffer> <silent> ;r ()<++><Esc>4hi
inoremap <buffer> <silent> ;R {}<++><Esc>4hi
inoremap <buffer> <silent> ;m <++>
inoremap <buffer> <silent> ;f <Esc>/<++><CR>:nohlsearch<CR>c4l
inoremap <buffer> <silent> ;F <Esc>/<++><CR>N:nohlsearch<CR>c4l
inoremap <buffer> <silent> ;s <Esc>:w<CR>
inoremap <buffer> <silent> ;q  + <Esc>hi <Esc>2la
inoremap <buffer> <silent> ;w  = <Esc>hi <Esc>2la
inoremap <buffer> <silent> ;; <Esc>
inoremap <buffer> <silent> jj <Esc>

autocmd Filetype c inoremap <buffer> <silent> jz //
autocmd Filetype cpp inoremap <buffer> <silent> jz //
autocmd Filetype matlab inoremap <buffer> <silent> jz %

autocmd Filetype python inoremap <buffer> <silent> jd def (<++>):<Esc>6hi
autocmd Filetype python inoremap <buffer> <silent> jc class ():<Esc>2hi
autocmd Filetype python inoremap <buffer> <silent> jz """  ""<Esc>2hi
autocmd Filetype python inoremap <buffer> <silent> jZ """<cr><++><cr>"""<Esc>2ka
autocmd Filetype markdown inoremap <buffer> <silent> jG ---<Enter><Enter>
autocmd Filetype markdown inoremap <buffer> <silent> jb **** <++><Esc>F

*hi
autocmd Filetype markdown inoremap <buffer> <silent> jx ~~~~ <++><Esc>F~hi
autocmd Filetype markdown inoremap <buffer> <silent> jx ** <++><Esc>F*

i
autocmd Filetype markdown inoremap <buffer> <silent> j

```
 `` <++><Esc>F
```

i
autocmd Filetype markdown inoremap <buffer> <silent> j~

```
<Enter><++><Enter>
```

<Enter><Enter><++><Esc>4kA
autocmd Filetype markdown inoremap <buffer> <silent> j\| <Esc>a\| <++>
autocmd Filetype markdown inoremap <buffer> <silent> jv <center>  </center><Esc>F<hi
autocmd Filetype markdown inoremap <buffer> <silent> jV $$\begin{matrix}<Esc>o\end{matrix}$$<Esc>ka
autocmd Filetype markdown inoremap <buffer> <silent> jt

<Esc>F]i
autocmd Filetype markdown inoremap <buffer> <silent> jh $  $ <++><Esc>F$hi
autocmd Filetype markdown inoremap <buffer> <silent> jH $$  $$<Esc>2hi
autocmd Filetype markdown inoremap <buffer> <silent> j8 \cdot
autocmd Filetype markdown inoremap <buffer> <silent> j* \times
autocmd Filetype markdown inoremap <buffer> <silent> jD \mathrm{d}{  }<++><Esc>F}hi
autocmd Filetype markdown inoremap <buffer> <silent> jd \partial{}<Esc>i
autocmd Filetype markdown inoremap <buffer> <silent> j- \frac{  }{ <++> } <++><Esc>F{2hi
autocmd Filetype markdown inoremap <buffer> <silent> jB \mathbf{  }<Esc>hi
autocmd Filetype markdown inoremap <buffer> <silent> jz <!--  --> <Esc>F>3hi
autocmd Filetype markdown inoremap <buffer> <silent> jp

autocmd Filetype markdown inoremap <buffer> <silent> jm

autocmd Filetype markdown inoremap <buffer> <silent> j1 #
autocmd Filetype markdown inoremap <buffer> <silent> j2 ##
autocmd Filetype markdown inoremap <buffer> <silent> j3 ###
autocmd Filetype markdown inoremap <buffer> <silent> j4 ####
autocmd Filetype markdown inoremap <buffer> <silent> j5 #####
autocmd Filetype markdown inoremap <buffer> <silent> j6 ######
````

