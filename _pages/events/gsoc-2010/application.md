---
title: SoC 2010 Application
---

The application for Fiji (*Fiji Is Just ImageJ*)

## Description

Fiji stands for "Fiji is Just ImageJ". [ImageJ](/) is a public domain scientific image processing application sponsored by the National Institute of Health. ImageJ runs on the Java Virtual Machine and thus has direct access to numerous and diverse public java libraries.

Thanks to one of last year's Google Summer of Code projects, the individual components of Fiji are kept up-to-date with the Fiji Updater.

All Fiji project founders and contributors have written large plugin collections and ImageJ-centric applications. At some point, it was inevitable to merge our projects into a centralized and organized framework, which includes consistent and updated documentation for all its components.

For the creation of Fiji, beyond our own ImageJ-centric applications, we selected and tested a subset of the literally thousands of open source plugins that exist for ImageJ, and integrated them along with several open source libraries into a consistent framework. Plugins added capabilities beyond mere image processing, including image segmentation, image registration, 3D visualization of image volumes, and support for a variety of JVM-supported scripting languages (so far: javascript, jython, jruby, clojure and beanshell).

Fiji as a community is supported by a variety of scientific research institutions with vested interests on image processing, including but not limited to the Howard Hughes Medical Institute Janelia Farm, the Max Planck Institute of Molecular Cell Biology and Genetics in Dresden, and the Institute of Neuroinformatics of the University of Zurich and ETH Zurich.

## Why is your organization applying to participate in GSoC 2010? What do you hope to gain by participating?

There are numerous tasks suitable for independent small projects, that would enhance Fiji substantially. With the GSoC, we see an opportunity to bring young bright people to our project, using the projects as their entry point to both the human aspects of our community (particularly its frequent hackathons) and the project code base.

Of course, the Google Summer of Code also offers a perfect opportunity for students to tackle problems which are challenging enough to take more than just a couple of weeks of focused work. We fully expect fantastic projects in the field of image segmentation, classification, visualization and other image processing/analysis related subjects to be completed by the end of the summer.

Another benefit of the participation is the higher visibility of our project. Already last year, we noticed an upsurge in the website usage connected to the Google Summer of Code. When we fully integrated the results of the two projects, there was another peak in the statistics. For a non-commercial project like Fiji, this is the kind of publicity which is needed to let the users know that there is a free program they might want to use.

## If your organization participated in past GSoCs, please let us know the ratio of students passing to students allocated, e.g. 2006: 3/6 for 3 out of 6 students passed in 2006

Yes. We have participated in 2009. Out of 3 accepted students, we had 1 failure (the student was late starting the project, accepted a fulltime day-job in addition to the GSoC project, and was unable to accomplish even the simplest tasks set by his mentor), and 2 successes.

One of the two successful projects was to provide a script editor with syntax highlighting for all the scripting languages supported by Fiji: Jython, JRuby, Clojure, Javascript and BeanShell. As a bonus, the script editor supports writing Java plugins, too: [Script_Editor](https://fiji.sc/wiki/index.php/Script_Editor)

The other successful project was to provide a full-fledged plugin manager. During the project, it turned out that a full plugin manager would not be feasible, but the project's result was a versatile Fiji Updater, which was incorporated into mainline Fiji after some cleanups: [Update_Fiji](https://fiji.sc/wiki/index.php/Update_Fiji)

Unfortunately, we were not able to retain the students as regular contributors, which may, or may not, be due to the tight organization of their respective studies.

## If your organization has not previously participated in GSoC, have you applied in the past? If so, for what year(s)?

We applied in 2009 and got accepted.

## What license(s) does your project use?

GPL (GNU Public License), version 2, with the exception that all plugins are free to use whatever license they wish to, as long as no Fiji-specific code is used.

## What is the URL for your ideas page?

[SoC_2010_Ideas](/events/gsoc-2010)

## What is the main development mailing list for your organization? This question will be shown to students who would like to get more information about applying to your organization for GSoC 2010. If your organization uses more than one list, please make sure to include a description of the list so students know which to use

fiji-devel@googlegroups.com

## What is the main IRC channel for your organization?

\#fiji-devel on irc.freenode.net

## Does your organization have an application template you would like to see students use? If so, please provide it now. Please note that it is a very good idea to ask students to provide you with their contact information as part of your template. Their contact details will not be shared with you automatically via the GSoC 2010 site

[SoC_2010_Template](template)

## Who will be your backup organization administrator?

Johannes Schindelin and Pavel Tomancak

## What criteria did you use to select individuals as mentors? Please be as specific as possible

All of the prospect mentors of the Fiji team must have proven their competence by being author of at least one popular ImageJ plugin. This ensures that they have at least intermediate knowledge of Java, the ImageJ API, and the community process. It also guarantees that the mentors do not "go away", and that they can finish the project in the unfortunate case that the student "goes away".

## What is your plan for dealing with disappearing students?

In the event that a student abandons without completing his/her project, the Fiji community will pick up where the student left and continue the work without the student.

The mentors will setup the project together with the student, splitting the project into small chunks (milestones) that can be completed within reasonable spans of one or two weeks. Students will be advised and encouraged to document their code as they go, and code documentation (concise yet complete) will be one aspect of the evaluation. Proper documentation will enable any new student or any Fiji community member to pick up the project where the student left it.

## What is your plan for dealing with disappearing mentors?

All of our mentor candidates have scientific research jobs directly intertwined with the software application Fiji. It is in their prime interest to gather new members and to develop Fiji further. Both have mentored students outside the GSoC program in the recent years.

In the unlikely event that any of the mentors must drop off, another mentor will be arranged to step in. The Fiji community has plenty of people involved in all aspects of the software, that would happily take on the mentorship to help the students finish their chosen project. In all likelihood, such new mentor would already be acquainted with the student via the mailing list, and through direct interest in, and awareness of project activities.

## What steps will you take to encourage students to interact with your project's community before, during and after the program?

The Fiji team developed good communications on the mailing list as well as on IRC out of necessity: the members live in different countries. This culture of communication will help the students not to be afraid to ask for help and report their progress.

Further, the mentors will make sure to hold "office hours" on IRC, and will generally try to start the conversation if the students do not do that themselves.

Frequent informal and short status updates will be asked for, so that the students do not lose focus, and if (geographically) possible, the mentors will meet their students in person.

## What will you do to ensure that your accepted students stick with the project after GSoC concludes?

Fiji is a thriving image processing software, and it gains functions almost weekly. Students interested in image processing will find that it provides a good basis for their future careers (provided that they want to stay working on image processing).

The Fiji group has been meeting 3 to 4 times a year since June 2007 (before the Fiji project was actually started!), and we have one major meeting already planned for this year. Such meetings are hackathons: we sit down together and code, exchange image data for testing, and usually hold one or two workshops for users.

We will invite and fund the students who stick around to attend at least one hackathon. The environment in these hackathons is actively kept friendly and relaxed, while at the same time focused on the variety of scientific problems all members are trying to solve.
