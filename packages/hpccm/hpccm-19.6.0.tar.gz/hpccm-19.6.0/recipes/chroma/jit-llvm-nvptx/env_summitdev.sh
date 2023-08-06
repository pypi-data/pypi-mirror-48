##### 
# SET UP ENVIRONMENT

module load gcc/5.4.0
module unload spectrum_mpi
module load cuda
module load cmake
module list 

SM=sm_60     # Kepler Gaming
OMP="yes"


# The directory containing the build scripts, this script and the src/ tree
TOPDIR=`pwd`

# Install directory
INSTALLDIR=${TOPDIR}/install/${SM}


if [ "x${OMP}x" == "xyesx" ];
then
 INSTALLDIR=${INSTALLDIR}_omp
fi

# LLVM Install Directory
LLVM_INSTALL_DIR=${HOME}/install
export LD_LIBRARY_PATH=${LLVM_INSTALL_DIR}/lib:${LD_LIBRARY_PATH}

# Source directory
SRCDIR=${TOPDIR}/../src

# Build directory
BUILDDIR=${TOPDIR}/build


### ENV VARS for CUDA/MPI
# These are used by the configure script to make make.inc
PK_CUDA_HOME=/sw/summitdev/cuda/8.0.54
export LD_LIBRARY_PATH=${PK_CUDA_HOME}/nvvm/lib:${LD_LIBRARY_PATH}
PK_MPI_HOME=$HOME/openmpi_gcc5.4.0
PK_GPU_ARCH=${SM}

export PATH=${PK_MPI_HOME}/bin:$PATH
export LD_LIBRARY_PATH=${PK_MPI_HOME}/lib:$LD_LIBRARY_PATH

### OpenMP
# Open MP enabled
if [ "x${OMP}x" == "xyesx" ]; 
then 
 OMPFLAGS="-fopenmp -D_REENTRANT "
 OMPENABLE="--enable-openmp"
else
 OMPFLAGS=""
 OMPENABLE=""
fi

if [ ! -d ${INSTALLDIR} ];
then
  mkdir -p ${INSTALLDIR}
fi
### COMPILER FLAGS
PK_CXXFLAGS=${OMPFLAGS}" -g -O3 -std=c++11 "

PK_CFLAGS=${OMPFLAGS}" -g -O3 -std=gnu99"

### Make
MAKE="make -j 10"

### MPI
PK_CC=mpicc
PK_CXX=mpicxx
QDPJIT_HOST_ARCH="PowerPC;NVPTX"
PK_LLVM_CXX=g++
PK_LLVM_CC=gcc
PK_LLVM_CFLAGS="-O3 -std=c99"
PK_LLVM_CXXFLAGS="-O3 -std=c++11"
JITARCHS="${QDPJIT_HOST_ARCH},nvptx"

#PK_NVCCFLAGS="NVCCFLAGS=\"--keep --keep-dir=/scratch/bjoo/tmp\""
