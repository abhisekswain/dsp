# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > 
**⌘Cmd + K:** Clears the screen  
**Top:** Displays active processes. Press q to quit  
**less:** Deliver output of file in screen size chunks  
**[command-a] | [command-b]:** Run command A and pipe output to command B  
**[command] > [file]:** Push output to file, it will get overwritten  
**[command] > >[file]:** Append output to existing file  
**pushd:** saves the current working directory in memory so it can be returned to at any time  
**popd:** returns to the path at the top of the directory stack  
**cat [options[ [filenames]:** reads files sequentially, writing them to standard output  
**grep “literal string” filename:** searches for specific string in file  


---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > **ls** - list with no option list files and directories in bare format where we won’t be able to view details like file types, size, modified date and time, permission and links  
**ls -a** - lists all files including those that are hidden    
**ls -l** - long format. Provides a list showing the permissions, number of inodes, the owner and the group, the file size, the last accessed date and time and file name    
**ls -lh** -  lists file in long format in byte sized chunks    
**ls -lah** - lists all files including hidden ones in long format in byte sized chunks  
**ls -t** - sorts files according to modification time (newest first)    
**ls -Glp** - lists files in long format, does not display group name and directories are marked by appending / to them


---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > REPLACE THIS TEXT WITH YOUR RESPONSE

 

