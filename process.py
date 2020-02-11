import pandas as pd
import json
import matplotlib.pyplot as plt

write_to_file = False
file_name = 'output/file_'
file_extension = '.png'
file_index = 0

def print_graph(plt):

    if write_to_file:
        plt.savefig(file_name + str(file_index) + file_extension)
        file_index=file_index+1
    else:
        plt.show()


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
    
    main = makes[makes > other_tolerance]
    other = makes[makes<=other_tolerance]
    if len(other) > 0:
        main = main.append(pd.Series([other.sum()],['Other']))

    if make_other:
        explode = []

        for i in range(len(main)-1):
            explode.append(0)
        explode.append(0.2)


    if not main_bar:
        if make_other:
            main.plot.pie(explode = explode, autopct = make_autopct(main))
        else:  
            main.plot.pie(autopct = make_autopct(main))
    else:
        plt.subplots(figsize=(8,6))
        main.plot.bar()
        plt.ylabel("Device Count")
        plt.xlabel("Device "+ field.capitalize())

    plt.title(title,size=16)
    plt.ylabel("")
    plt.tight_layout()
    print_graph(plt)

    if make_other:
        if not other_bar:
            other.plot.pie(autopct = make_autopct(other))
            plt.ylabel("")
        else:
            #plt.subplots(figsize=(8,6))
            other.plot.bar()
            plt.ylabel("Device Count")
            plt.xlabel("Device "+ field.capitalize())
            

        plt.title("Other Devices",size=16)
        
        plt.tight_layout()
        print_graph(plt)

data = json.load(open('data/data.json'))

network_header = pd.DataFrame(data['network'])
internet_header = pd.DataFrame(data['internet'],index=[0])


df = pd.DataFrame(data["devices"])
device_count = len(df)

name = pd.DataFrame(network_header['name']).iloc[0]['name']
date = pd.DataFrame(network_header['last_changed']).iloc[0]['last_changed']



provider = pd.DataFrame(internet_header['provider']).iloc[0]['provider']
city = pd.DataFrame(internet_header['city']).iloc[0]['city']
region = pd.DataFrame(internet_header['region']).iloc[0]['region']


print("Analysis of " + str(device_count) +" devices on network \"" + name +"\" on " + date + ".")
print("Internet provided by "+ provider+" located in " + city +", " + region +".")



draw_graph("Manufacturers of Devices",'make',7,True,False,False)
draw_graph("Types of Devices",'type',22,True,False,False)
draw_graph("Models of Devices",'model',7,True,False,True)
