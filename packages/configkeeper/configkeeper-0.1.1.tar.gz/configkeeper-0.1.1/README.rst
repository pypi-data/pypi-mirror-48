=============================
ConfigKeeper
=============================

.. image:: https://badge.fury.io/py/configkeeper.png
    :target: http://badge.fury.io/py/configkeeper


Description
-----------
ConfigKeeper provides a single backup command which copies a comfiguration file (.vimrc,
.bashrc, etc) into a repository and pushes it.

Usage
-----
.. code-block:: bash

    configkeeper path/to/config-file

Setup
-----
Clone the repository. Link the script somewhere under your `$PATH`.
The following assumes that `~/.local/bin` is added to your path.

.. code-block:: bash

    git clone https://gitlab.com/loxosceles/configkeeper.git ~/tools
    ln -s ~/tools/configkeeper/configkeeper ~/.local/bin/configkeeper

Create a repository for your config files you want to back up. The default is
`~/.local_configurations`.

