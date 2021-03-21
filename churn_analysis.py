############### IMPORT DEPENDENCIES & SET FORMATS ###############
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.options.display.float_format = '${:,.2f}'.format

# Format Currency Function for Plotting
def formatCurrency(x):
    if x < 0:
        return "$({:,.2f})".format(abs(x))
    else:
        return "${:,.2f}".format(x)

############### OPEN CSV & READ INTO DATAFRAME ###############
file_name = 'Churn_analysis_East'
final_file_name = file_name + '.csv'
read_my_file = pd.read_csv(final_file_name)
df = pd.DataFrame(read_my_file)
print(f'{final_file_name} loaded!')

############### FORMAT BUILDING NAME ###############
df['Building Name'] = df['Building Name'].astype(str)
df['Building Name'] = df['Building Name'].str.zfill(6)

############### CONVERT ATTRIBUTED CHURN TO FLOAT ###############
df.replace(to_replace =" $-   ", value ='0', inplace = True)                    # replace blanks with 0
df['Attributed Churn'] = df['Attributed Churn'].astype(float)

############### PLOT TOTAL CHURN BY GEO (BAR)) ###############
geo_total = df.groupby(['Geography'])['Attributed Churn'].sum().sort_values()
geo_total.plot.bar(title = 'Attributed Churn by GEO 2019-2020')
plt.xlabel('Geography')
plt.xticks(rotation=45, ha='right')
plt.ylabel("Attributed Churn Bookings")
plt.show()

############### PLOT TOP 10 MARKETS BY CHURN (BAR) ###############
market_total = df.groupby(['Market Lookup'])['Attributed Churn'].sum().sort_values().head(10)
market_total.plot.bar(title = 'Attributed Churn by GEO 2019-2020')
plt.xlabel('Market')
plt.xticks(rotation=45, ha='right')
plt.ylabel("Attributed Churn Bookings")
plt.show()
