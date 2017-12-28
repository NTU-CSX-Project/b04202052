#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 00:27:24 2017

@author: allen
"""
    
class machine(list):
    def name(self):
        return self[0][0]
    def get_str(self,address):
        address=list(address)
        s=str()
        for i in range(len(self)):
            for j in address:
                s+=str(self[i][j])
                s+=','
            s+="\n"
        return s

def diff_of_target(machine,colume):
    for i in range(len(machine)):
        if i==0:
            machine[i].append(float((machine[i][colume])))
        else:
            machine[i].append((float(machine[i][colume])-float(machine[i-1][colume])))

def save_array(machine,target):
    name=machine.name()+'.csv'
    file=open(name,'w',encoding='UTF-8')
    file.write(machine.get_str(target))
    file.close()

def change_second(time):
    time_ls=time.split(sep=':')
    for i in range(len(time_ls)):
        time_ls[i]=int(time_ls[i])
    return (3600*time_ls[0]+60*time_ls[1]+time_ls[2])

def format_time(machine):
    for i in range(len(machine)):
        machine[i][2]=machine[i][2][11:19]
    for i in range(len(machine)):
        machine[i][2]=change_second(machine[i][2])

def format_array(machine):
    for i in range(len(machine)):
        machine[i].append(int(0))

def get_colume(data_array,colume):
    colume_array=[]
    for i in range(len(data_array)):
        colume_array.append(float(data_array[i][colume]))
    return colume_array

def compare(machine,compare,colume):
    counter=0
    for i in range(len(machine)):
        if abs(float(machine[i][colume]))>compare:
            machine[i][-1]+=1
            counter+=1
    return counter

def label_adjacent(machine):
    target_row=[]
    n=0
    for i in range(len(machine)):
        if machine[i][-1]!=0:
            target_row.append(i)
        else:
            pass
    for i in target_row:
        if i<5:
            for j in range(0,i):
                n+=1
                machine[j][-1]+=1
            for j in range(1,6):
                n+=1
                machine[i+j][-1]+=1
        elif i>=(len(machine)-5):
            for j in range(i,len(machine)):
                n+=1
                machine[j][-1]+=1
            for j in range(-1,-6,-1):
                n+=1
                machine[i+j][-1]+=1
        else:
            for j in [-5,-4,-3,-2,-1,1,2,3,4,5]:
                n+=1
                machine[i+j][-1]+=1
    print(n)

def seperate(new_machine,machine):
    for i in range(len(machine)):
        if machine[i][-1]!=0:
            new_machine.append(machine[i][0:-1])

def subs_element(machine,element,target):
    for i in range(len(machine)):
        machine[i][target]=element