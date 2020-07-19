== Connecting to  the cluster ==

We will use SSH (secure shell) to connect to the cluster. On Mac OSX we need to simply open a terminal window (under Applications->Utilities), on PC we may need to download an ssh client such as [http://www.chiark.greenend.org.uk/~sgtatham/putty/ Putty].

In the terminal type:

 ssh madmax.mpi-cbg.de

and enter your password
 
 tomancak@madmax.mpi-cbg.de's password: 
 
Now you are on the cluster

 Last login: Sun May 19 09:01:24 2013 from 10.1.7.16
 "Platform HPC" 3.1 (build 7211) Management Node
 Welcome to the MPI-CBG cluster masternode.
 [tomancak@madmax ~]$

== Moving around ==

'''pwd''' - ''print working directory''

 [tomancak@madmax ~]$ pwd
 /home/tomancak

''' cd ''' - ''change directory''

 [tomancak@madmax ~]$ cd /projects
 [tomancak@madmax projects]$ pwd
 /projects

'''~''' - ''tilda'' means home directory

 [tomancak@madmax projetcs]$ cd ~
 [tomancak@madmax ~]$ pwd
 /home/tomancak

'''/''' - ''slash'' demarcates directories and by itself means the root directory

 [tomancak@madmax ~]$ cd /
 [tomancak@madmax /]$ pwd
 /

'''.''' - current directory, if we want to for example execute a script in the current directory we do it like this:

 ./executable_script
 
This tells the interpreter to look for the file executable_script in the current directory and not somewhere else.

'''..''' - one directory up

 [tomancak@madmax projects]$ cd ..
 [tomancak@madmax /]

''' pressing tab ''' - auto-completion, we don't need to type long names of directories, start typing the name and press '''tab''' and the linux system will either auto-complete or show you the options you have

 [tomancak@madmax ~]$ cd /projects/toman + press tab
 [tomancak@madmax ~]$ cd /projects/tomancak_lightsheet
 [tomancak@madmax tomancak_lightsheet]$

== Manipulating files ==

'''ls'''

'''more'''

'''tail'''

'''nano'''

'''mv'''

'''cp'''

'''scp'''

'''rm'''

'''mkdir'''

'''rmdir'''

'''gunzip'''

'''tar'''

== Permissions ==

'''chmod'''

'''su'''

'''sudo'''

== Pipes and redirects ==

'''|'''

'''>'''

'''wc'''

== Misc ==

'''which'''

'''top'''

'''watch'''

'''grep'''

'''sort'''

'''find'''

'''man'''

== Using it on the cluster ==

Here we put all of that goodness to work to make our life on a cluster easier.

Once we submit the jobs we want to monitor the progress. For example '''bjobs -r''' gives us an output summarising our running jobs. If there are many its not that useful. How about counting them?

 bjobs -r | wc -l
 160

More useful, we have 160 jobs running. Still how about the pending ones? We can do that:

 bjobs -r | grep PEND | wc -l
 40

Ok 40. Now, how many jobs actually finished successfully? Lets say they create some ''.tif'' files a few directories down

 ls ../../output/*.tif | wc -l
 200

Good, looks like 200 are finished. Its tempting to keep pressing enter on those commands but its also tiresome. Using

 watch -n5 'ls ../../output/*.tif | wc -l' 

outputs continuously

 Every 5.0s: ls ../../output/*.tif | wc -l                                                                                             
 Mon May 20 21:16:37 2013
 180

i.e. we get the number of files automatically updated every 5 seconds (without the -n paramater every 2s by default).
