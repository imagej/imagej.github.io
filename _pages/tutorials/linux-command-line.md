---
title: Linux command line tutorial
---

## Connecting to the cluster

We will use SSH (secure shell) to connect to the cluster. On macOS we need to simply open a terminal window (under {% include bc path="Applications|Utilities" %}), on PC we may need to download an ssh client such as [Putty](http://www.chiark.greenend.org.uk/~sgtatham/putty/).

In the terminal type:

{% highlight shell %}
ssh madmax.mpi-cbg.de
{% endhighlight %}

and enter your password:

{% highlight shell %}
tomancak@madmax.mpi-cbg.de's password:   
{% endhighlight %}

Now you are on the cluster!

{% highlight shell %}
Last login: Sun May 19 09:01:24 2013 from 10.1.7.16  
"Platform HPC" 3.1 (build 7211) Management Node  
Welcome to the MPI-CBG cluster masternode.  
[tomancak@madmax ~]$
{% endhighlight %}

## Moving around

**pwd** - *print working directory*

{% highlight shell %}
[tomancak@madmax ~]$ pwd  
/home/tomancak
{% endhighlight %}

**cd** - *change directory*

{% highlight shell %}
[tomancak@madmax ~]$ cd /projects  
[tomancak@madmax projects]$ pwd  
/projects
{% endhighlight %}

**\~** - *tilda* means home directory

{% highlight shell %}
[tomancak@madmax projects]$ cd ~  
[tomancak@madmax ~]$ pwd  
/home/tomancak
{% endhighlight %}

**/** - *slash* demarcates directories and by itself means the root directory

{% highlight shell %}
[tomancak@madmax ~]$ cd /  
[tomancak@madmax /]$ pwd  
/
{% endhighlight %}

**.** - current directory, if we want to, for example, execute a script in the current directory we do it like this:

{% highlight shell %}
./executable_script  
{% endhighlight %}

This tells the interpreter to look for the file `executable_script` in the current directory and not somewhere else.

**..** - one directory up

{% highlight shell %}
[tomancak@madmax projects]$ cd ..  
[tomancak@madmax /]
{% endhighlight %}

**pressing tab** - auto-completion, we don't need to type long names of directories, start typing the name and press **tab** and the linux system will either auto-complete or show you the options you have.

{% highlight shell %}
[tomancak@madmax ~]$ cd /projects/toman + press tab  
[tomancak@madmax ~]$ cd /projects/tomancak_lightsheet  
[tomancak@madmax tomancak_lightsheet]$
{% endhighlight %}

## Manipulating files

**ls**

**more**

**tail**

**nano**

**mv**

**cp**

**scp**

**rm**

**mkdir**

**rmdir**

**gunzip**

**tar**

## Permissions

**chmod**

**su**

**sudo**

## Pipes and redirects

**\|**

**&gt;**

**wc**

## Misc

**which**

**top**

**watch**

**grep**

**sort**

**find**

**man**

## Using it on the cluster

Here we put all of that goodness to work to make our life on a cluster easier.

Once we submit the jobs, we want to monitor the progress. For example **bjobs -r** gives us an output summarising our running jobs. If there are many, it's not that useful. How about counting them?

{% highlight shell %}
bjobs -r | wc -l  
160
{% endhighlight %}

More usefully, we have 160 jobs running. Still how about the pending ones? We can do that:

{% highlight shell %}
bjobs -r | grep PEND | wc -l  
40
{% endhighlight %}

Ok 40. Now, how many jobs actually finished successfully? Let's say they create some *.tif* files in `../../ouput`:

{% highlight shell %}
ls ../../output/*.tif | wc -l  
200
{% endhighlight %}

Good, looks like 200 are finished. It's tempting to keep pressing enter on those commands but it's also tiresome. Using:

{% highlight shell %}
watch -n5 'ls ../../output/*.tif | wc -l' 
{% endhighlight %}

outputs continuously:

{% highlight shell %}
Every 5.0s: ls ../../output/*.tif | wc -l                                                                                               
Mon May 20 21:16:37 2013  
180
{% endhighlight %}

i.e. we get the number of files automatically updated every 5 seconds (without the -n paramater, every 2s by default).
