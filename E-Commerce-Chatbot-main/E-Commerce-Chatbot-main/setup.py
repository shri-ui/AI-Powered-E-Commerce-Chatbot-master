from setuptools import find_packages, setup

setup(
    name="ecommbot",
    version="0.0.1",
    author="shri",
    author_email="shri.ss2783@gmail.com",
    packages=find_packages(),
    install_requires=['langchain-astradb','langchain','langchain-google-genai','datasets','pypdf','python-dotenv','flask']
)