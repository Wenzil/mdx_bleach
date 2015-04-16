
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    with open('README.md', 'r') as readme:
        LONG_DESCRIPTION = readme.read()
except Exception:
    LONG_DESCRIPTION = None


setup(
    name='mdx_bleach',
    version='0.1.0',
    description="Python Markdown extension to sanitize the output of untrusted
                "Markdown documents.",
    long_description=LONG_DESCRIPTION,
    author='Sami Turcotte',
    author_email='samiturcotte@gmail.com',
    url='https://github.com/Wenzil/mdx_bleach',
    license='MIT License',
    classifiers=(
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
    ),
    keywords=['mdx', 'bleach', 'markdown', 'extension', 'sanitize', 'html'],

    packages=[
        'mdx_bleach',
    ],
    install_requires=[
        "bleach >= 1.4.1",
        "Markdown >= 2.6.1",
    ],

)
