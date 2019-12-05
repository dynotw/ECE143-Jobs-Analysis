#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 12:20:12 2019

@author: srishtydua
"""

from time import time
from time import sleep
from datetime import datetime
import requests
from requests import get
from random import randint
from IPython.core.display import clear_output
import json
import re
import csv

def get_all_jobs(pages):
    '''
    URL - https://careers.google.com/api/jobs/jobs-v1/search/?company=Google&company=YouTube&employment_type=FULL_TIME&hl=en_US&jlo=en_US&location=California%2C%20USA&location=Oregon%2C%20USA&location=Washington%2C%20USA&page={}&q=&sort_by=relevance
    :param pages: input from main
    :type pages: list
    '''
    assert isinstance(pages,list)
    requests = 0
    start_time = time()
    total_runtime = datetime.now()
    for page in pages:
        response = get("https://careers.google.com/api/jobs/jobs-v1/search/?company=Google&company=YouTube&employment_type=FULL_TIME&hl=en_US&jlo=en_US&page={}&q=&sort_by=relevance".format(page))
        requests += 1                             # Monitor the frequency of requests
        assert response.status_code == 200        # Throw a warning for non-200 status codes
        assert requests <= 147                    # Set page requests. Break the loop if number of requests is greater than expected
        # Pauses the loop between 10 - 20 seconds and marks the elapsed time
        sleep(randint(10, 20))
        current_time = time()
        elapsed_time = current_time - start_time
        print("Google Request:{}; Frequency: {} request/s; Total Run Time: {}".format(requests,
              requests / elapsed_time, datetime.now() - total_runtime))
        clear_output(wait=True)
        
        yield from get_job_infos(response)


def get_job_infos(response):
    '''
    :param response: input from get_all_jobs function
    :type response: requests.models.Response
    '''
    assert isinstance(response,requests.models.Response)
    google_jobs = json.loads(response.text)
    for website in google_jobs['jobs']:
        google_job_id = website['job_id']
        try:
            found_id = re.search('jobs/(\d+)', google_job_id).group(1)
        except AttributeError:
            found_id = None
        site = website["company_name"]
        title = website["job_title"]
        location = website["locations"]
        description = website["description"]
        job_link = "https://careers.google.com/jobs/results/" + found_id
        qualifications = website["summary"]
        yield site, title, location, job_link, description, qualifications


def main():
    '''
    set number of pages and then write in csv file
    '''
    # Set the number of pages to scrape
    pages = [str(i) for i in range(1, 147)]

    # Writes to csv file
    with open('google_jobs.csv', "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Website", "Title", "Location", "Job URL", "description", "qualifications"])
        writer.writerows(get_all_jobs(pages))


if __name__ == "__main__":
    main()