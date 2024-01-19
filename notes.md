
# Jan 11

mac shortcuts
in command line
```
open [filename] -a [application name]
```
allows you to open a file using designated application

right click on a file and get info will allow you to change the default application you use to open that type of file

```
ls -F
```
will show directories with /

```
printenv SHELL
open -a bbedit .zshrc

```

in the .zshrc file
add alias

```
alias ls="ls -F"
alias bb="open -a bbedit"
```

save the .zshrc file will allow ls to be ls -F and bb to be open -a bbedit

# Jan 16

use tab complete all the time, it's good
cd ~ will bring me back to home directory

to get the content of a variable, put $ ahead of it to dereference it
printenv $HOME

cat returns all content of file to screen
head shows first 10 lines of the file
tail shows last 10 lines of the file
head -x shows first x lines of the file
tail -x shows last x lines of the file

less and more are close
but less is more
use less
it has more functions

if you are opening multiple files using less or zless with *
use :n to go to next file
use shift g to go to the end of current file

standard output goes to terminal
standard input is keyboard to terminal

the ">" can save things to files
it can save command outputs as well
