from setuptools import setup, find_packages

setup(
    name = "fihe",
    version = "0.0.2",
    keywords = ("file deduplication"),
    description = "File Helper",
    long_description = "File Helper",
    license = "MIT Licence",

    url = "https://github.com/neepuitl/ifh",
    author = "zengxiangji",
    author_email = "xijiz@qq.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    entry_points = {
        'console_scripts': ["fihe=fihe.__main__:main"]
    }
)