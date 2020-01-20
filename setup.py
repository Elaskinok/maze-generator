from setuptools import setup

DESCRIPTON = 'Labyrinth generator console-utility.'

setup(
    name='labyr_generator',
    version='2.0',
    description=DESCRIPTON,
    url='#',
    author='KozachenkoKirill',
    author_email='mr.elaskin@mail.ru',
    license='LabyrGEN',
    packages={'labyr_generator',},
    package_dir={'labyrinth': 'labyr_generator'},
    python_requires='>=3.6',
    install_requires=['image',],
    entry_points={'console_scripts' : ['labyr-gen = labyr_generator.main:main']},
    zip_safe=False
)
