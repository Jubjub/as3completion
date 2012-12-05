function! As3Complete(findstart, base)
    if a:findstart
        " locate the start of the word
        let line = getline('.')
        let start = col('.') - 1
        while start > 0 && line[start - 1] =~ '\a'
            let start -= 1
        endwhile
        return start
    else
python << EOF
import vim
import as3completion
reload(as3completion)
vim.command('let res = %s' % as3completion.complete(vim.eval('a:base')))
vim.command('echo res')
vim.command('return res')
EOF
    endif
endfun

set omnifunc=As3Complete

