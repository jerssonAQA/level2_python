import read_csv
import utils
import charts

def run():
  data = read_csv.read_csv('./aProyecto/data.csv') #lectura del archivo
  opcion=utils.menu()
  while True:
    if opcion=='1':
      country = input('Type Country => ') 
      result= utils.population_by_country(data, country)#devuelve el direccionario de un pais en especifico (country)
      if len(result)>0: # si es cero es porque no encontro pais con esa descripcion
        country=result[0]
        labels,values=utils.get_population(country)
        charts.generate_bar_chart(labels,values)
    elif (opcion=='2'):
      utils.listas(opcion)
      countries= list(map(lambda x:x['Country/Territory'],data))
      percentages= list(map(lambda x:float(x['World Population Percentage']),data))
      charts.generate_pie_chart(countries,percentages)
      
    elif  opcion=='3':
      name_continent=input('Ingrese el nombre de continente:')
      if (name_continent in list(map(lambda x:x['Continent'],data))):
        print(' Visualizacion de datos segun '+name_continent)
        data= list(filter(lambda x:x['Continent'] ==name_continent,data))
        countries= list(map(lambda x:x['Country/Territory'],data))
        percentages= list(map(lambda x:float(x['World Population Percentage']),data))
        charts.generate_pie_chart(countries,percentages)
      else:
        print('Opcion no valida')
    
    

if __name__ == '__main__':
  run()
