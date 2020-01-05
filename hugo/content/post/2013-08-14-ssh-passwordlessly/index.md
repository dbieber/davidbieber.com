+++
title = "ssh Passwordlessly"
subtitle = ""

date = 2013-08-14T00:00:00
lastmod = 2013-08-14T00:00:00
draft = false
authors = ["admin"]

tags = []
summary = ""

[image]
  caption = ""
  focal_point = "Right"
+++

You're used to ssh-ing into machine **B** from machine **A** by typing:

`ssh username@B.com`<br>
`password`

Now you wish to ssh from machine **A** into machine **B** without having to enter your password. Just follow these steps.

1. Create a public/private <a href="http://en.wikipedia.org/wiki/RSA_(algorithm)">RSA</a> key pair by issuing the unix command `ssh-keygen`. Do not enter a passphrase.

2. Put the private key on machine **A** (the machine you wish to ssh from). Usually the best place to put it is in `~/.ssh`.

3. On machine **B**, create the file `~/.ssh/authorized_keys`. Add the public key as a line to this new file. You can do this with the command `cat public_key >> authorized_keys` or by copy/pasting.

4. On machine **A**, create the file `~/.ssh/config`. Add the following to this file.
`Host anyname`<br>
`HostName B.com`<br>
`User username`<br>
`IdentityFile ~/.ssh/private_key`

That's it. You can now passwordlessly ssh into machine **B** from machine **A** just by typing:

`ssh anyname`

And as a bonus, you can now <a href="http://en.wikipedia.org/wiki/Secure_copy">`scp`</a> to and from machine **B** passwordlessly as well.

There's [loads](http://nerderati.com/2011/03/simplify-your-life-with-an-ssh-config-file/) [more](http://linux.die.net/man/5/ssh_config) that you can do with an ssh config file. So have a Google, and see what you can see.

------

I'm posting this online because it's something I wish I had known sooner. Hopefully you can benefit from it.

This post isn't the whole story though! Using an ssh key without a passphrase (a la step 1) is dangerous; if anyone gains access to your private key then they'll be able to ssh into machine B as you. The solution is to (back in step 1) create a passphrase for your private key, and then <a href="http://en.wikipedia.org/wiki/Ssh-agent">ssh-agent</a> will remember your decrypted private key so that you don't need to enter your password too often.
