"""
 Copyright (c) 2019 Intel Corporation
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
      http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

import os
import re
import sys
import codecs
import setuptools
import glob
import sysconfig

here = os.path.abspath(os.path.dirname(__file__))

with open("README.md", "r") as fh:
    long_description = fh.read()


def read(*parts):
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


INSTALL_REQUIRES = ["numpy>=1.15.2",
                    "onnx>=1.3.0",
                    "opencv-python>=3.4.3.18",
                    "pandas>=0.23.4",
                    "tensorboardX>=1.4",
                    "torch>=1.0.0",
                    "torchvision>=0.2.1",
                    "tqdm>=4.26.0",
                    "pretrainedmodels>=0.7.4",
                    "networkx==2.3"]

DEPENDENCY_LINKS = []
if "--cpu-only" in sys.argv:
    INSTALL_REQUIRES.extend(["torch", "torchvision"])
    if sys.version_info[:2] == (3, 5):
        DEPENDENCY_LINKS = [
            'https://download.pytorch.org/whl/cpu/torch-1.3.1%2Bcpu-cp35-cp35m-linux_x86_64.whl',
            'https://download.pytorch.org/whl/cpu/torchvision-0.4.2%2Bcpu-cp35-cp35m-linux_x86_64.whl']
    elif sys.version_info[:2] == (3, 6):
        DEPENDENCY_LINKS = [
            'https://download.pytorch.org/whl/cpu/torch-1.3.1%2Bcpu-cp36-cp36m-linux_x86_64.whl',
            'https://download.pytorch.org/whl/cpu/torchvision-0.4.2%2Bcpu-cp36-cp36m-linux_x86_64.whl']
    elif sys.version_info[:2] >= (3, 7):
        DEPENDENCY_LINKS = [
            'https://download.pytorch.org/whl/cpu/torch-1.3.1%2Bcpu-cp37-cp37m-linux_x86_64.whl',
            'https://download.pytorch.org/whl/cpu/torchvision-0.4.2%2Bcpu-cp37-cp37m-linux_x86_64.whl']
    else:
        print("Only Python > 3.5 is supported")
        sys.exit(0)
    KEY = ["CPU"]
    sys.argv.remove("--cpu-only")
else:
    INSTALL_REQUIRES.extend(["torch==1.4.0", "torchvision==0.4.2"])
    KEY = ["GPU"]


EXTRAS_REQUIRE = {
    "tests": [
        "pytest"],
    "docs": []
}

package_data = {}


setuptools.setup(
    name="action_recognition",
    version=find_version(os.path.join(here, "action_recognition/version.py")),
    author="Intel",
    author_email="alexander.kozlov@intel.com",
    description="Neural Networks Compression Framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/opencv/openvino-training-extensions",
    packages=setuptools.find_packages(),
    dependency_links=DEPENDENCY_LINKS,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    package_data=package_data,
    keywords=KEY
)

