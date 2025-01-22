# GLIBCXX
```sh
wget https://anaconda.org/bioconda/cafe/5.1.0/download/linux-64/cafe-5.1.0-h5ca1c30_1.tar.bz2
conda install --use-local cafe-5.1.0-h5ca1c30_1.tar.bz2

cd /nfs_fs/nfs1/sunwu/miniconda3/envs/cafe
wget http://archive.ubuntu.com/ubuntu/pool/main/g/gcc-12/libstdc++6_12-20220319-1ubuntu1_amd64.deb
wget http://archive.ubuntu.com/ubuntu/pool/main/g/gcc-14/libstdc++6_14.2.0-4ubuntu2_amd64.deb
dpkg-deb -x libstdc++6_14.2.0-4ubuntu2_amd64.deb extracted_libstdc++
strings extracted_libstdc++/usr/lib/x86_64-linux-gnu/libstdc++.so.6 | grep GLIBCXX

cd lib
mv ../extracted_libstdc++/usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.33 .
chmod u+x libstdc++.so.6.0.33

mv libstdc++.so.6.0.29 libstdc++.so.6.0.29-source

ln -sf libstdc++.so.6.0.33 libstdc++.so.6.0.29
ln -sf libstdc++.so.6.0.33 libstdc++.so.6
ln -sf libstdc++.so.6.0.33 libstdc++.so
```
# glibc_2.38
```sh
cd /nfs_fs/nfs1/sunwu/miniconda3/envs/cafe
wget http://archive.ubuntu.com/ubuntu/pool/main/g/glibc/libc6_2.40-1ubuntu3_amd64.deb
dpkg-deb -x libc6_2.40-1ubuntu3_amd64.deb ./glibc-2.40
```
