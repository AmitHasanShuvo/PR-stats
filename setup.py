import setuptools


setuptools.setup(
    name='pr_stats',
    version='0.0.1',
    author="Kazi Amit Hasan",
    author_email="kaziamithasan89@gmail.com",
    description="This module brings different stats about pull requests using GitHub API.",
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    License='MIT',
    long_description_content_type="text/markdown",
    url="https://github.com/AmitHasanShuvo/data-inspector",
    keywords='stats',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['pandas==1.1.2','matplotlib==3.1.2','numpy==1.18.5', 'seaborn==0.11.1','scipy==1.6.2']
)