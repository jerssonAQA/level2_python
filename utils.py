
def get_population(country_dict):
  population_dict={
    '2022': int(country_dict['2022 Population']),
    '2020': int(country_dict['2020 Population']),
    '2015': int(country_dict['2015 Population']),
    '2010': int(country_dict['2010 Population']),
    '2000': int(country_dict['2000 Population']),
    '1990': int(country_dict['1990 Population']),
    '1980': int(country_dict['1980 Population']),
    '1970': int(country_dict['1970 Population'])
  }
  return population_dict.keys(),population_dict.values()

def population_by_country(data,country):
  result = list(filter(lambda item: item['Country/Territory'] == country,data))
  #devuelve una fila o item del dataset
  return result

def menu():
  print('            ********** MENU **********           ')
  print('Ingrese 1: si desea ver la poblacion de un pais en varios años: ')
  print('Ingrese 2: si desea ver la poblacion del planeta: ')
  print('Ingrese 3: si desea ver la poblacion por continente: ')
  opcion=''
  while True:
    opcion=input('ingrese su opción: ')
    if (opcion in '[1-3]'):
      return opcion
    print('Opcion no valida')
    
  