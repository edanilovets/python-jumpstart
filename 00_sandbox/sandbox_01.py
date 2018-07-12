# Description		: Displays some information about the OS you are running this script on

import platform

profile = [
        'architecture',
        'machine',
        'node',
        'platform',
        'processor',
        'python_build',
        'python_compiler',
        'python_version',
        'release',
        'system',
        'uname',
        'version',
    ]

for key in profile:
    if hasattr(platform, key):
        print(key + ": " + str(getattr(platform, key)()))
