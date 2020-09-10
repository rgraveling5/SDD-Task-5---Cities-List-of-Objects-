"""
SBB Task 4a - Student Record

Rachael Graveling
09/09/2020

Cities (Lists of Objects)

Reads in the data for a record and stores in a object
TODO: Add the record to a list so that we have a list of objects
"""

class Record():
    def __init__(self, city, country, population, language):
        self.city = city
        self.country = country
        self.population = population
        self.language = language

def main():
    city = get_record()
    display_record(city)

def get_record():
    #A list for storing the individual records (lists)
    rec = []

    # Total number of records
    no_of_cities = 3

    #Loop for number of record entries
    for x in range (no_of_cities):
    # Input data for record
      city = input('Please enter a city > ')
      country = input('Please enter country > ')
      population = float(input('Please enter the population (millions) > '))
      language = input('Please enter language > ')
      print()

    #Add record to list
      rec.append(Record(city, country, population, language))


    #Return list instead of single record
    return rec

def display_record(rec):
    # TODO: Replace this with printing all records
    for record in rec:
      print(record.city, record.country, record.population, record.language)

main()