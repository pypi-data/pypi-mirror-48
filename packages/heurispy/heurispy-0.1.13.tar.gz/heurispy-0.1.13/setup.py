from setuptools import setup

setup(name='heurispy',
      version='0.1.13',
      description='Framework para exploración de heurísticas de búsqueda local en problemas de optimización discreta',
      url='https://gitlab.com/escamilla.een/heurispy',
      author='Esteban Escamilla Navarro',
      author_email='escamilla.een@gmail.com',
      license='',
      packages=['heurispy', 'heurispy.ejemplos', 'heurispy.heuristicas'],
      install_requires=['pathos', 'tqdm', 'numpy', 'pandas', 'fpdf', 'matplotlib', 'pypdf2'],
      include_package_data=True,
      zip_safe=False)
