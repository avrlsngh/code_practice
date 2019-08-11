'''
PLATFORM - CodeChef
QUESTION CODE - ANKTRAIN
QUESTION LINK - https://www.codechef.com/problems/ANKTRAIN
THIS SOLUTION AUTHOR - avrlsngh
'''
'''
Rahul and Rashi are off to the wedding of a close relative. This time they have to travel without their guardians. Rahul got very interested in the arrangement of seats inside the train coach.

The entire coach could be viewed as an arrangement of consecutive blocks of size 8.


Berth Number   	Compartment

 1 -  8               1  
 9 - 16               2  
17 - 24               3  
... and so on
Each of these size-8 blocks are further arranged as:


 1LB,  2MB,  3UB,  4LB,  5MB,  6UB,  7SL,  8SU  
 9LB, 10MB, ...
 ...   
 ...
Here LB denotes lower berth, MB middle berth and UB upper berth.
The following berths are called Train-Partners:


3UB   |  6UB  
2MB   |  5MB  
1LB   |  4LB  
7SL   |  8SU  
and the pattern is repeated for every set of 8 berths.

Rahul and Rashi are playing this game of finding the train partner of each berth. Can you write a program to do the same?
'''

n = int(input())
arr = []
res_arr = []

for _ in range(n):
    arr.append(int(input()))

for i in range(n):
    rem = arr[i] % 8
    if(rem > 3):
        if(rem == 7):
            res_arr.append(arr[i] + 1)
        else:
            res_arr.append(arr[i] - 3)

    else:
        if(rem == 0):
            res_arr.append(arr[i] - 1)
        else:
            res_arr.append(arr[i] + 3)

for i in range(len(res_arr)):
    rem = res_arr[i] % 8
    if(rem == 0):
        res_arr[i] = str(res_arr[i])+'SU'
    if(rem == 1 or rem == 4):
        res_arr[i] = str(res_arr[i])+'LB' 
    if(rem == 2 or rem == 5):
        res_arr[i] = str(res_arr[i])+'MB'
    if(rem == 3 or rem == 6):
        res_arr[i] = str(res_arr[i])+'UB'
    if(rem == 7):
        res_arr[i] = str(res_arr[i])+'SL'
    print(res_arr[i])
