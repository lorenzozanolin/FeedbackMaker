from docx2python import docx2python

def flatten(lista): #used to flat the result from the parsed word file
    if isinstance(lista, list):
        if len(lista) == 1:
            return flatten(lista[0])
        else:
            return [elemento for sublist in lista for elemento in flatten(sublist)]
    else:
        return [lista]


def readPlan(path : str): #-> str:
    doc = docx2python(path)
    
    fullText = doc.body
    fullText = flatten(fullText)
    
    #print(fullText)
    plan = cleanPlan(fullText)
    print(plan)
    
def cleanPlan(fullText : list) -> list:
    fullText.pop(0) #remove name
    fullText = [value for value in fullText if 'NEL WARM UP 'not in value]  #remove useless info
    fullText = fullText[:fullText.index("CIRCUITO ADDOME")-1] #remove abs and the remainders
    program = '\n'.join(fullText) 
    program = program.split("GIORNO")
    program.pop(0)
    
    days=[]
    for i in program:
        day=''.join(i).split("\n--\t")
        day = [d.replace("\n","") for d in day ]
        days.append(day)
    return days
    
    
    
    
    
#if __name__ == "main.py":
    # input per l'utente che gli chiede il mese
#path = "/Users/lorenzozanolin/Library/Mobile Documents/com~apple~CloudDocs/Allenamento/Streetlifting/Mese 9/Lorenzo Zanolin #9.docx"
path = "../Streetlifting/Mese 9/Lorenzo Zanolin #9.docx"
#print(saveDays(readPlan(path=path))[0])
readPlan(path)