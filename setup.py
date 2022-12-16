from distutils.core import setup

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(name='Gait_Lab_Video_Renaming_Tool',
      version='1.6',
      description='Video renaming tool used within ORLAU gait lab',
      author='Tim Arthur',
      author_email='timothy.arthur1@nhs.net',
      url='https://github.com/TimArthur391/Gait_Lab_Video_Renaming_Tool.git',
      license=license,
     )