from setuptools import setup, find_namespace_packages

setup(
    name="moderngl-window",
    version="2.4.2",
    description="A cross platform helper library for ModernGL making window creation and resource loading simple",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/moderngl/moderngl_window",
    author="Einar Forselv",
    author_email="eforselv@gmail.com",
    packages=find_namespace_packages(include=['moderngl_window', 'moderngl_window.*']),
    include_package_data=True,
    keywords=['moderngl', 'window', 'context'],
    license='MIT',
    platforms=['any'],
    python_requires='>=3.6',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Games/Entertainment',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Multimedia :: Graphics :: 3D Rendering',
        'Topic :: Scientific/Engineering :: Visualization',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    install_requires=[
        'moderngl<6',
        'pyglet>=2.0dev23',
        'numpy>=1.16,<2',
        'pyrr>=0.10.3,<1',
        'Pillow>=9,<10',
    ],
    extras_require={
        "PySide2": ['PySide2<6'],
        "pyqt5": ['PyQt5'],
        "glfw": ['glfw'],
        "PySDL2": ['PySDL2'],
        "pywavefront": ["pywavefront>=1.3.3,<2"],
        "trimesh": ["trimesh>=3.2.6,<4", "scipy>=1.3.2"],
        "tk": ["pyopengltk>=0.0.3"],
        "pygame": ["pygame>=2.1.2"],
    },
    project_urls={
        'Documentation': 'https://moderngl-window.readthedocs.io',
        'ModernGL': 'https://github.com/moderngl/moderngl',
    },
)
