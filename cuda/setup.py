from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension
import os

use_local_cub = True
magma_path = "/private/home/jgu/tools/magma"
include_dirs = [f'{magma_path}/include']
if use_local_cub:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    cub_path = os.path.join(dir_path, 'cub-1.8.0')
    include_dirs.append(cub_path)

extension = CUDAExtension('kilonerf_cuda',
    ['fourier_features.cu', 'generate_inputs.cu', 'global_to_local.cu', 'pybind.cu',
     'integrate.cu', 'multimatmul.cu', 'network_eval.cu', 'reorder.cu', 'utils.cu',
     'render_to_screen.cpp'],
    include_dirs = include_dirs,
    libraries = ['GL', 'GLU', 'glut'],
    extra_objects = [f'{magma_path}/lib/libmagma.a'],
    extra_compile_args = {'cxx': [], 'nvcc': ['-Xptxas', '-v,-warn-lmem-usage']}
    )

setup(
    name='kilonerf_cuda',
    ext_modules=[extension],
    cmdclass={
        'build_ext': BuildExtension
    })
