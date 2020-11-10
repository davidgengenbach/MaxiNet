import sys, os, subprocess, distutils
from setuptools import setup, find_packages

setup(name='MaxiNet',
      version='1.2',
      description='Distributed Software Defined Network Emulation',
      long_description="MaxiNet extends the famous Mininet emulation environment to span the emulation across several physical machines. This allows to emulate very large SDN networks.",
      classifiers=[
          'Programming Language :: Python :: 3.6',
      ],
      keywords='mininet MaxiNet SDN Network OpenFlow openvswitch',
      url='https://www.cs.uni-paderborn.de/?id=maxinet',
      author_email='maxinet@lists.upb.de',
      packages=find_packages(),
      install_requires=[
          'Pyro4',
      ],
      include_package_data=True,
      package_data={
          "MaxiNet": ["Scripts/*"],
      },
      entry_points={
          'console_scripts': [
              'MaxiNetWorker = MaxiNet.WorkerServer.server:main',
              'MaxiNetFrontendServer = MaxiNet.FrontendServer.server:main',
              'MaxiNetStatus = MaxiNet.WorkerServer.server:getFrontendStatus',
          ]
      },
      zip_safe=False)

if ((__name__ == "__main__") and (sys.argv[1] == "install")):
    # We need to make package_data files executable...
    # Ugly hack:

    import tempfile

    with tempfile.NamedTemporaryFile() as file:
        f = open(file.name, "w")
        f.write("""
import os,subprocess
from MaxiNet.tools import Tools
d = Tools.get_script_dir()
for f in filter(lambda x: x[-3:]==".sh",os.listdir(d)):
    print(f)
    subprocess.call(["sudo","chmod","a+x",d+f])
    """.strip())
        f.close()
        subprocess.call(["python3", file.name])
