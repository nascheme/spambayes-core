from setuptools import setup

from spambayes import __version__

setup(
    name="spambayes-core",
    version=__version__,
    description="Spam classification system",
    author="the spambayes project",
    author_email="spambayes@python.org",
    url="https://github.com/nascheme/spambayes-core/",
    license="Python Software Foundation License 2.0",
    packages=[
        'spambayes',
    ],
    install_requires=["fasteners"],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: No Input/Output (Daemon)',
        'License :: OSI Approved :: Python Software Foundation License',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: Communications :: Email :: Filters',
    ],
    python_requires=">=3.8",
)
