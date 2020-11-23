# Installation

    1. download VirtualBox 6.1.16 Software Developer Kit (SDK) from
        https://www.virtualbox.org/wiki/Downloads
        (check online guides for further instructions)

    2. install virtualbox python package which is reliant on the virtualbox SDK
        pip isntall virtualbox
        (https://github.com/sethmlarson/virtualbox-python)

    3. install FastApi
        pip install fastapi

    4. Start the server using either commands
        python -m uvicorn app:app --reload
        uvicorn app:app --reload


# used links

https://www.oracle.com/technical-resources/articles/it-infrastructure/admin-manage-vbox-cli.html

https://www.virtualbox.org/manual/ch08.html#vboxmanage-modifyvm

https://www.howopensource.com/2011/06/how-to-use-virtualbox-in-terminal-commandline/

https://coderwall.com/p/8m--dq/purge-deleted-hard-disks-from-virtual-box

https://www.cyberciti.biz/faq/how-to-set-up-ssh-keys-on-linux-unix/

https://forums.virtualbox.org/viewtopic.php?f=7&t=92707

http://www.cesareriva.com/how-to-install-the-virtualbox-sdk/

https://janakiev.com/blog/python-shell-commands/

https://github.com/sethmlarson/virtualbox-python/issues/104