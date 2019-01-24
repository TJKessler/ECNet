from setuptools import setup, find_packages

setup(
    name='ecnet',
    version='2.0.1',
    description='UMass Lowell Energy and Combustion Research Laboratory Neural'
                ' Network Software',
    url='http://github.com/tjkessler/ecnet',
    author='Travis Kessler, Hernan Gelaf-Romer, Sanskriti Sharma',
    author_email='travis.j.kessler@gmail.com,'
                 ' Hernan_Gelafromer@student.uml.edu,'
                 ' Sanskriti_Sharma@student.uml.edu',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'pyyaml',
        'ecabc',
        'pygenetics',
        'colorlogging',
        'numpy',
        'tensorflow'
    ],
    package_data={
        'ecnet': [
            'tools/PaDEL-Descriptor/*',
            'tools/PaDEL-Descriptor/lib/*',
            'tools/PaDEL-Descriptor/license/*'
        ]
    },
    zip_safe=False
)
