#!/bin/bash
#
#################
# BUILD Chroma
#################
source env.sh

pushd ${SRCDIR}/chroma
#aclocal; automake; autoconf
popd

pushd ${BUILDDIR}

if [ -d ./build_chroma-double ]; 
then 
  rm -rf ./build_chroma-double
fi
mkdir  ./build_chroma-double

cd ./build_chroma-double


${SRCDIR}/chroma/configure --prefix=${INSTALLDIR}/chroma-double_quda \
	--with-qdp=${INSTALLDIR}/qdp++-double \
        --with-qmp=${INSTALLDIR}/qmp \
	--enable-cpp-wilson-dslash \
        CC="${PK_CC}"  CXX="${PK_CXX}" \
	CXXFLAGS="${PK_CXXFLAGS}" CFLAGS="${PK_CFLAGS}" \
	LDFLAGS="-Wl,-zmuldefs -L${PK_CUDA_HOME}/lib64 -L${CUDA_INSTALL_PATH}/lib64/stubs" LIBS="-lcublas -lcudart -lcuda" \
        --enable-c-scalarsite-bicgstab-kernels --host=x86_64-linux-gnu --build=none \
        --with-quda=${INSTALLDIR}/quda \
        --with-cuda=${PK_CUDA_HOME}
${MAKE}
${MAKE} install

popd
