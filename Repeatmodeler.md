# Installation and Usage of RepeatModeler
RepeatModeler is a frequently-used tool in genome annotation, but the intallation could be a bit troublesome.

## Installation
### 1 RepeatMasker
#### TRF
```sh
mkdir Repeatmodeler
cd Repeatmodeler
git clone https://github.com/Benson-Genomics-Lab/TRF.git
cd TRF;mkdir build
cd build
../configure
make
```
Error reported:
```sh
CDPATH="${ZSH_VERSION+.}:" && cd .. && ~/software/RepeatModeler/TRF/missing aclocal-1.16 
~/software/RepeatModeler/TRF/missing: line 81: aclocal-1.16: command not found
WARNING: 'aclocal-1.16' is missing on your system.
         You should only need it if you modified 'acinclude.m4' or
         'configure.ac' or m4 files included by 'configure.ac'.
         The 'aclocal' program is part of the GNU Automake package:
         <https://www.gnu.org/software/automake>
         It also requires GNU Autoconf, GNU m4 and Perl in order to run:
         <https://www.gnu.org/software/autoconf>
         <https://www.gnu.org/software/m4/>
         <https://www.perl.org/>
make: *** [../aclocal.m4] Error 127
```
Installing aclocal by conda:
```sh
conda create -n repeatmodeler automake autoconf
conda activate repeatmodeler
aclocal --version

# output
# aclocal (GNU automake) 1.17
# Copyright (C) 2024 Free Software Foundation, Inc.
# License GPLv2+: GNU GPL version 2 or later <https://gnu.org/licenses/gpl-2.0.html>
# This is free software: you are free to change and redistribute it.
# There is NO WARRANTY, to the extent permitted by law.

# Written by Tom Tromey <tromey@redhat.com>
#        and Alexandre Duret-Lutz <adl@gnu.org>.
```
Make again:
```sh
make
# The error still exists
CDPATH="${ZSH_VERSION+.}:" && cd .. && /bin/sh /nfs_fs/nfs1/sunwu/software/RepeatModeler/TRF/missing aclocal-1.16 
/nfs_fs/nfs1/sunwu/software/RepeatModeler/TRF/missing: line 81: aclocal-1.16: command not found
WARNING: 'aclocal-1.16' is missing on your system.
         You should only need it if you modified 'acinclude.m4' or
         'configure.ac' or m4 files included by 'configure.ac'.
         The 'aclocal' program is part of the GNU Automake package:
         <https://www.gnu.org/software/automake>
         It also requires GNU Autoconf, GNU m4 and Perl in order to run:
         <https://www.gnu.org/software/autoconf>
         <https://www.gnu.org/software/m4/>
         <https://www.perl.org/>
make: *** [../aclocal.m4] Error 127
```
Reconfigure the file `aclocal.m4`:
```sh
cd ..
aclocal
automake --add-missing
cd build
make
```
Done!
#### rmblast
```sh
cd ~/software/Repeatmodeler
wget https://www.repeatmasker.org/rmblast/rmblast-2.14.1+-x64-linux.tar.gz
tar -xzvf rmblast-2.14.1+-x64-linux.tar.gz
# remember to change the `.bashrc`
```
#### RepeatMasker
```sh
wget https://www.repeatmasker.org/RepeatMasker/RepeatMasker-4.1.7-p1.tar.gz
tar -xzvf RepeatMasker-4.1.7-p1.tar.gz
```
Configure the libraries of `Dfam` and `Repbase`:
```sh
# Dfam
cd RepeatMasker/Libraries
wget https://www.dfam.org/releases/Dfam_3.8/families/Dfam-RepeatMasker.lib.gz
gunzip Dfam-RepeatMasker.lib.gz

# Repbase, this lib is paid, please subscribe and download on your own

cd ..
perl ./configure

# remember to change the `.bashrc`
```

### 2 RECON
```sh
cd ~/software/Repeatmodeler
wget http://www.repeatmasker.org/RepeatModeler/RECON-1.08.tar.gz
tar -xzvf RECON-1.08.tar.gz
cd RECON-1.08/src/
make
# remember to change the `.bashrc`
```

### 3 RepeatScount
```sh
cd ~/software/RepeatModeler/
wget http://www.repeatmasker.org/RepeatScout-1.0.6.tar.gz
tar -zxvf RepeatScout-1.0.6.tar.gz
cd RepeatScout-1.0.6
make
# remember to change the `.bashrc`
```

### 4 UCSC genome browser command-line utilities
```sh
cd ~/software/RepeatModeler/
wget http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/twoBitInfo
wget http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/twoBitToFa
wget http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/faToTwoBit
# use chmod to modify program permissions
chmod u+x twoBitInfo
chmod u+x twoBitToFa
chmod u+x faToTwoBit
# remember to change the `.bashrc`
```
### 5 Optional. Required for running LTR structural search pipeline
#### LtrHarvest 
```sh
cd ~/software/RepeatModeler/
wget https://genometools.org/pub/genometools-1.6.2.tar.gz
tar -zxvf genometools-1.6.2.tar.gz
cd genometools-1.6.2/
# remember to change the `.bashrc`
```
#### Ltr_retriever
```sh
cd ~/software/RepeatModeler/
wget https://github.com/oushujun/LTR_retriever/archive/refs/tags/v3.0.1.tar.gz
tar -zxvf tar -zxvf LTR_retriever-3.0.1.tar.gz
# remember to change the `.bashrc`
```
#### MAFFT
```sh
conda create -n repeatmodeler
conda activate repeatmodeler
conda install bioconda::mafft
```
Building the link, so RepeatModeler `configure` program can find the mafft:
```sh
ln -sf ~/miniconda3/envs/repeatmodeler/bin/ MAFFT
```

#### CD-HIT
```sh
cd ~/software/RepeatModeler/
wget https://github.com/weizhongli/cdhit/archive/refs/tags/V4.8.1.tar.gz
tar -zxvf V4.8.1.tar.gz
cd cdhit-4.8.1/
# remember to change the `.bashrc`
```
#### Ninja
```sh
cd ~/software/RepeatModeler/
wget https://github.com/TravisWheelerLab/NINJA/archive/refs/tags/0.98-cluster_only.tar.gz
tar -zxvf 0.98-cluster_only.tar.gz
cd NINJA-0.98-cluster_only/NINJA/
make all
# remember to change the `.bashrc`
```
### 6 RepeatModeler
```sh
cd ~/software/RepeatModeler/
git clone https://github.com/Dfam-consortium/RepeatModeler.git
cd RepeatModeler-master/
perl ./configure
```
However, the output showing that:
```sh
The following perl modules required by RepeatModeler are missing from
your system.  Please install these first:
    JSON
    File::Which
    Devel::Size
```
So, we must be installing these perl modules in advance:
#### Non-root installation of perl and perl-modules
`perl`
```sh
wget https://www.cpan.org/src/5.0/perl-5.40.0.tar.gz
tar -zxvf perl-5.40.0.tar.gz
cd ~/software/perl-5.40.0
```
Following the prompt to complete the installation.
```sh
make -help
./Configure -des -Dprefix=~/software/perl-5.40.0 -Dusethreads
```
Don't forget to point to your own Perl installation in `.bashrc` or another configuration file.
Enter interactive cpan installation mode.
```sh
perl -MCPAN -e shell
```
Installing required modules by interactive cpan:
```perl
install JSON
install File::Which
install Devel::Size
```
#### done
Now, install it!
```shell
cd ~/software/RepeatModeler/RepeatModeler-master
perl ./configure
# remember to change the `.bashrc`
```
Done!




