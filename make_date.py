"""
Created on Nov 07 2018

@author: swhite
@brief: This script is used to create dates in the formated needed for OOI Data Portal annotations
@usage:
"""

import requests
from datetime import datetime
import netCDF4 as nc

# Define date
# beginDate = '2018-10-30T01:48:00'
# endDate = '2018-10-31T01:48:00'

beginDate = raw_input('Enter time,date in this format yyyy-mm-dd hh:mm:ss : ')

begin_DT = datetime.strptime(beginDate,'%Y-%m-%d %H:%M:%S')
beginDT = int(nc.date2num(begin_DT,'seconds since 1970-01-01')*1000)

print beginDT
