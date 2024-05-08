#mancano
    # input per l'utente che gli chiede il mese
    # input per l'utente che seleziona il giorno
    # ratings
    # genera il commento
    

from docx2python import docx2python

def flatten(lista): #used to flat the result from the parsed word file
    if isinstance(lista, list):
        if len(lista) == 1:
            return flatten(lista[0])
        else:
            return [elemento for sublist in lista for elemento in flatten(sublist)]
    else:
        return [lista]


def readPlan(path : str) -> list:   #used to read from word file, parse it and create a list of lists, each one contains the program of a single day
    doc = docx2python(path)
    
    fullText = doc.body
    fullText = flatten(fullText)
    
    plan = cleanPlan(fullText)
    return plan
    
def cleanPlan(fullText : list) -> list:
    fullText.pop(0) #remove name
    fullText = [value for value in fullText if 'NEL WARM UP 'not in value]  #remove useless info
    fullText = fullText[:fullText.index("CIRCUITO ADDOME")-1] #remove abs and the remainders
    program = '\n'.join(fullText) #create from the list a single string
    program = program.split("GIORNO")   #recreate a list which element contains a single day
    program.pop(0)  #remove the first element, useless
    
    days=[]
    for i in program:
        day=''.join(i).split("\n--\t")  #first create a single string from all the elements of the day, then split each day by the exercise (--t) and then create a new list
        day = [d.replace("\n","") for d in day ]    #remove all newlines command 
        days.append(day[1:])    #remove the number of the day, useless
    return days
    
    
    
    
path = "../Streetlifting/Mese 9/Lorenzo Zanolin #9.docx"
plan = readPlan(path)

