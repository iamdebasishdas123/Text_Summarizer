import setuptools
with open("Readme.md", "r",encoding="utf-8") as f:
    long_description = f.read()
    
__version__ ="0.0.0"
Repo_Name="Text_Summarizer"
Author_Username="iamdebasishdas123"
SRC_Repo="textsummarizer"
Author_Email="iamdebasishdas123@gmail.com"




setuptools.setup(
    name=SRC_Repo,
    version=__version__,
    author=Author_Username,
    author_email=Author_Email,
    description="A simple text summarizer NLP application",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{Author_Username}/{Repo_Name}",
    project_url={
        "Bug Tracker": f"https://github.com/{Author_Username}/{Repo_Name}/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")   
    
)