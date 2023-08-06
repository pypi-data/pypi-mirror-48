#! /bin/bash
source ./env.sh
./build_llvm_trunk.sh
./build_qmp.sh
#./build_libxml2.sh
./build_qdp++-double.sh
chmod -R 777 *
./build_quda_qdp_double-cmake.sh
./build_chroma-double.sh

