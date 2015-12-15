from setuptools import setup

setup(
    name='atlas',
    version='0.0.1',
    author='Mihir Singh (@citruspi)',
    author_email='hello@mihirsingh.com',
    packages=['atlas', 'atlas.templating', 'atlas.providers'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'click',
        'jinja2',
        'boto'
    ],
    scripts=[
        'scripts/atlas'
    ]
)
