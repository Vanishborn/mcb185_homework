
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

