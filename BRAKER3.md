# Perl
```sh
conda create -n braker3
conda activate braker3

perl -MCPAN -e shell
install File::Spec::Functions
install Hash::Merge
install List::Util
install MCE::Mutex
install Module::Load::Conditional
install Parallel::ForkManager
install POSIX
install Scalar::Util::Numeric
install YAML
install Math::Utils
install File::HomeDir
install YAML::XS
install Data::Dumper
install Thread::Queue
install threads
```
# BRAKER components
```sh
cd ~/software/
git clone https://github.com/Gaius-Augustus/BRAKER.git
```

# GeneMark-ETP
```sh
cd ~/software/
git clone https://github.com/gatech-genemark/GeneMark-ETP.git


```
```
export GENEMARK_PATH=/nfs_fs/nfs1/sunwu/software/GeneMark-ETP/bin
