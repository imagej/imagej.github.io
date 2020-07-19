There are plenty of good reasons why one might need to synchronize all the branches of multiple repositories:

* Development happens on multiple continents
* Some servers might have some unscheduled downtime from time to time
* Windows users might want to have a fast access to a Git-SVN mirror

This last point is quite a sore point: [http://msysgit.github.io/ Git for Windows]' support for importing Subversion repositories suffers from many performance problems, ranging from the general I/O weakness of the platform to the need to use MSys Perl to be able to use the <code>SVN.pl</code> module.

Alas, a solution is nigh!

We solved exactly those problems in the ImageJ project. There is a [http://jenkins.imagej.net/view/Synchronizers/job/ImageJ-synchronizer/ Jenkins job] to synchronize the ImageJ repositories with each other, using {{GitHub|org=scijava|repo=scijava-scripts|path=git-synchronizer.sh|label=this script}}. Sadly the script is a little more complex than I hoped, but it does the job reliably and to be honest, it is a little more tricky than I first thought: when there are updates from only one of the repositories, they should be forced. However, there might be contradicting updates in which case nothing may be forced. Of course, such a script&mdash;especially when it is a little more complex than the author hoped&mdash;also has to take precautions not to be overzealous in corner-cases the author might have not thought about. That is the reason why it makes extra-sure to look for updates it might have missed in earlier rounds and does '''not''' force those updates. [[Jenkins]] executes this job every 5 minutes which is why it is very important that the much faster <code>git://</code> protocol is used for fetching the branches instead of the slower ssh-based protocol used for pushing.

As for the git-svn mirror, we have a Jenkins job that too. It is driven by a&mdash;thankfully quite simple&mdash;[https://github.com/imagej/imagej/blob/9227a1048426dc2c1b312be4e8a80c1b726a04ce%5E/bin/jenkins-git-job.sh script]. This script makes sure that the remote information is set up such that all branches in <code>refs/remotes/</code> (i.e. the ones maintained by git-svn) are pushed into the <code>refs/heads/svn/</code> namespace. Jenkins polls the Subversion repository and only runs the job when new commits are available.

Both jobs (and likewise the siblings of the ImageJ synchronizer used to synchronize the {{GitHub|repo=imglib|label=ImgLib2}} and {{GitHub|repo=fiji|label=Fiji}} repositories) proved quite useful and stable in our development.

The synchronizer for Git repositories was designed with flexibility in mind: the information which repositories should be synchronized is passed as command-line parameters. Should it be required, it will be easy to adjust the synchronizer for the Git-SVN mirror to be as flexible.

[[Category:News]]
[[Category:ImageJ2]]
