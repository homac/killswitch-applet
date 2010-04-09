#!/usr/bin/python

from distutils.core import setup

KILLSWITCH_APPLET_VERSION='0.2.2'

dist = setup(name='killswitch-applet',
    version=KILLSWITCH_APPLET_VERSION,
    author='Holger Macht',
    author_email='holger@homac.de',
    maintainer='Holger Macht',
    maintainer_email='holger@homac.de',
    description='Killswitch Applet',
    long_description='Manage Killswitches',
    url='http://blog.homac.de',
    download_url='http://blog.homac.de',
    license='WTFPL',
    platforms='linux',
    scripts=['killswitch-applet/killswitch-applet'],
    data_files=[
        ('share/icons/hicolor/32x32/apps', ['icons/killswitch-applet.png']),
        ('share/icons/hicolor/scalable/apps', ['icons/scalable/killswitch-applet.svg']),
        ('share/applications', ['data/killswitch-applet.desktop']),
        ],
)
    
## To uninstall manually delete these files/folders:
## /usr/bin/killswitch-applet
## /usr/share/icons/hicolor/32x32/apps/killswitch-applet.png
## /usr/share/icons/hicolor/scalable/apps/killswitch-applet.svg
## /usr/lib64/python2.6/site-packages/killswitch_applet-0.1-py2.6.egg-info
## /usr/share/applications/killswitch-applet.desktop
