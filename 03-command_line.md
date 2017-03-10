# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

>>* `pwd` - display current directory
* `mkdir <directory name>` - create a new directory
* `rmdir` - Directory should be empty to use this. Use `rm -r <directory name>` to delete a directory with content (including subfolders)
 `cd <directory path>` - change directory to given directory path
 `ls -lt` - display files and directories ordered by modification date, descending
 `touch <file name>` - create a 0 byte empty file
 `rm <file name` - delete file
 `mv <source file name> <new file name>` - renaming is the same command as moving a file within the same directory
 `ls -a` - lists hidden files on Unix
 `cp <source file path> <destination directory>` - copies file to another directory
 `less <file name>` - quick editor to read contents of a file (read-only). Better than more. Less is more :)
 `grep -n apple myfile.txt`      # include the line number
 `grep -i apple myfile.txt`       # case insensitive matching
 `grep --color apple myfile.txt`  # color the matching text
 `grep -v apple myfile.txt`	# return lines that don't contain apple
 `grep -R apple mydirectory/`	# search for apple in any file in mydirectory
 Here is a very nice website with quick examples of widely used Unix commands: [http://www.oliverelliott.org/](http://www.oliverelliott.org/article/computing/ref_unix/#)
---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

>> `ls` - simple file and directory listing. Does not display hidden files
>> `ls -a` - list all files/directories including hidden ones  
`ls -l` - listing, long format. Displays attributes such as owner, permissions, modification times, size
`ls -lh`  - long format, with size displayed in human readable format. Such as in KB, MB, GB etc.
`ls -lah` - long format, including hidden files/directories with size displayed in a human readable format  
`ls -t`  - listing sorted by the modification time. Most recently modified file shown first
`ls -Glp` - `G` argument colorizes output, so that directories are displayed in a different color. `l` for long format. `p` puts a slash('/') after directory names


---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

>> `ls -1` - displays each entry of a separate line. This helpful if you are piping the output of this to another function. ex: iterate through files using a for loop
`ls -ltr` - lists files in ascending order by modification time
`ls -ltR` - lists files in subdirectories as well
`ls -m` - displays files/directories as a comma separated list. This could be useful when creating python lists or JSON
`ls -ld */` - display only directories in the current directory

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs allows one to pipe output from one command to a command doesn't accept a standard input stream.
copy files that contain the word git to another directory:
`grep -l git *.md | xargs -I {} cp {} temp/`
