from setuptools import setup, find_packages

#pip install -e .

setup(
    name='erp_server',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # Укажите необходимые зависимости
        'flask',
        'sqlalchemy',
        'flask-jwt-extended',
        'flask-cors',
        "fastapi",
        "pydantic",
        "uvicorn[standard]",
        "pyyaml",
        "openapi-core",
        # добавьте другие зависимости по необходимости
    ],
    tests_require=[
        "pytest",
        "pytest-cov",
        "httpx"
    ],
)
