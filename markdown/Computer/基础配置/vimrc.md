# .vimrc

```bash
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
	    let mapping_pattern = '\\\\V' . escape(a:mapping, '\\\\')
		  let comment_pattern = '\\\\V' . escape(substitute(&l:commentstring, '%s.*$', '', ''), '\\\\')
		    return (text_before_cursor =~? '^' . ('\\\\v(' . comment_pattern . '\\\\v)?') . '\\\\s*\\\\v' . mapping_pattern . '\\\\v$')
		endfunction

		inoreabbrev <expr> <bar><bar>
		          \\\\ <SID>isAtStartOfLine('\\\\|\\\\|') ?
		          \\\\ '<c-o>:TableModeEnable<cr><bar><space><bar><left><left>' : '<bar><bar>'
		inoreabbrev <expr> __
		          \\\\ <SID>isAtStartOfLine('__') ?
		          \\\\ '<c-o>:silent! TableModeDisable<cr>' : '__'

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
    \\\\ execute 'NERDTree' argv()[0] | wincmd p | enew | execute 'cd '.argv()[0] | endif
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
    \\\\ 'mkit': {},
    \\\\ 'katex': {},
    \\\\ 'uml': {},
    \\\\ 'maid': {},
    \\\\ 'disable_sync_scroll': 0,
    \\\\ 'sync_scroll_type': 'middle',
    \\\\ 'hide_yaml_meta': 1,
    \\\\ 'sequence_diagrams': {},
    \\\\ 'flowchart_diagrams': {},
    \\\\ 'content_editable': v:false,
    \\\\ 'disable_filename': 0
    \\\\ }
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
"apt install mono-complete golang node\\\\sigma default-\\\\deltak npm
Plug 'ycm-core/YouCompleteMe'
```