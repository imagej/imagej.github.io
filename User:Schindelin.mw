{{Userbox
| name = Johannes Schindelin
| gravatar = c2938f05cefad961fec000e7734c73ac
| title = Mother of Fiji
| affiliation = MPI-CBG Dresden (former), LOCI (former)
| loci = johannes-schindelin
| github = dscho
| openhub = gitte
| osrc = dscho
}}= [http://loci.wisc.edu/people/johannes-schindelin Johannes Schindelin] =

... was involved in the [[Fiji]] and [[ImageJ2]] projects helping with programming, algorithms, educating scientists about the fine points of scientific image analysis, planning experiments, and generally cheering up people.

= A short story about Fiji =

This story is not about [[wikipedia:Fiji|the island called ''Fiji'']]. This story is how [https://fiji.sc Fiji Is Just ImageJ] became born.

== The beginning ==

Back when I met [http://albert.rierol.net Albert Cardona] at the [[Conference 2006|first ImageJ conference]], it became pretty apparent pretty quickly that not only would we become good friends, but also that we had a lot of mutual respect for the work we had done so far. His biggest accomplishment was certainly [[TrakEM2]], but he had also worked on the macro interpreter (including a so-called [[Macro Interpreter|Command Line Interface]], which is a two-paned window for interactive macro evaluation) and had already turned to [[Jython_Scripting|Jython]] as a more powerful way to script ImageJ. At that time, I had not worked all that many years with ImageJ, but I already was maintainer of [[ImageJA]].

Over the years, we had more and more contact, meeting briefly in [http://genetics.biozentrum.uni-wuerzburg.de/main/ Würzburg] and later at a [[hackathon]] at [http://www.hhmi.org/bulletin/nov2007/chronicle/hackathon.html Janelia Farms], where we met with a bunch of enthusiastic people who all tried to bridge neuro science with software development (even if I was there, the article does not show a photo of me, because they did the article in the second week, and back then I was not on too-good terms with my employer, so I dared only ask to leave for one).

After an exciting hackathon, you almost always have to take a few breaths for a couple of weeks. In other words, you are no longer as productive, and if you are a workaholic like me, you fall into a depression.

It helped much to stay in contact and chat frequently. I did that a lot, especially with Albert, who kept improving TrakEM2. He also asked me constantly: "Johannes, have you tried it yet? You'll like it, it has a lot of features!"

But I hadn't.

The problem for me was not so much that I did not have time. I had a lot of time back then, because I had a lot of problems with my boss, then. Not because he is a bad person, not because I would not like him. Sometimes, two people just talk past each other, no matter what they do, even if they try hard not to. I digress.

The problem was that TrakEM2 seemed too tedious to set up. It required a database, and not just any database. It had to be [http://www.postgresql.org/ PostgreSQL], back then probably the only popular database system I was <u>not</u> familiar with. TrakEM2 also required a bunch of ''.jar'' files which you had to install before you could start.

Eventually, Albert told me: "Johannes, we need an installer for TrakEM2!"

We kept chatting about that over a couple of weeks, if not months. At some stage, Albert had done away with the requirement of the PostgreSQL database. It was still the most efficient way to handle your data if you needed to access them from multiple computers, but now you could also store the intermediate data in plain files.

Eventually, one dark December day in 2007 (and in Scotland, December <u>is</u> as dark as it gets) I gave in.

Out of frustration with my job, I had just started a distribution of [[Git]] for [https://git-for-windows.github.io/ Windows] which included making an installer, so I thought I could put together an installer pretty quickly.

The first step was to get a version of ImageJ and TrakEM2 and Java (we were 100% sure that we needed to ship Java with the installer, otherwise users would get into problems with their Java 1.1.8 not being able to run Java 5 classes, let alone run at a decent speed) to run on the main platforms: Windows, MacOSX and Linux. You might not consider Linux a major platform, but it was and still is the platform Albert and me are using.

After a couple of days I showed the result to Albert. So far, there was no installer, but it was a working ''portable application'', i.e. a big ''.zip'' file you could unpack and then double click on an executable which would run Java with all the parameters set correctly.

To this date, there is no installer, but hey, maybe we get one in another 3 years...

== The surprise ==

When I showed the result to Albert, he seemed to be happy. At least he did not run away in disgust. But I did not hear a lot about Fiji from his side, except that he needed a way to contribute.

Since I was heavily involved in the development of the version control software [http://git-scm.com/ Git] (contributing one or two useful things such as the config handling, the interactive rebase, the diffstat code, the low-level 3-way merge code, etc) it was natural that I kept all my work in a Git repository.

But I had no public place to put it, where Albert could have accessed it.

There was that computer in Würzburg -- lovingly dubbed ''Dumbo'', since we named all our computers after some movie persona, such as ''Agent Smith'', ''Minime'', and of course ''Dumbo'' -- which could be accessed from the outside, but it was already serving the ''Virtual Insect Brain Protocol'' and had only 128MB RAM which was way too little memory to handle a repository the size of Fiji.

So Albert got me access to his computer. Back then, that was in Los Angeles in Volker Hartenstein's group, and Volker seemed to be okay with the idea of having an easy-to-install TrakEM2 developed with my help.

By the way, this computer was called ''Instar'', but I have no idea whether that was only because it was used to develop things (''instar'' is a biological term describing a stage of larval development in insects).

I continued to work on this Fiji thing and even got it to run on MacOSX, which was one of my goals: I wanted to support all the major platforms. Windows, MacOSX and Linux. Both 32-bit and 64-bit. It should not matter which Operating System you happened to have, the software should Just Run<sup>tm</sup>.

After some weeks I was reasonably comfortable with Fiji and thought about wrapping this project up, since I had plans to work for Google.

Little did I know just how many people Albert told about this project. I thought it was really focused on TrakEM2, but as Albert's motto is (or at least back then, was) ''The sky is the limit'', he had told a few people at the Max-Planck Institute of Molecular Cell Biology and Genetics in Dresden. Sorry for the lengthy title, earlier I always referred to it as "the Max-Planck in Dresden", but there are three. The MPI-CBG just happens to be the biggest one in Dresden. And probably also one of the most important Max-Planck Institutes on this planet. But sorry, I digress.

At one point Albert told me. Apparently the good people in Dresden were not only interested in our little software project, but were actually enthusiastic. Enthusiastic enough that they provided us with a nice, beefy [[Pacific|server]], and offered to organize a [[hackathon]] to kick-start Fiji as a much bigger project!

== Fiji won't quit ==

TBD
