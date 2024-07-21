from setuptools import setup, find_packages

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
        # добавьте другие зависимости по необходимости
    ],
)
