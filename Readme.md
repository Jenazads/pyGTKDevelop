# PyGTK

[![](/img/pygtk.jpg)](http://www.pygtk.org/)

## Installing jhBuild

OS: ubuntu 16.04

### Create Folder

In this directory we setup permissions

    sudo mkdir -p /opt/gnomeGtk
    sudo chown `whoami`:`whoami` /opt/gnomeGtk

### Create build folder

In this directory contains jhbuild's build.

    mkdir -p ~/checkout/gnomeGtk
    cd ~/checkout/gnomeGtk

### Checkout JHBuild module

we clone jhbuild repository.

    git clone git://git.gnome.org/jhbuild
    cd jhbuild
    ./autogen.sh
    make
    make install
    
### Add PATH variable

Manually, we add PATH to ~/.bashrc

    echo PATH=$PATH:~/.local/bin >> ~/.bashrc
    jhbuild sanitycheck

### Change config file

Our directory is ~/checkout/gnome2/jhbuild

    cd examples/
    cp sample.jhbuildrc ~/.jhbuildrc

### Verify Installed package

    sudo apt-get install apt-file
    sudo apt-file update
    jhbuild sysdeps --install
    jhbuild sanitycheck

### Errors

Some packages not found.

Solved:

    sudo apt install apt-file docbook-xsl build-essential git-core gettext libtext-csv-perl autotools-dev autoconf gettext pkgconf autopoint
    sudo apt-get install automake1.10 libtool libglib2.0-dev libgtk2.0-dev libxml2-dev

### Installing dependencies packages

    jhbuild build pygobject

There a list of errors during installation time:

#### First "error"

Required flex y bison.

Solved:

    sudo apt-get install flex
    sudo apt-get install bison

#### Second "error"

libtool: not found and libtool.m4

Solved:

    sudo apt-get install libtool-bin
    cp /usr/share/aclocal/libtool.m4 /opt/gnomeGtk/share/aclocal/

#### Third "error"

xsltproc: not found

Solved:
  
    sudo apt-get install xsltproc
    sudo apt-get install docbook-xsl build-essential git-core python-libxml2

#### Fourth "error"

m4macros/glib-getext.m4: m4_copy cant be overwritten

Solved:

    sudo apt-get install gettext gettext-devel gettext-base
    
### Installing other packages

    jhbuild build gtk+
    jhbuild gnome-weather
    jhbuild build dconf glib-networking gvfs libcanberra

No errors found.

This tutorial was taken of [jhBuild](https://wiki.gnome.org/Projects/Jhbuild/OnUbuntu)

## Examples

### Progress bar

Executing example [progress bar example](https://python-gtk-3-tutorial.readthedocs.io/en/latest/progressbar.html) from python-gtk-3 to verify the correct installation

![](/img/progressbar_example.jpg)()

### Snake GTK

Is a simple classic game Snake, developed en pyGTK.

![](/img/snakeGTK.jpg)()



