python << EOF
import as3completion
reload(as3completion)
as3completion.main()
EOF

function! As3Complete(findstart, base)
    if a:findstart
        " locate the start of the word
        let line = getline('.')
        let start = col('.') - 1
        while start > 0 && line[start - 1] =~ '\a' && line[start - 1] != ' '
            let start -= 1
        endwhile
        return start
    else
python << EOF
import vim
import as3completion
page = vim.current.buffer[:]
position = vim.current.window.cursor
position = (position[1], position[0] - 1)
start = vim.eval('a:base')
vim.command('let res = %s' % as3completion.complete(page, position, start))
vim.command('return res')
EOF
    endif
endfun
set omnifunc=As3Complete
