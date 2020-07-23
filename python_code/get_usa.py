import sys
import os 
import math

merged_dataset = open('../dataset/WHO_merged.csv','r')
usa_dataset = open('../dataset/USA_deaths.csv','w')


count = 0
for line in merged_dataset.readlines():
    if count==0:
       usa_dataset.writelines(line)
    count=1
    if line.split(',')[0]=='2450':
        usa_dataset.writelines(line)

merged_dataset.close()
use_dataset.close()
