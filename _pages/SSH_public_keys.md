Often, it is inconvenient to input your password all the time when you push/pull via ssh (not using the [[Git#contrib|contrib user]]).

For such case, you can set up a public/private key pair.  Create them with

 ssh-keygen -t dsa

Usually, it is a good idea to create a public/private key pair for specific purposes, so that a single compromised key (see [http://www.debian.org/security/2008/dsa-1576 an example] how that can happen even if you did not do anything wrong) does not affect all of your machines.  So, change the default name ''id_dsa'' to something like ''id_dsa.fiji'' before hitting ''Return''.

You can password-protect your private key, in which case you have to use the program [[wikipedia:Ssh-agent|ssh-agent]], but is is usually more convenient to leave the password empty, in which case you are not even asked for it anymore.

Now you should have a file ''id_dsa.fiji.pub'' (the public key) in addition to ''id_dsa.fiji'' (the private key).

Add the public key (the single line contained in the file ''id_dsa.fiji.pub'') to the file ''$HOME/.ssh/authorized_keys'' on the '''remote''' computer, i.e. the computer you want to connect to without a password. '''Note!''' Make sure that the ''.ssh/'' directory as well as all contained files are owned by the correct user, and that ''.ssh/'' is accessible to the same user.

For convenience, you should now add a section like this to the file ''$HOME/.ssh/config'' on the '''local''' computer, i.e. the computer with the private key:

 Host fiji.sc
     User hacker
     IdentityFile /home/hacker/.ssh/id_dsa.fiji

Without this section, you would have to specify both the identity file as well as the user everytime you connect.  For even further convenience, you can add a nick name:

 Host fiji
     HostName fiji.sc
     User hacker
     IdentityFile /home/hacker/.ssh/id_dsa.fiji

With this, you can connect to the remote machine with

 ssh fiji

See also [http://help.github.com/win-set-up-git/ GitHub's documentation on SSH keys].

[[Category:Git]]
[[Category:Tutorials]]
