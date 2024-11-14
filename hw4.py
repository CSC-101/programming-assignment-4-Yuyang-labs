import sys
import os
import build_data

import county_demographics
from build_data import convert_county

def population_total(counties):
    total = 0
    for county in counties:
        total += county.population['2014 Population']
    print(f"2014 Population: {total}")
    return total

def display(counties):
    for county in counties:
        print(county.county + ", " + county.state)
        print("\tPopulation: ", county.population["2014 Population"])
        print("\tAge:\n" + "\t <5: ", county.age["Percent Under 5 Years"],"%")
        print("\t <18: ", county.age["Percent Under 18 Years"],"%")
        print("\t <65: ", county.age["Percent 65 and Older"],"%")
        print("Education \n" + "\t >= High School: ", county.education["High School or Higher"],"%")
        print("\t >= Bachelor's: ", county.education["Bachelor's Degree or Higher"],"%")
        print("Ethnicity Percentages \n" + "\t American Indian and Alaska Native: ", county.ethnicities["American Indian and Alaska Native Alone"],"%")
        print("\t Asian Alone: ", county.ethnicities["Asian Alone"],"%")
        print("\t Black Alone: ", county.ethnicities["Black Alone"],"%")
        print("\t Hispanic or Latino: ", county.ethnicities["Hispanic or Latino"],"%")
        print("\t Native Hawaiian and Other Pacific Islander Alone: ", county.ethnicities["Native Hawaiian and Other Pacific Islander Alone"],"%")
        print("\t Two or More Races: ", county.ethnicities["Two or More Races"],"%")
        print("\t White Alone: ", county.ethnicities["White Alone"],"%")
        print("\t White Alone, not Hispanic or Latino: ", county.ethnicities["White Alone, not Hispanic or Latino"],"%")
        print("Income \n", "\t Median Household: ", county.income["Median Household Income"])
        print("\t Per Capita: ", county.income["Per Capita Income"])
        print("\t Below Poverty Level: ", county.income["Persons Below Poverty Level"],"%")

def filter_state(counties, state:str):
    filtered = []
    for county in counties:
        if county.state == state:
            filtered.append(county)
    print(f"Filter: state == {state} ({len(filtered)}entries)")
    return filtered


def filter_gt(counties, field:str, threshold:float):
   field_parts = field.split('.')
   category = field_parts[0]
   subcategory = field_parts[1]
   filtered = []
   for county in counties:
       try:
           if category == "Education":
               number = county.education[subcategory]
           elif category == "Ethnicities":
               number = county.ethnicities[subcategory]
           elif category == "Income":
               number = county.income[subcategory]
           else:
               raise ValueError(f"Unknown category: {category}")


           if number is not None and number > threshold:
               filtered.append(county)


       except AttributeError:
           print(f"County {county.name} does not have the required '{category} structure")


   count = len(filtered)
   print(f"Filter: {field} < {threshold} ({count} entries)")
   return filtered

def filter_lt(counties, field:str, threshold:float):
   field_parts = field.split('.')
   category = field_parts[0]
   subcategory = field_parts[1]
   filtered = []
   for county in counties:
       try:
           if category == "Education":
               number = county.education[subcategory]
           elif category == "Ethnicities":
               number = county.ethnicities[subcategory]
           elif category == "Income":
               number = county.income[subcategory]
           else:
               raise ValueError(f"Unknown category: {category}")


           if number is not None and number < threshold:
               filtered.append(county)


       except AttributeError:
           print(f"County {county.name} does not have the required '{category} structure")


   count = len(filtered)
   print(f"Filter: {field} < {threshold} ({count} entries)")
   return filtered

def population(counties, field:str):
    total = 0
    field_parts = field.split('.')
    category = field_parts[0]
    subcategory = field_parts [1]
    for county in counties:
        try:
            if category == "Education":
                percent = county.education[subcategory] #percentage subcategory of education
            elif category == "Ethnicities":
                percent = county.ethnicities[subcategory] #percentage subcategory of ethnicities
            elif category == "Income":
                percent = county.income[subcategory] #percentage subcategory of Income
            else:
                raise ValueError(f"Unknown category: {category}")
            if percent is not None:
                total += county.population['2014 Population'] * (percent/100)
            else:
                print(f"Field '{field}' npt found in the county data")
        except AttributeError:
            print(f"County {county.name} does not have the required '{category}' structure")
    print(f"2014 {field} population: {total}")
    return total

def percent(counties, field:str):
   sub_pop = 0
   total_pop = 0
   sub_pop_percentage = 0
   field_parts = field.split('.')
   category = field_parts[0]
   subcategory = field_parts[1]


   for county in counties:
       try:
           if category == "Education":
               percentage = county.education[subcategory]
           elif category == "Ethnicities":
               percentage = county.ethnicities[subcategory]
           elif category == "Income":
               percentage = county.income[subcategory]
           else:
               raise ValueError(f"Unknown category: {category}")


           if percentage is not None:
               total_pop += county.population['2014 Population']
               sub_pop += county.population['2014 Population'] * (percentage / 100)
           else:
               print(f"Field '{field}' not found in the county data")


       except AttributeError:
           print(f"County {county.name} does not have the required '{category} structure")


   if total_pop > 0:
       sub_pop_percentage = (sub_pop / total_pop) * 100
       print(f"2014 {field} percentage:{sub_pop_percentage:}")
   else:
       print("Total population is zero, cannot calculate")


   return sub_pop_percentage




def operation():
   filename = sys.argv[1]
   try:
       counties = build_data.get_data()  #access the full data set by converting unreadable data to readable
       filepath = os.path.join('inputs', filename)
       with open(filepath, 'r') as infile:   #Automatically closes file
           for line in infile:
               line = line.strip()    #removes whitespaces


               if "filter-state" in line:
                   state = line.split(":")[1]
                   counties = filter_state(counties, state)


               elif "filter-gt" in line:
                   try:
                       field = line.split(":")[1]
                       value = line.split(":")[2]
                       counties = filter_gt(counties, field, float(value))
                   except ValueError:
                       print("Data cannot be converted to float value")


               elif "filter-lt" in line:
                   try:
                       field = line.split(":")[1]
                       value = line.split(":")[2]
                       counties = filter_lt(counties, field, float(value))
                   except ValueError:
                       print("Data cannot be converted to float value")


               elif "population" in line and ":" in line:
                   field = line.split(":")[1]
                   population(counties, field)


               elif "percent" in line:
                   field = line.split(":")[1]
                   percent(counties, field)


               elif "population-total" in line:
                   population_total(counties)


               elif "display" in line:
                   display(counties)


   except FileNotFoundError:
       print("Error File Not Found")


   print("End of Program")


if __name__ == "__main__":
    operation()




