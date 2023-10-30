from setuptools import setup
from setuptools.command.install import install
import subprocess

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        subprocess.run("python simple-track.py", shell=True)

setup(
    name='simple_track',
    version='1.0',
    install_requires=[
        'geocoder',
        'phonenumber',
        'folium',
        'webbrowser'
    ],
    cmdclass={
        'install': PostInstallCommand,
    }
)
