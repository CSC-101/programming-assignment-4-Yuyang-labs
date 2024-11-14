
#part4:
#percentage by education
def percent_by_education(list_demographic:list[CountyDemographics], key:str)-> float:
    county_population = 0
    sub_population = 0
    for pop in list_demographic:
        county_population += pop.population['2014 Population']

    for pop in list_demographic:
        if key in pop.education:
            sub_population += pop.population['2014 Population'] * (pop.education[key]/100)
    return round((round(sub_population, 1)/county_population)*100, 1)
#The function's purpose is to return the specified 2014 subpopulation as a percentage of the total 2014 population across the set of counties in the provided list for the education key of interest
#The parameters are list_demographic:list[CountyDemographics], key:str which is a list of county demographics and the education key of interest.
#The return type is a float of the specified 2014 subpopulation as a percentage of the total 2014 population across the set of counties for the education key fo interest.

#education by ethnicity
def percent_by_ethnicity(list_demographic:list[CountyDemographics], key:str)-> float:
    county_population = 0
    sub_pop = 0
    for pop in list_demographic:
        county_population += pop.population['2014 Population']

    for pop in list_demographic:
        if key in pop.ethnicities:
            sub_pop += pop.population['2014 Population'] * (pop.ethnicities[key]/100)
    return round((round(sub_pop,1)/county_population)*100, 1)
#The function's purpose is to return the specified 2014 subpopulation as a percentage of the total 2014 population across the set of counties in the provided list for the ethnicity key of interest.
#The parameters are list_demographic:list[CountyDemographics], key:str which is a list of county demographics and the ethnicity key of interest.
#The return type is a float of the specified 2014 subpopulation as a percentage of the total 2014 population across the set of counties for the ethnicity key fo interest.

#percent below poverty level
def percent_below_poverty_level(list_demographic:list[CountyDemographics])-> float:
    county_population = 0
    sub_pop = 0
    for pop in list_demographic:
        county_population += pop.population['2014 Population']

    for pop in list_demographic:
        sub_pop += pop.population['2014 Population'] * (pop.income["Persons Below Poverty Level"]/100)

    return round((round(sub_pop, 1)/county_population)*100, 1)
#The function's purpose is to return the 2014 subpopulation indicated by income key 'Persons Below Poverty Level' as a percentage of the total 2014 population across the set of counties in the provided list for the key of interest..
#The parameters are list_demographic:list[CountyDemographics] which is a list of county demographics.
#The return type is a float of the specified 2014 subpopulation as a percentage of the total 2014 population for the income key 'Persons Below Poverty Level.'

#Part 5
#education_greater_than
def education_greater_than(list_demographic:list[CountyDemographics], key:str, threshold_value: float)-> list[CountyDemographics]:
    list_counties = []
    for county in list_demographic:
        if key in county.education and county.education[key] > threshold_value:
            list_counties.append(county)
    return list_counties
#The purpose fo this function is to return a list of county demographic objects for which the value for the education key is greater than the threshold value.
#The parameters are list_demographic:list[CountyDemographics], key:str, threshold_value:float, which is a list of county demographics, the education key, and the threshold value.
#The return type is a list of county demographic objects that's value for the education key is greater than the threshold value.

#education_less_than
def education_less_than(list_demographic:list[CountyDemographics], key:str, threshold_value: float)-> list[CountyDemographics]:
    list_counties = []
    for county in list_demographic:
        if key in county.education and county.education[key] < threshold_value:
            list_counties.append(county)
    return list_counties

#The purpose fo this function is to return a list of county demographic objects for which the value for the education key is less than the threshold value.
#The parameters are list_demographic:list[CountyDemographics], key:str, threshold_value:float, which is a list of county demographics, the education key, and the threshold value.
#The return type is a list of county demographic objects that's value for the education key is less than the threshold value.

# ethnicity_greater_than
def ethnicity_greater_than(list_demographic: list[CountyDemographics], key:str, threshold_value: float)-> list[CountyDemographics]:
    list_counties = []
    for county in list_demographic:
        if key in county.ethnicities and county.ethnicities[key] > threshold_value:
            list_counties.append(county)
    return list_counties
#The purpose fo this function is to return a list of county demographic objects for which the value for the ethnicity key is greater than the threshold value.
#The parameters are list_demographic:list[CountyDemographics], key:str, threshold_value:float, which is a list of county demographics, the ethnicity key, and the threshold value.
#The return type is a list of county demographic objects that's value for the ethnicity key is greater than the threshold value.
# ethnicity_less_than
def ethnicity_less_than(list_demographic: list[CountyDemographics], key: str, threshold_value: float) -> list[CountyDemographics]:
    list_counties = []
    for county in list_demographic:
        if key in county.ethnicities and county.ethnicities[key] < threshold_value:
            list_counties.append(county)
    return list_counties

#The purpose fo this function is to return a list of county demographic objects for which the value for the ethnicity key is less than the threshold value.
#The parameters are list_demographic:list[CountyDemographics], key:str, threshold_value:float, which is a list of county demographics, the ethnicity key, and the threshold value.
#The return type is a list of county demographic objects that's value for the ethnicity key is less than the threshold value.

 # test below_poverty_level_greater_than
def below_poverty_level_greater_than(list_demographic: list[CountyDemographics], threshold_value: float)-> list[CountyDemographics]:
    list_counties = []
    for county in list_demographic:
        if county.income["Persons Below Poverty Level"] > threshold_value:
            list_counties.append(county)

    return list_counties
#The purpose fo this function is to return a list of county demographic objects for which the value key 'Persons Below Poverty Level' is greater than the threshold value.
#The parameters are list_demographic:list[CountyDemographics], threshold_value:float, which is a list of county demographics and the threshold value.
#The return type is a list of county demographic objects for which the value key 'Persons Below Poverty Level' is greater than the threshold value.

def below_poverty_level_less_than(list_demographic: list[CountyDemographics], threshold_value: float)-> list[CountyDemographics]:
    list_counties = []
    for county in list_demographic:
        if county.income["Persons Below Poverty Level"] < threshold_value:
            list_counties.append(county)

    return list_counties
#The purpose fo this function is to return a list of county demographic objects for which the value key 'Persons Below Poverty Level' is less than the threshold value.
#The parameters are list_demographic:list[CountyDemographics], threshold_value:float, which is a list of county demographics and the threshold value.
#The return type is a list of county demographic objects for which the value key 'Persons Below Poverty Level' is less than the threshold value.







