import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_docs():
    result = []
    in_docs = False
    f = open(os.path.join(os.path.dirname(__file__), 'speaklater.py'))
    try:
        for line in f:
            if in_docs:
                if line.lstrip().startswith(':copyright:'):
                    break
                result.append(line[4:].rstrip())
            elif line.strip() == 'r"""':
                in_docs = True
    finally:
        f.close()
    return '\n'.join(result)


setup(
    name='flaskpress-speaklater',
    author='InfrasCloudy, @allanice001',
    author_email='support@linaccess.za.net',
    version='1.3.0',
    url='http://github.com/infrascloudy/flaskpress_speaklater',
    py_modules=['speaklater'],
    description="Implements a lazy string for python for use with gettext",
    long_description=get_docs(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Internationalization',
        'Programming Language :: Python'
    ]
)