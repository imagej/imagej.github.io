{{GitMenu}}
=Repositories=
We are using git to write papers. Typical situation is the following: you start a directory on your laptop which you then turn into git repository, now you want to 'transfer' it to your work computer and keep tracking your changes from both places. For that you need to set-up an empty git-repo on a Internet/Intranet accessible server (aka in our case becherovka). 

Here are the steps :

1. initialize a bare repository on becherovka

<source lang="bash">git --git-dir=/path/my-new-repo.git init --bare</source>

2. Register that repository as a remote repository on your laptop by issuing this command inside the repository

<source lang="bash">git remote add origin becherovka:/path/my-new-repo.git</source>

(Note: If it fails, you already have an "origin" and need to use a different name. One can chnange the path to the remote "origin" by editing the url field in the .git/config.)

3. Push from the laptop to the remote repository

<source lang="bash">git push --all origin</source>

4. Now the final, extremely satisfactory step, clone the repository to your work computer 

<source lang="bash">git clone becherovka:/path/my-new-repo.git</source>

(Note: git clone creates a directory my-new-repo.git, so do it from the root of your git_papers folder.)

Magically, all the files flow onto your computer and you can track the changes to your manuscript performed from work or from home on your laptop by pulling and pushing until the next nasty merge conflict appears.

[[Category:Git]]
