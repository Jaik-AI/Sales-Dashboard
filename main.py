import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales.csv')
df['Revenue'] = df['Price']*df['Quantity']

print('='*30)
print("\tSALES REPORT")
print('='*30)
print(f"\nTotal revenue : ₹{df['Revenue'].sum():,}\n")

exp_product = df['Price'].idxmax()
print("\n=== Most Expensive Product ===\n")
print(f"Name  : {df.loc[exp_product,"Product"]}\nPrice : ₹{df.loc[exp_product,"Price"]:,}\n")

chp_product = df['Price'].idxmin()
print("\n=== Cheapest Product ===\n")
print(f"Name  : {df.loc[chp_product,"Product"]}\nPrice : ₹{df.loc[chp_product,"Price"]:,}\n")

best_sell = df["Quantity"].idxmax()
print("\n=== Best Selling Product ===\n")
print(f"Name     : {df.loc[best_sell,'Product']}\nPrice    : ₹{df.loc[best_sell,'Price']:,}\nQuantity : {df.loc[best_sell,'Quantity']}\n")


high_rev = df['Revenue'].idxmax()
print("\n=== Highest Revenue Product ===\n")
print(f"Name    : {df.loc[high_rev,'Product']}\nPrice   : ₹{df.loc[high_rev,"Price"]:,}\nRevenue : ₹{df.loc[high_rev,"Revenue"]:,}\n")

print("\n=== Category-Wise Revenue ===\n")
ctg_rev = df.groupby("Category")['Revenue'].sum()
for catg , rev in ctg_rev.items():
    print(f"{catg:<11} : ₹{rev:,}")

print("\n=== Average Product Price ===\n")
print(f"₹{df['Price'].mean():,.2f}")

print("\n=== Top 3 Revenue Products ===\n")
top_3 = df.sort_values('Revenue',ascending=False).head(3)
for i,(_,row) in enumerate(top_3.iterrows(),start=1):
    print(f"{i}. Name      : {row['Product']}")
    print(f"   Price     : ₹{row['Price']:,}")
    print(f"   Quantity  : {row['Quantity']}")
    print(f"   Revenue   : ₹{row['Revenue']:,}\n")

print("\n=== Highest Revenue Category ===\n")
print(f"Category : {ctg_rev.idxmax()}\n")

categories = ctg_rev.index
revenue = ctg_rev.values
plt.figure(figsize=(15,10))
# Bar Chart
plt.subplot(3,2,1)
plt.bar(categories,revenue)
plt.title("Revenue By Category")
plt.xlabel("Category")
plt.ylabel("Revenue")

# Pie chart
plt.subplot(3,2,2)
plt.pie(revenue,labels = categories, autopct= '%1.1f%%',startangle=90)
plt.title('Revenue Contribution')

# Horizontal Bar chart
plt.subplot(3,2,3)
top_5_rev = df.sort_values('Revenue',ascending= False).head(5)
product = top_5_rev['Product'].tolist()
rev  = top_5_rev['Revenue'].tolist()
plt.barh(product,rev)
plt.title('Top 5 Revenue Products')
plt.xlabel('Revenue')
plt.ylabel('Products')

# Line chart
plt.subplot(3,2,4)
plt.plot(df['Product'],df['Price'],marker = '^')
plt.title('Product Price Comparison')
plt.xlabel("Products")
plt.ylabel("Price")

plt.subplot(3,2,5)
ctg_qty = df.groupby('Category')['Quantity'].sum()
categ = ctg_qty.index
quant  = ctg_qty.values
plt.barh(categ,quant)
plt.title('Quantity Sold by Category')
plt.xlabel('Quantity')
plt.ylabel('Category')

plt.subplot(3,2,6)
plt.scatter(df['Revenue'],df['Quantity'])
plt.title("Revenue vs Quantity")
plt.xlabel('Revenue')
plt.ylabel('Quantity')
plt.tight_layout()
plt.show()