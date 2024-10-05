from setuptools import setup, find_packages

setup(
    name="dynamic-prompt",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'dynamic-prompt=dynamic_prompt.main:main',
        ],
    },
    package_data={
        'dynamic_prompt': ['config.json', 'categories/*.json'],
    },
)
