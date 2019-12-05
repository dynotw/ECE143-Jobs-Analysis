# ECE143 Project for 2019 Fall
## Team
Group 1: Bo Chen, Hafiza Rauf, Shuai Hao, Srishty Dua, Yening Dong

## Topic
Data Analysis of Jobs in Amazon, Facebook and Google

### Dataset:
https://careers.google.com/

https://www.amazon.jobs/en

https://www.facebook.com/careers/

The entire dataset contains 3 csv files scrapped from the above websites, including kinds of information like Company, Location, Job Tittle, Job Category, Date, Job Description, Job Basic Qualifications, Job Preferrd Qualification etc.

### Motivation:
Nowadays, an increasing number of people want to find a job in top IT comapnies like FLAG, especially working as Software Engineer. And the ECE143 is a course about programming language, so we believe that the majority of classmates will be interested in the job opportunity in IT companies. As a result, we decide to give classmates some information about jobs in Top IT companies, including Amazon, Facebook and Google.

### Meaning:
We will analyse different aspects from the job, like job category, location, posting date, job qualification and so on. Accoding to the results, we will give people some tips, which the popular job is, which the popular location is, when people should seek jobs, which qualification is important and so on.

### Plan:
Firstly, we scrape the dataset from the companies' career centers. Then we clean and extract useful data from the dataset. Next we analyse these data by information categories, and use the most effective graphs to visualize the results. Finally, we prepare for the presentation.

## File Structure
In each .csv files, there are different categories of data, so we assign the tasks to each group members, in terms of categories. Our file structure is divided by data categories.
```
Root
|
+----Data Scraper
|       |   README.md
|       |   amazonfinal copy (1).py
|       |   facebook final copy.py
|       |   google final copy.py
|
|
+----Job Category
|       |   README.md
|       |   amazon_job_category.py
|       |   facebook_job_category.py
|       |   google_job_category.py
|
|
+----Location
|       |   README.md
|       |   amazon_Location.py
|       |   facebook_location.py
|       |   google_location.py
|
|
+----Major_Degree_Experience_Language_WordCloud
|       |   README.md
|       |   amazon.py
|       |   amazon_job_graph.py
|       |   google.py
|       |   google_job_graph.py
|       |   facebook.py
|       |   facebook_job_graph.py
|       |   experience_years_of_3_companies.py
|       |   summary.py
|
|
|    README.md
|
```

## Packages:
```
1.Beautiful Soup
2.Selenium
3.re
4.pandas
5.Matplotlib
6.Plotly
7.Seaborn
```

For installing these packages, you can use either ```pip3``` to install packages. 

Take ```Numpy``` for example,
```
pip3 install numpy
```

## How to run code
* Python version: Python 3.6.6 64-bit
1. Install all the above third libraries. 
2. Run the ```amazonfinal copy (1).py``` , ```facebook final copy.py``` and ```google final copy.py``` to scrape all the data from the companies' websites.
3. Run the different .py files to create the corresponding categories' graphs. 

Take 'Location' for example, find the Location files, then run the ```google_location.py``` , ```amazon_location.py``` and ```facebook_location.py``` to create the location graphs respectively.
