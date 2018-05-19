# secureChat
This application is designed to use emberjs and a firebase database to create and manage various tasks 


## Libraries Used
```
    Client-side
        from tkinter import messagebox
        from Tkinter import *
        import socket, ssl
        import select
        import sys
        import OpenSSL
        from threading import Thread

        from Crypto.PublicKey import RSA
        from Crypto.Signature import PKCS1_PSS
        from Crypto.Hash import SHA
    Server-side
        from socket import AF_INET, socket, SOCK_STREAM
        from threading import Thread
        import subprocess, ssl
```

## Installation..
* `git clone git@github.com:rawalshree/secureChat.git`
* `cd secureChat`

## Running / Development..
### Once you have the app installed, run...
    * `1) Start the server in a widow`
        * `Start the server in a shell a terminal widow`
    * `2) Enter.. python3 servertest.py `
    * `How to end server on Mac`
    * `lsof -i :33000 kill -9 38632`
    *`In order to run a client version, enter the command..
    * `python3 clienttest.py "localhost" 33000`

## Additional Git Commands
### How to add access and add from a remote branch
### Creates a new branch miles and switches to it...
* `git checkout -b <branch name>`
### Verify you're on the new branch
* `git status`
### Add any changes from the new remote branch to the master
* `git add .`
* `git commit -m "initiating changes from remote branch to master`
* `git remote add origin git@github.com:rawalshree/secureChat.git`
* `git push -u origin <remotebranchName>`
### Switch back to the master
* `git checkout master`
* `git merge <remotebranchName>`
* `git push -u origin master`


### Also, if you want to clone from the remote branch you can
* `git clone -b <branch_name> git@github.com:rawalshree/secureChat.git`

### If you accidently pushed the wrong repo, and need to revert to an old repository
### state or in other words to the previous commit...

### Enter the command...
* `git log`
### This will display a log of all the recent git commits with their
### corresponding commit SHA-1 ID's, which git uses as its version control
Choose the corresponding commit, and instead of using..
* `git fetch`
We can simply click on commits on the repository bar above the branch names..
Then click the commit  SHA-1 ID, and then click browse files...
Then simply download a zip, or..
* `git clone` from the correct corresponding commit repo


  # Created By:
  ## [Shree Rawal](https://github.com/rawalshree)
  ## [Jonathon Moubayed ](  https://github.com/jonmoubayed)
   ## [Diego Franchi](  https://github.com/diegofranchi)
    ## [Imran Gosla](  https://github.com/imrangosla)
    ## [Miles McCloskey](  https://github.com/milesjmccloskey)
    ## [Chase Moyniham](  https://github.com/chasemoy)

  # Team Leaders:
    * ` Shree Rawal,`
    * ` Email:000@gmail.com`
    * ` Jonathon Moubayed,`
      * `Email: jonmoubayed@csu.fullerton.edu`
   
  

    
    
   
   

  

