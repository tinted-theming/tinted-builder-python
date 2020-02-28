# Base16 One Dark
# Author: Base24

set -l color00 '#282c34'
set -l color01 '#3f4451'
set -l color02 '#4f5666'
set -l color03 '#545862'
set -l color04 '#9196a1'
set -l color05 '#abb2bf'
set -l color06 '#e6e6e6'
set -l color07 '#ffffff'
set -l color08 '#e06c75'
set -l color09 '#d19a66'
set -l color0A '#e5c07b'
set -l color0B '#98c379'
set -l color0C '#56b6c2'
set -l color0D '#61afef'
set -l color0E '#c678dd'
set -l color0F '#be5046'

set -U FZF_DEFAULT_OPTS "
  --color=bg+:$color01,bg:$color00,spinner:$color0C,hl:$color0D
  --color=fg:$color04,header:$color0D,info:$color0A,pointer:$color0C
  --color=marker:$color0C,fg+:$color06,prompt:$color0A,hl+:$color0D
"
