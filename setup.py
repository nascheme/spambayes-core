from setuptools import setup

from spambayes import __version__

setup(
    name="spambayes-core",
    version=__version__,
    description = "Spam classification system",
    author = "the spambayes project",
    author_email = "spambayes@python.org",
    url = "http://spambayes.sourceforge.net",
    license="Python Software Foundation License 2.0",
    packages = [
        'spambayes',
        ],
    install_requires = ["fasteners"],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Plugins',
        'License :: OSI Approved :: Python Software Foundation License',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows :: Windows 95/98/2000',
        'Operating System :: Microsoft :: Windows :: Windows NT/2000',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Communications :: Email :: Filters',
        ],
    python_requires=">=3.8",
)
