#!/bin/python3

import os
import sys

# Complete the averageOfTopEmployees function below.
def averageOfTopEmployees(rating):
    a= (rating)
    k=0
    s=0
    for i in a:
        if i>=90:
            s=s+i
            s=s+0.00
            k=k+1
    s=s/k
    s=round(s,2)
    print (("%0.2f")%(s))
            

if __name__ == '__main__':
    n = int(input())

    rating = []
    k=0
    t=0
    for i in range(n):
        rating_item = int(input())
        rating.append(rating_item)

    averageOfTopEmployees(rating)
