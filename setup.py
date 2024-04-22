from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='minebannerlib',
  version='0.0.3',
  author='saddydead1',
  author_email='saddydead1@gmail.com',
  description='Lib for create minecraft banner image',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/saddydead1/minebannerlib',
  packages=find_packages(),
  install_requires=['requests>=2.25.1','nbtlib', 'pillow'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='minecraft banner python pil',
  project_urls={
    'GitHub': 'https://github.com/saddydead1/minebannerlib'
  },
  python_requires='>=3.12'
)
