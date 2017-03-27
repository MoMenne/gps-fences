
execute pathogen#infect()
syntax on
filetype plugin indent on


set smartindent
set expandtab
set tabstop=2
set softtabstop=2 " default to 2 spaces for the soft tab
set shiftwidth=2

" turn on the mouse
set mouse=a

set relativenumber  "use relative line numbers
set number "but still show the current absolute line num

" resize splits when inactive
" set winwidth=84
" set winheight=5
" set winminheight=5
" set winheight=999

" matches all [{(
set showmatch

" improves vim search
set incsearch
set hlsearch

set runtimepath^=~/.vim/bundle/ctrlp.vim

let NERDTreeDirArrows=0
" after building your container run this at vim command line and restart vim 
" :helptags ~/.vim/bundle/ctrlp.vim/doc

