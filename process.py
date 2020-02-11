import pandas as pd
import json
import matplotlib.pyplot as plt

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values) 
        val = int(round(pct*total/100.0))
        return '({v:d})'.format(v=val)
    return my_autopct

def draw_graph(title,field,other_tolerance,make_other,main_bar,other_bar):

    df[field].fillna('Unknown',inplace=True)
    df[field].replace('Generic','Unknown',inplace=True)


    makes = df[field].value_counts()
    if make_other:
        main = makes[makes > other_tolerance]
        other = makes[makes<=other_tolerance]
        main = main.append(pd.Series([other.sum()],['Other']))
    else:
        main = makes

    if make_other:
        explode = []

        for i in range(len(main)-1):
            explode.append(0)
        explode.append(0.2)


    if not main_bar:
        main.plot.pie(autopct = make_autopct(main))
    else:
        plt.subplots(figsize=(8,6))
        main.plot.bar()
        plt.ylabel("Device Count")
        plt.xlabel("Device "+ field.capitalize())

    plt.title(title,size=16)
    plt.ylabel("")
    plt.tight_layout()
    plt.show()

    if make_other:
        if not other_bar:
            other.plot.pie(autopct = make_autopct(other))
            plt.ylabel("")
        else:
            plt.subplots(figsize=(8,6))
            other.plot.bar()
            plt.ylabel("Device Count")
            plt.xlabel("Device "+ field.capitalize())
            

        plt.title("Other Devices",size=16)
        
        plt.tight_layout()
        plt.show()

data = json.load(open('data/data.json'))

header = pd.DataFrame(data['network'])

df = pd.DataFrame(data["devices"])


draw_graph("Manufacturers of Devices",'make',7,True,False,False)
draw_graph("Types of Devices",'type',22,True,False,False)
draw_graph("Models of Devices",'model',7,True,False,True)