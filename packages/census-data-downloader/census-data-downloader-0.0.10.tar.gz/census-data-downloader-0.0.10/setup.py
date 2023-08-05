from setuptools import setup


setup(
    name='census-data-downloader',
    version='0.0.10',
    description="Download Census data and reformat it for humans",
    author='Los Angeles Times Data Desk',
    author_email='datadesk@latimes.com',
    url='http://www.github.com/datadesk/census-data-downloader',
    license="MIT",
    packages=("census_data_downloader",),
    install_requires=(
        "pandas",
        "us",
        "census",
        "click"
    ),
    entry_points="""
        [console_scripts]
        censusdatadownloader=census_data_downloader.cli:cmd
    """,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
    ],
)
