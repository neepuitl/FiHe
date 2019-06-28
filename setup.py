from setuptools import setup, find_packages

setup(
    name = "ifh",
    version = "0.0.1",
    keywords = ("file deduplication"),
    description = "ITL File Helper",
    long_description = "ITL File Helper",
    license = "MIT Licence",

    url = "https://github.com/neepuitl/ifh",
    author = "zengxiangji",
    author_email = "xijiz@qq.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    entry_points = {
        'console_scripts': ["ifh=ifh.__main__:main"]
    }
)