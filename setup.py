import setuptools

with open("README.md","r", encoding="utf-8") as f:
    long_description = f.read()

__version__ ="0.0.0"

Repo_NAME="Text-Summarization"
Author_USER_NAME="devg211"
SRC_REPO = "textSummarization"
Author_EMAIL = "guptadev599@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=Author_USER_NAME,
    author_email=Author_EMAIL,
    description="A python package for NLP project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"http://github.com/{Author_USER_NAME}/{Repo_NAME}",
    project_urls={
        "Bug Tracker":f"http://github.com/{Author_USER_NAME}/{Repo_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)