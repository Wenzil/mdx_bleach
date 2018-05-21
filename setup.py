
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Read the README into long_description, converting to reStructuredText if
# pypandoc is installed. This is because PyPI expects package descriptions to be
# in reStructuredText format. Only the package maintainer needs to have pypandoc
# installed.
try:
    try:
        from pypandoc import convert
        LONG_DESCRIPTION = convert('README.md', 'rst')
    except ImportError:
        with open('README.md', 'r') as readme:
            LONG_DESCRIPTION = readme.read()
except IOError:
    LONG_DESCRIPTION = None

setup(
    name='mdx_bleach',
    version='0.1.4',
    description="Python-Markdown extension to sanitize the output of untrusted "
                "Markdown documents.",
    long_description=LONG_DESCRIPTION,
    author='Sami Turcotte',
    author_email='samiturcotte@gmail.com',
    url='https://github.com/Wenzil/mdx_bleach',
    download_url='https://github.com/Wenzil/mdx_bleach/archive/0.1.4.tar.gz',
    license='MIT',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Filters",
        "Topic :: Text Processing :: Markup :: HTML",
    ],
    keywords=['mdx', 'bleach', 'markdown', 'extension', 'sanitize', 'html'],

    packages=[
        'mdx_bleach',
    ],
    install_requires=[
        "bleach >= 1.5",
        "Markdown >= 2.6.1",
    ],

)
