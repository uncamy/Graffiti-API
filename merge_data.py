import pandas as pd

f1 = pd.read_csv('./graffiti_geocode.csv')
f2 = pd.read_csv('./graffiti_geocode2.csv')
f3 = pd.read_csv('./graffiti_geocode3.csv')
f4 = pd.read_csv('./graffiti_geocode4.csv')
f5 = pd.read_csv('./graffiti_geocode5.csv')
f6 = pd.read_csv('./graffiti_geocode6.csv')
f7 = pd.read_csv('./graffiti_geocode7.csv')

full= f1.append(f2)
full1 = full.append(f3)
full2 = full1.append(f4)
full3 = full2.append(f5)
full4 = full3.append(f6)
full5 = full4.append(f7)

full5.to_csv('./geocoded_manhattan.csv')
