# Assignment 6: Interview a dataset

Dataset: COVID-19 outbreak data in Louisiana nursing homes. I used Tabula to take the data from [pdf format](http://ldh.la.gov/assets/oph/Coronavirus/NursingHomes/NHReport051820.pdf) 
and convert it into a [csv format](https://docs.google.com/spreadsheets/d/1ompFTmd-UQE5Ww-LwRBRNkqvsPpLhze_1jwpn3LQ19g/edit#gid=1782651483).

## Questions

1. How many total deaths in the Louisiana nursing homes? 987 deaths
2. How many total cases? 4,084 among residents, 1,737 among staff.
3. How many facilities affected? 195
4. Which nursing home has the highest death rate? Metairie Healthcare

## Excel functions

I then used an Excel functions to get the resident death rate. One tricky thing about the data - I'm not sure if the census includes 
residents who died or excludes them, so I calculated it both ways (```deaths/census``` and ```deaths/(census + deaths)```).

I also sorted the data by cases and deaths, to see how many facilities had at least one of either.

## Headline + nutgraf

### COVID-19 infects thousands in Louisiana nursing homes, killing hundreds

According to state health department data, over 190 nursing homes have seen covid-19 infections or deaths, representing more than two-thirds 
of licensed nursing homes in the state. Nearly 1,000 residents have died, and thousands more have tested positive.




