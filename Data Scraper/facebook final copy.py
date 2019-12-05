#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 16:26:25 2019

@author: srishtydua
"""
from time import time
from datetime import datetime
from time import sleep
from random import randint
import requests
from requests import get
from IPython.core.display import clear_output
from bs4 import BeautifulSoup
import csv
import pandas as pd
import numpy as np
import tempfile

def get_all_jobs(pages):
    '''
    URL: https://www.facebook.com/careers/jobs?results_per_page=100&roles[0]=full-time#search_result
    :param pages: input from main
    :type pages: list
    '''
    assert isinstance(pages,list)
    requests = 0
    start_time = time()
    total_runtime = datetime.now()
    for page in pages:
        response = get("https://www.facebook.com/careers/jobs?results_per_page=100&roles[0]=full-time&page={}#search_result".format(page))
        requests += 1       # Monitor the frequency of requests
        assert response.status_code == 200        # Throw a warning for non-200 status codes
        assert requests <= 25                    # Set page requests. Break the loop if number of requests is greater than expected
        sleep(randint(8, 15))       # Pauses the loop between 8 - 15 seconds and marks the elapsed time
        current_time = time()
        elapsed_time = current_time - start_time
        print("Facebook Request:{}; Frequency: {} request/s; Total Run Time: {}".format(requests,
              requests / elapsed_time, datetime.now() - total_runtime))
        clear_output(wait=True)

        yield from get_job_infos(response)


def get_job_infos(response):
    '''
    :param response: input from get_all_jobs function
    :type response: requests.models.Response
    '''
    assert isinstance(response,requests.models.Response)
    page_soup = BeautifulSoup(response.text, "lxml")
    job_containers = page_soup.find_all("a", "_69jm")
    count = 0
    links = []
    for container in job_containers:
        title = container.find("div", "_69jo").text
        location = container.find("div", "_1n-z _6hy- _21-h").text
        category = container.find("div", "_75tt").text
        job_link = "https://www.facebook.com" + container.get("href")
        links.append(job_link)
        count += 1
        yield title, location, category, job_link
    for link in links:
        if link == 'https://www.facebook.com/careers/jobs/378724109726469/':
            continue
        r = get(link)
        soup = BeautifulSoup(r.text, "lxml")
        title1 = soup.find("h4", "_1zbm _8lfl").text
        g = ''
        description = soup.find("div", "_8mli").text
        data = soup.find_all("div","_8mlh")
        responsibilities = soup.find("div", "_8lfy").text
        minimum_qualifications = data[1].text
        yield title1, g, description, responsibilities, minimum_qualifications


def main():
    '''
    set number of pages and then write in csv file
    '''
    # Set the number of pages to scrape
    pages = [str(i) for i in range(1, 25)]

    # Writes to a temp file
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, newline='', encoding="utf-8") as temp_csv:
        writer = csv.writer(temp_csv)
        writer.writerow(["Title", "Location", "Category", "Job URL"])
        writer.writerows(get_all_jobs(pages))

        # Reads the temp file into a data frame for output to csv file
        fb_df = pd.read_csv(temp_csv.name)
        fb_df = fb_df.join(fb_df['Location'].str.split('\W+(?=\s[A-Z][a-z])', expand=True)
                           .add_prefix('city_').fillna(np.nan))
        fb_df = fb_df.set_index(list(fb_df.columns.values[0:4])).stack()
        fb_df = fb_df.reset_index()
        fb_df['Location'] = fb_df.iloc[:, -1].str.strip()
        fb_df.drop(fb_df.columns[[-1, -2]], axis=1, inplace=True)
        fb_df.to_csv('facebook_jobs.csv', index=False)


if __name__ == "__main__":
    main()