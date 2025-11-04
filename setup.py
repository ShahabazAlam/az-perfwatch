from setuptools import setup, find_packages

setup(
    name="perfwatch",
    version="1.0.0",
    author="Shahabaz Alam",
    description="Production-ready performance monitoring library for Python web applications",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/perfwatch",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'perfwatch': [
            'dashboard/templates/**/*.html',
            'dashboard/static/**/*',
        ],
    },
    install_requires=[
        "fastapi>=0.100.0",
        "flask>=2.3.2",
        "django>=4.2",
        "sqlalchemy>=2.0",
        "pymongo>=4.0",
        "rich>=13.4",
        "jinja2>=3.1",
        "uvicorn>=0.25.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "black>=23.0",
            "flake8>=6.0",
            "mypy>=1.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "perfwatch=perfwatch.cli.main:cli",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Monitoring",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Framework :: Django",
        "Framework :: Flask",
        "Framework :: FastAPI",
    ],
    python_requires=">=3.8",
    keywords="performance monitoring profiling django flask fastapi metrics",
)

