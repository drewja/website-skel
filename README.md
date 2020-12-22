A tool for quickly bootstrapping a development environment with one command. Basically just copies files from the skel directory into one of your choosing with a handy cli that once installed can be run from anywhere.

QUICK START

    someguy@computer:~/somedir$ git clone https://github.com/drewja/website-skel

    someguy@computer:~/somedir/website-skel$ cd website-skel

    # install the cli to copy your skeleton
    someguy@computer:~$./install.sh
    # use ./remove.sh to uninstall

USAGE: (from anywhere on your filesystem)

    someguy@computer:~/mydir$ webskel

CLI will ask for a name and location of your new project

cd into the newly created project


    someguy@computer:~/mydir$ cd my-project
    someguy@computer:~/mydir/my-project$ npm install -i
    ...
    someguy@computer:~/mydir/my-project$ npm run start &
    ...
    #open your editor of choice
    someguy@computer:~/mydir/my-project$ code .


Editing the skel directory:

Every time you make changes to your skeleton you must run uninstall.sh followed by install.sh and your good to go.

TODO: support multiple skeletons selectable from the cli or maybe multiple cli's that are bound to different skeleton files.