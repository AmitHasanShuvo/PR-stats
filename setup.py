import setuptools


setuptools.setup(
    name='pr_stats',
    version='0.0.1',
    author="Kazi Amit Hasan",
    author_email="kaziamithasan89@gmail.com",
    description="This module brings different stats about pull requests using GitHub API.",
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/AmitHasanShuvo/PR-stats",
    keywords=['stats','pull requests','github'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)