from setuptools import find_packages, setup

package_name = 'publisher_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sophia',
    maintainer_email='sophiashoco@gmail.com',
    description='Creates a publishing node that asks the user for coordinates that it will then publish to the created topic until interrupted/terminated.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'talker = publsiher_py.publisher:main',
        ],
    },
)
