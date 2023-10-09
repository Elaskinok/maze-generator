from setuptools import setup

DESCRIPTION = "Maze generator console-utility."

setup(
    name="maze_generator",
    version="2.0",
    description=DESCRIPTION,
    url="#",
    author="KozachenkoKirill",
    author_email="mr.elaskin@mail.ru",
    license="MazeGEN",
    packages={
        "maze_generator",
    },
    package_dir={"maze": "maze_generator"},
    python_requires=">=3.6",
    install_requires=[
        "image",
    ],
    zip_safe=False,
)
