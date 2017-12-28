#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 20:20:12 2017

@author: allen
"""
import re
import function as fun
import numpy as np

#declaration of variables
machine_00=fun.machine()
machine_01=fun.machine()
machine_02=fun.machine()
machine_03=fun.machine()
machine_04=fun.machine()
machine_05=fun.machine()

#the function to classify information according to machine id
def classify(data,machine_id):
    global machine_00
    global machine_01
    global machine_02
    global machine_03
    global machine_04
    global machine_05
    if data[0]==machine_id[0]:
        machine_00.append(data)
    if data[0]==machine_id[1]:
        machine_01.append(data)
    if data[0]==machine_id[2]:
        machine_02.append(data)
    if data[0]==machine_id[3]:
        machine_03.append(data)
    if data[0]==machine_id[4]:
        machine_04.append(data)
    if data[0]==machine_id[5]:
        machine_05.append(data)

#opening the file and get the data we want
File=open('CPU.csv','r',encoding='UTF-8')
raw_data=File.read()
File.close()

data_ls=re.split(r'[,\n]\s*',raw_data)

#to distinguish all machine id
machine_id=[]
machine_id_rep=[]
machine_id_rep.append(data_ls[0])

for i in range(int(len(data_ls)/8)-1):
    if data_ls[8*(i+1)]!=data_ls[8*i]:
        machine_id_rep.append(data_ls[8*(i+1)])

machine_id_rep.sort()
machine_id.append(machine_id_rep[0])

for i in range(len(machine_id_rep)-1):
    if machine_id_rep[i+1]!=machine_id_rep[i]:
        machine_id.append(machine_id_rep[i+1])
#_________________________________________________

#to format the data array and construct what we want
for i in range(int(len(data_ls)/8)):
    classify(data_ls[8*i:8*i+8],machine_id)

#to calculate the difference of CPU_usage_percent
fun.diff_of_target(machine_00, 4)
fun.diff_of_target(machine_01, 4)
fun.diff_of_target(machine_02, 4)
fun.diff_of_target(machine_03, 4)
fun.diff_of_target(machine_04, 4)
fun.diff_of_target(machine_05, 4)
    
fun.format_array(machine_00)
fun.format_array(machine_01)
fun.format_array(machine_02)
fun.format_array(machine_03)
fun.format_array(machine_04)
fun.format_array(machine_05)

fun.format_time(machine_00)
fun.format_time(machine_01)
fun.format_time(machine_02)
fun.format_time(machine_03)
fun.format_time(machine_04)
fun.format_time(machine_05)

#_________________________________________________

#to calculate the stander deviation and average of CPU usage percent
cpu_00_std=np.std(fun.get_colume(machine_00,4),ddof=0)
cpu_01_std=np.std(fun.get_colume(machine_01,4),ddof=0)
cpu_02_std=np.std(fun.get_colume(machine_02,4),ddof=0)
cpu_03_std=np.std(fun.get_colume(machine_03,4),ddof=0)
cpu_04_std=np.std(fun.get_colume(machine_04,4),ddof=0)
cpu_05_std=np.std(fun.get_colume(machine_05,4),ddof=0)

cpu_00_ave=np.mean(fun.get_colume(machine_00,4))
cpu_01_ave=np.mean(fun.get_colume(machine_01,4))
cpu_02_ave=np.mean(fun.get_colume(machine_02,4))
cpu_03_ave=np.mean(fun.get_colume(machine_03,4))
cpu_04_ave=np.mean(fun.get_colume(machine_04,4))
cpu_05_ave=np.mean(fun.get_colume(machine_05,4))

cpu_00_diff_std=np.std(fun.get_colume(machine_00,-2),ddof=0)
cpu_01_diff_std=np.std(fun.get_colume(machine_01,-2),ddof=0)
cpu_02_diff_std=np.std(fun.get_colume(machine_02,-2),ddof=0)
cpu_03_diff_std=np.std(fun.get_colume(machine_03,-2),ddof=0)
cpu_04_diff_std=np.std(fun.get_colume(machine_04,-2),ddof=0)
cpu_05_diff_std=np.std(fun.get_colume(machine_05,-2),ddof=0)

cpu_00_diff_ave=np.mean(fun.get_colume(machine_00,-2))
cpu_01_diff_ave=np.mean(fun.get_colume(machine_01,-2))
cpu_02_diff_ave=np.mean(fun.get_colume(machine_02,-2))
cpu_03_diff_ave=np.mean(fun.get_colume(machine_03,-2))
cpu_04_diff_ave=np.mean(fun.get_colume(machine_04,-2))
cpu_05_diff_ave=np.mean(fun.get_colume(machine_05,-2))

'''print(cpu_00_diff_ave)
print(cpu_01_diff_ave)
print(cpu_02_diff_ave)
print(cpu_03_diff_ave)
print(cpu_04_diff_ave)
print(cpu_05_diff_ave)
print("__________________________")'''
#_________________________________________________

#to label the data we want in each machine
print(fun.compare(machine_00, cpu_00_ave+10.5*cpu_00_std, 4))
print(fun.compare(machine_01, cpu_01_ave+8.5*cpu_01_std, 4))
print(fun.compare(machine_02, cpu_02_ave+8*cpu_02_std, 4))
print(fun.compare(machine_03, cpu_03_ave+10*cpu_03_std, 4))
print(fun.compare(machine_04, cpu_04_ave+12*cpu_04_std, 4))
print(fun.compare(machine_05, cpu_05_ave+12*cpu_05_std, 4))
print("__________________________")
'''
print(fun.compare(machine_00, 0.1, 4))
print(fun.compare(machine_01, 0.1, 4))
print(fun.compare(machine_02, 0.1, 4))
print(fun.compare(machine_03, 0.1, 4))
print(fun.compare(machine_04, 0.1, 4))
print(fun.compare(machine_05, 0.1, 4))
print("__________________________")'''

print(fun.compare(machine_00, cpu_00_diff_ave+10*cpu_00_diff_std, -2))
print(fun.compare(machine_01, cpu_01_diff_ave+7.5*cpu_01_diff_std, -2))
print(fun.compare(machine_02, cpu_02_diff_ave+6.5*cpu_02_diff_std, -2))
print(fun.compare(machine_03, cpu_03_diff_ave+8*cpu_03_diff_std, -2))
print(fun.compare(machine_04, cpu_04_diff_ave+11*cpu_04_diff_std, -2))
print(fun.compare(machine_05, cpu_05_diff_ave+12*cpu_05_diff_std, -2))
print("__________________________")

'''n=0
for i in range(len(machine_05)):
    if machine_05[i][-1]!=0:
        n+=1
    if n in range(0,1200):
        print(machine_05[i][-1])

print(n)'''

fun.label_adjacent(machine_00)
fun.label_adjacent(machine_01)
fun.label_adjacent(machine_02)
fun.label_adjacent(machine_03)
fun.label_adjacent(machine_04)
fun.label_adjacent(machine_05)
#_________________________________________________

#to seperate the labeled data and form the new array
finaldata_00=fun.machine()
finaldata_01=fun.machine()
finaldata_02=fun.machine()
finaldata_03=fun.machine()
finaldata_04=fun.machine()
finaldata_05=fun.machine()

fun.seperate(finaldata_00,machine_00)
fun.seperate(finaldata_01,machine_01)
fun.seperate(finaldata_02,machine_02)
fun.seperate(finaldata_03,machine_03)
fun.seperate(finaldata_04,machine_04)
fun.seperate(finaldata_05,machine_05)

fun.subs_element(finaldata_01,6,0)
fun.subs_element(finaldata_04,5,0)
fun.subs_element(finaldata_03,4,0)
fun.subs_element(finaldata_02,3,0)
fun.subs_element(finaldata_00,2,0)
fun.subs_element(finaldata_05,1,0)

for i in range(len(finaldata_00)):
    score=int(1.0*((float(finaldata_00[i][4])-cpu_00_ave)/cpu_00_std)\
                          +2.0*((float(finaldata_00[i][-1])-cpu_00_diff_ave)/cpu_00_diff_std))
    finaldata_00[i].append(score)
for i in range(len(finaldata_01)):
    score=int(1.0*((float(finaldata_01[i][4])-cpu_01_ave)/cpu_01_std)\
                          +2.0*((float(finaldata_01[i][-1])-cpu_01_diff_ave)/cpu_01_diff_std))
    finaldata_01[i].append(score)
for i in range(len(finaldata_02)):
    score=int(1.0*((float(finaldata_02[i][4])-cpu_02_ave)/cpu_02_std)\
                          +2.0*((float(finaldata_02[i][-1])-cpu_02_diff_ave)/cpu_02_diff_std))
    finaldata_02[i].append(score)
for i in range(len(finaldata_03)):
    score=int(1.0*((float(finaldata_03[i][4])-cpu_03_ave)/cpu_03_std)\
                          +2.0*((float(finaldata_03[i][-1])-cpu_03_diff_ave)/cpu_03_diff_std))
    finaldata_03[i].append(score)
for i in range(len(finaldata_04)):
    score=int(1.0*((float(finaldata_04[i][4])-cpu_04_ave)/cpu_04_std)\
                          +2.0*((float(finaldata_04[i][-1])-cpu_04_diff_ave)/cpu_04_diff_std))
    finaldata_04[i].append(score)
for i in range(len(finaldata_05)):
    score=int(1.0*((float(finaldata_05[i][4])-cpu_05_ave)/cpu_05_std)\
                          +2.0*((float(finaldata_05[i][-1])-cpu_05_diff_ave)/cpu_05_diff_std))
    finaldata_05[i].append(score)
#_________________________________________________

#to creant final data file
'''fun.save_array(finaldata_00,(2,4,-1))
fun.save_array(finaldata_01,(2,4,-1))
fun.save_array(finaldata_02,(2,4,-1))
fun.save_array(finaldata_03,(2,4,-1))
fun.save_array(finaldata_04,(2,4,-1))
fun.save_array(finaldata_05,(2,4,-1))'''

final_data=str()
final_data=finaldata_00.get_str((0,2,4,-2,-1))+finaldata_01.get_str((0,2,4,-2,-1))+finaldata_02.get_str((0,2,4,-2,-1))+finaldata_03.get_str((0,2,4,-2,-1))+finaldata_04.get_str((0,2,4,-2,-1))+finaldata_05.get_str((0,2,4,-2,-1))

ffile=open("final__version.csv",'w',encoding='UTF-8')
ffile.write(final_data)
ffile.close()