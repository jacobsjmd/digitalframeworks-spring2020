# Assignment 5: Cleaning data

I decided to clean data from Connecticut regarding the number of coronavirus cases and deaths in the state's nursing homes. 
The state originally posted the data in pdf format. The file is saved under ```CT.py``` and can also be found [here](https://portal.ct.gov/-/media/Office-of-the-Governor/News/20200507-Nursing-Homes-with-COVID19.pdf?la=en).

First, I used [Tablula](https://tabula.technology/) to extract the pdf into a csv (```CT_uncleaned.csv```). However, Tabula 
had a lot of issues scraping, with empty rows and columns and names of nursing homes spread across multiple rows.

I used a Python script (```cleaning_script.py```) to clean the data - comments in the script show the steps.
