import pandas as pd
import json
import matplotlib.pyplot as plt

data = json.load(open('data/data.json'))

header = pd.DataFrame(data['network'])

df = pd.DataFrame(data["devices"])

df['make'].fillna('Unknown',inplace=True)

makes = df['make'].value_counts()
main = makes[makes > 7]
other = makes[makes<=7]
main = main.append(pd.Series([other.sum()],['Other']))

explode = []

for i in range(len(main)-1):
    explode.append(0)
explode.append(0.2)

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '({v:d})'.format(v=val)
    return my_autopct

main.plot.pie(explode=explode, autopct = make_autopct(main))

plt.title("Manufacturers of Devices",size=16)
plt.ylabel("")
plt.show()

other.plot.pie(autopct = make_autopct(other))
plt.title("Other Devices",size=16)
plt.ylabel("")


plt.show()

df['model'].fillna('Unknown',inplace=True)

makes = df['model'].value_counts()
main = makes[makes > 7]
other = makes[makes<=7]
main = main.append(pd.Series([other.sum()],['Other']))

explode = []

for i in range(len(main)-1):
    explode.append(0)
explode.append(0.2)

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '({v:d})'.format(v=val)
    return my_autopct

main.plot.pie(explode=explode, autopct = make_autopct(main))

plt.title("Models of Devices",size=16)
plt.ylabel("")
plt.show()

plt.subplots(figsize=(10,5))
other.plot.bar()

plt.title("Other Devices",size=16)
plt.ylabel("")


plt.show()

df['type'].fillna('Unknown',inplace=True)
df['type'].replace('Generic','Unknown',inplace=True)

makes = df['type'].value_counts()
main = makes[makes > 22]
other = makes[makes<=22]
main = main.append(pd.Series([other.sum()],['Other']))

explode = []

for i in range(len(main)-1):
    explode.append(0)
explode.append(0.2)

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '({v:d})'.format(v=val)
    return my_autopct

main.plot.pie(explode=explode, autopct = make_autopct(main))

plt.title("Types of Devices",size=16)
plt.ylabel("")
plt.show()

other.plot.pie(autopct = make_autopct(other))
plt.title("Other Devices",size=16)
plt.ylabel("")


plt.show()
