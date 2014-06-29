syntax on
map <F5> :w <CR> :!g++ %; ./a.out <CR>
nmap <C-H> :noh <CR>
" sprawdza czy edytowany plik nie ulegl zmianie i go aktualizuje
map <F6> :checkt <CR>
set backspace=indent,eol,start
set autoindent
set incsearch
set hlsearch
set number
set mouse=a
set nocompatible
set background=dark
set wildmenu
set ruler
runtime ftplugin/man.vim
set ignorecase
set hidden
set autoread<
"->>>>>>>>>>>>>> zmienne do zawijania textu formatowania itd

"set linebreak
"set showbreak=>>
"set tw=0 columns=100
"set wm=0
"set formatoptions+=t

augroup myvimrc
    au!
    au BufWritePost .vimrc,_vimrc,vimrc,.gvimrc,_gvimrc,gvimrc so $MYVIMRC | if has('gui_running') | so $MYGVIMRC | endif
augroup END

let mapleader=','
map <leader>ew :e <C-R>=expand("%:p:h") . "/" <CR>
map <leader>es :sp <C-R>=expand("%:p:h") . "/" <CR>
map <leader>ev :vsp <C-R>=expand("%:p:h") . "/" <CR>
map <leader>et :tabe <C-R>=expand("%:p:h") . "/" <CR>

set laststatus=2
let g:airline_powerline_fonts=1
set guifont=Ubuntu\ Mono\ for\ VimPowerline\ 12
set t_Co=256

" Configuration the NERDTree
execute pathogen#infect()
filetype plugin indent on
helptags ~/.vim/doc
let g:NERDTreeWinPos = 'left'
let g:NERDTreeWinSize = '40'
nmap <silent> <F10> :NERDTreeToggle<CR>
imap <silent> <F10> <ESC>:NERDTreeToggle<CR>
cmap <silent> <F10> <ESC>:NERDTreeToggle<CR>

" Configuration the TagBar
let g:tagbar_left = 0
let g:tagbar_width = 40
nmap <silent> <F12> :TagbarToggle<CR>
imap <silent> <F12> <ESC>:TagbarToggle<CR>
cmap <silent> <F12> <ESC>:TagbarToggle<CR>


" configuration the syntastic




let &path.="src/include,include,/usr/include,src,inc,src/inc,src,"

" Configuration youcoplateme->listtoogle
let g:lt_location_list_toggle_map = '<leader>l'
let g:lt_quickfix_list_toggle_map = '<leader>q'
let g:lt_height = 10
let g:ycm_global_ycm_extra_conf = "~/.vim/.ycm_extra_conf.py"
