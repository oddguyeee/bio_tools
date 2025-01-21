```sh
cd ~/software
git clone https://github.com/abacus-gene/paml.git
cd paml/src
make -f Makefile

ls -lF
rm *.o

# test
./baseml
./codeml
./evolver
```
