== Description ==

Fiji is an open source image processing application, oriented towards scientific research and large data sets. Fiji provides software libraries and end-user applications constructed as plugins. Popular plugins include 2d, 3d and 4d linear and non-linear image registration; 4d image visualization; particle tracking; image segmentation with machine learning; object reconstruction from series of images by automatic, semi-automatic and manual means; quantitative measurements such as particle analysis and image statistics; and batch processing.

Fiji runs on the JVM, and supports 6 different JVM languages (java, jython, clojure, jruby, beanshell and javascript) and a DSL (ImageJ macro language). We target 3 operating systems (Linux, MacOSX and Windows) in both 32-bit and 64-bit flavors. The whole of fiji is built by a single command, and the entire code base is under version control with git (https://fiji.sc/cgi-bin/gitweb.cgi?p=fiji.git). All libraries and commands are extensively documented in a wiki with extensive examples, parameter descriptions and both written and video tutorials (https://fiji.sc).

The core developers of Fiji are scientific researchers at the Max Plank Institute, the ETH Zurich, the Massachussets Institute of Technology, the Pasteur Institute in Paris, the Laboratory for Molecular Biology in Cambridge (UK), the University of Wisconsin-Madison, Howard Hughes Medical Institute at Janelia Farm, and the European Molecular Biology Laboratory, among others. These institutions host regular hackathons and generously finance servers and developers.


== Why is your organization applying to participate in GSoC 2011? What do you hope to gain by participating? ==

Fiji has grown enormously over the last two years. Statistics collected by our automatic updater (result of Google Summer of Code 2009) indicates that Fiji is in use in just about every major research institution around the world. Several publications in scientific journals are citing Fiji and Fiji's plugins (see https://fiji.sc/Publications). The wiki that hosts Fiji's documentation got 23,169 unique visitors this past February 2011.

All this growth comes at a cost: there is now a lot of demand for specific enhancements and new features.

The first example is the demand for implementations of very novel computer vision algorithms for image segmentation, which make practical the extraction of data from very large image data sets. The automatization of 3d and 4d image acquisition has become the new standard, and now researchers confront the processing of very long 4d series and very large 3d volumes. For example, the imaging of the complete embryonic development of a zebra fis with a temporal resolution of minutes, and the neural circuit reconstruction from nanometer-scale data obtained with electron microscopy.

A second example is the Script Editor (result of Google Summer of Code 2009) which supports 7 languages that can run in the JVM. Having so many languages supported enables a wide variety of researchers to be immediately at home, getting work done with their preferred language. This success has led to several petitions to add further languages such as Scala and Groovy, and to enhance the editor with transparent automatisms for discovering classes and methods available in Fiji's libraries.

The Google Summer of Code program captures the attention of students worldwide, facilitating the discovery of ideal students for our open source software project. We hope that we'll entice great students beyond their contribution this Summer and perhaps recruit them later for further development of scientific image processing applications.


== Did your organization participate in past GSoCs? If so, please summarize your involvement and the successes and challenges of your participation ==

In 2009, we crafted and submitted an application for Fiji as a hosting institution, which was awarded 3 student positions. Two of these students went on to develop two key components of Fiji: the Fiji Updater and the Script Editor. The third student abandoned soon after starting, but his project was partially completed by the mentor (support for [[MATLAB]] scripts). The two successful projects greatly improved Fiji.

The Fiji Updater enabled one-click package updates and completely changed the way in which image processing software developers and the end-user scientists interact. The feedback loops became faster and far less error prone, having removed the hassle of ensuring consistency in the versions of the necessary software libraries for the execution of the plugins and applications of interest.

The Script Editor lowered the barrier to get work done for the researcher in need of programming, particularly regarding batch-processing of large collections of image files. Currently it supports 7 languages and we are planning on adding two more. Albert Cardona, the Fiji application admin, was the project mentor for the student that created the Script Editor. 

== Does your organization have an application template you would like to see students use? If so, please provide it now. Please note that it is a very good idea to ask students to provide you with their contact information as part of your template. Their contact details will not be shared with you automatically via the GSoC 2011 site. ==

Application for a Google Summer of Code project with Fiji.

Name:
Email:
IRC nickname in irc.freenode.net:
Personal website:

1. What do you study? Please be brief; 2-3 sentences and a link to a webpage would do great.

2. Have you contributed to open source projects in the past? Please list each one, with links to the source repositories. Add a short description in 2 or 3 sentences about your contribution to each. Indicate who reviewed your code, if appropriate (name and email).

3. Have you used Fiji? For what purposes? Please explain in 2 or 3 sentences.

4. Have you downloaded and compiled the Fiji source code repositories? Answer yes/no.

5. Have you read the proposals from the ideas page at https://fiji.sc/GSoC_2011_Ideas ? Answer yes/no.

6. What project do you propose to work on during the Summer of code? With which mentor? Do you know the mentor via email, IRC or personally? Please be specific and try to be concise. If necessary please include links to diagrams, cartoons and pictures, with appropriate descriptions of what are they and how are they relevant. Please give your proposal to a friend or colleage and see if he understands it before pasting it below; it will help you craft a better proposal.

7. Why should we choose to work with you and not some other student? In what way are you exceptional? Please be brief.

8. Anything else you'd like us to know? (Optional)


== What criteria did you use to select the individuals who will act as mentors for your organization? Please be as specific as possible ==

All proposed mentors are core Fiji developers. These developers are both academics with experience supervising undergraduate and graduate students, and have a vested interest (for their own research) in seeing the student's project completed. In short, mentors are both skilled and motivated.


== What is your plan for dealing with disappearing students? ==

The proposed mentors are all core Fiji developers. The projects listed in our ideas page are projects that Fiji developers would sooner or later tackle themselves. In the event that a student quits, the project will be continued by a mentor.

To facilitate the task, mentors will lay down a plan together with the student, with specific weekly milestones. Students will be advised to document their code as they go, as the means to explain the code to themselves and to the mentor. The documentation is a key component of the student's evaluation, and will aid the mentor--or any Fiji developer--to pick up where the student left.


== What is your plan for dealing with disappearing mentors? ==

The proposed mentors are all dedicated core Fiji developers. They are also all in academia, either PhD students, postdocs, or faculty. It is in their best interest that they take students to aid them develop components of the Fiji software for their own research purposes. They have all mentored undergraduates, master students and PhD students in the past two years.

In the unlikely event that a mentor finds it unavoidable to quit the mentorship, another Fiji developer will take the role.


== What steps will you take to encourage students to interact with your project's community before, during and after the program? ==

We will select students with an interest in image processing. All mentors are part of scientific research laboratories in need of developing specific applications, which are then released to the world with Fiji. Before the project starts, we will figure out the best way for the student to start using Fiji for his own purposes, in whatever manner possible to avoid interfering with their current duties.

During the Summer, we will encourage students to communicate with mentors via the #fiji-devel IRC channel in irc.freenode.net and the fiji-devel@googlegroups.com mailing list. In this way, the Fiji developers community will participate of the conversation and aid in guiding the student in the right direction. In the process, the student will get to know a variety of members of the Fiji developers community, seeding the possibility of starting other projects with them later on.

If the students are bright and willing, we will have every reason to hire them as intern students or master students in our own research labs. Their contribution will enrich Fiji through software development for scientific projects.

== Anything else you'd like to tell us? ==

The Google Summer of Code was a fantastic experience. We are looking forward to participate again.
