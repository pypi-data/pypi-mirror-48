#!/bin/bash
#
#################
# BUILD QMP
#################
source ./env.sh

pushd ${SRCDIR}/qdp-jit-llvm-nvptx

if [ -f ./include/qdp_libdevice.h ];
then
   echo "QDP-JIT LibDevice already patched. Cleaning"
   rm -rf ./libdevice_files
   rm -f ./include/qdp_libdevice.h
   rm -f ./lib/qdp_libdevice.cc
fi

echo "QDP-JIT adding LibDevice patch"
mkdir -p ./libdevice_files
cp ${PK_CUDA_HOME}/nvvm/libdevice/* ./libdevice_files
pushd ./libdevice_files
CUDA_MAJOR=`nvcc --version | grep release | awk '{ print $6}' | cut -f2 -dV | cut -f1 -d.`
case ${CUDA_MAJOR} in
8)
      echo CUDA v8. Copying libdevice.compute_30.10.bc to libdevice.compute_60.10.bc for Pascal support
      cp libdevice.compute_30.10.bc libdevice.compute_60.10.bc
      cp libdevice.compute_35.10.bc libdevice.compute_37.10.bc
      ;; 
9) 
      MY_SM=`echo ${SM} | cut -f2 -d'_'`
      echo CUDA v9. Copying libdevice.10.bc to libdevice.compute_${MY_SM}.10.bc
      mv libdevice.10.bc libdevice.compute_${MY_SM}.10.bc
      ;;
*)
     echo Unknown CUDA Version
      ;;
esac
popd ## libdevice_files
./pack_libdevice.sh ./libdevice_files
popd

pushd ${SRCDIR}/qdp-jit-llvm-nvptx
autoreconf
popd

pushd ${BUILDDIR}

if [ -d ./build_qdp++-double ]; 
then 
  rm -rf ./build_qdp++-double
fi

mkdir  ./build_qdp++-double
cd ./build_qdp++-double

echo $LD_LIBRARY_PATH
sleep 5
${SRCDIR}/qdp-jit-llvm-nvptx/configure \
	--prefix=${INSTALLDIR}/qdp++-double \
	--with-libxml2 \
	--with-qmp=${INSTALLDIR}/qmp \
	--enable-comm-split-deviceinit \
        --enable-parallel-arch=parscalar \
	--enable-precision=double \
	--enable-largefile \
	--enable-parallel-io \
        --enable-dml-output-buffering \
        --disable-generics \
        --disable-filedb \
        --with-cuda=${PK_CUDA_HOME} \
	--with-llvm=${LLVM_INSTALL_DIR} \
	--enable-llvm6-trunk \
        CXXFLAGS="${PK_CXXFLAGS}" \
	CFLAGS="${PK_CFLAGS}" \
	LDFLAGS="-L${PK_CUDA_HOME}/nvvm/lib " \
	LIBS="-ldl -lpthread" \
	CXX="${PK_CXX}" \
	CC="${PK_CC}" \
	--host=x86_64-linux-gnu --build=none \
	${OMPENABLE}

${MAKE}
${MAKE} install

popd
