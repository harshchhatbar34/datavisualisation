import json

from pygal_maps_world import i18n

def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country."""
    for code,name in i18n.COUNTRIES.items():
        if name == country_name:
            return code
    #If the country wasn't found ,return None.
    return None


#Load the data into alist.
filename = 'world population'
with open(filename) as f:
    pop_data = json.load(f)


#Print the 2010 population for each country.
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            print("{} : {}".format(code, population))
        else:
            print("ERROR- {}".format(country_name))
#         print("{} : {}".format(country_name, population) )




# for country_code in sorted(i18n.COUNTRIES.keys()):
#     print(country_code, i18n.COUNTRIES[country_code])





# print(get_country_code('Andorra'))
# print(get_country_code('United Arab Emirates'))
# print(get_country_code('India'))
