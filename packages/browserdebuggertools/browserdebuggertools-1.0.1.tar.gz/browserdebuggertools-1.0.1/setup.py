from setuptools import setup, find_packages


requires = [
        "requests",
        "websocket-client",
]


PACKAGES = find_packages(include="browserdebuggertools*")

setup(
    name="browserdebuggertools",
    version="1.0.1",
    packages=PACKAGES,
    install_requires=requires,
    license="GNU General Public License v3",
    description="A client which calls remote web browser debugger methods",
    long_description_content_type="text/markdown",
    long_description=open("README.md").read(),
    url="https://github.com/scivisum/browser-debugger-tools",
    author="SciVisum LTD",
    author_email="rd@scivisum.co.uk"
)
