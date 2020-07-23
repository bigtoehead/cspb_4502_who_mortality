import sys
import os 
import math

first_dataset = open('../dataset/Morticd10_part1.csv','r')
second_dataset = open('../dataset/Morticd10_part2.csv','r')
merged_dataset = open('../dataset/WHO_merged.csv','w')

for line in first_dataset.readlines():
    merged_dataset.writelines(line)

first_dataset.close()

count = 0
for line in second_dataset.readlines():
    if count!=0:
       merged_dataset.writelines(line)
    count=1

second_dataset.close()
merged_dataset.close()
