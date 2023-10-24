import numpy as np
import locale

# Formats the number into INR format
def formatINR(number):
    s, *d = str(number).partition(".")
    r = ",".join([s[x-2:x] for x in range(-3, -len(s), -2)][::-1] + [s[-3:]])
    return "".join([r] + d)

def getAverageSalary(result_list):
    salary=np.array([])
    for element in result_list:
        if int(element['salary'])>0:
            salary=np.append(salary,int(element['salary']))
    return formatINR(round(np.mean(salary)))
    
