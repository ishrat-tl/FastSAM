# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from setuptools import find_packages, setup

setup(
    name="Fast SAM",
    version="0.1.1",
    install_requires=[],
    packages=['fastsam', 'fastsam_tools'],
    package_dir= {
        'fastsam': 'fastsam',
        'fastsam_tools': 'utils',
    },
    url="https://github.com/CASIA-IVA-Lab/FastSAM",
)
