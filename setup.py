from setuptools import setup, find_packages

setup(
    name="ollama-cli-test-generator",
    version="1.0.0",
    author="PratheepanBernierC",
    author_email="pratheepan.bernier@eminds.ai",
    description="A CLI tool for generating and validating test cases using Ollama LLM",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/PratheepanBernierC/ollama_cli_test_case_generator",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "langchain-core",
        "langchain-ollama",
        "pytest",
        "torch",
        "transformers"
    ],
    entry_points={
        "console_scripts": [
            "ollama-cli-test-case-generator=cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    zip_safe=False,
)
