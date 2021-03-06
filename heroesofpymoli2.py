import pandas as pd
import numpy as np

file_to_load = "purchase_data.csv"

purchase_data_df = pd.read_csv(file_to_load)
purchase_data_df.head()

player_count = len(purchase_data_df["SN"].unique())
print(player_count)

different_items = purchase_data_df["Item ID"].value_counts()
unique_items = different_items.count()
average_price = purchase_data_df["Price"].mean()
number_of_purchases = len(purchase_data_df["Purchase ID"].unique())
total_revenue = purchase_data_df["Price"].sum()

summary_table = pd.DataFrame({"Number of Unique Items": unique_items,
                              "Average Price": [average_price],
                              "Number of Purchases": [number_of_purchases],
                              "Total Revenue": [total_revenue],
                             })
summary_table

gender_tally_df = purchase_data_df[["SN", "Gender"]]
drop_df = gender_tally_df.drop_duplicates()
drop_two = drop_df["Gender"].value_counts()
gender_figure = drop_two/player_count * 100

summary_table_gender = pd.DataFrame({"Total Count": drop_two,
                                     "Percentage of Players": gender_figure})
summary_table_gender

purchase_group = purchase_data_df.groupby(["Gender"])
total_price = purchase_group["Price"].sum()
gender_count = purchase_data_df["Gender"].value_counts()
average_price = total_price/gender_count
per_person = total_price/drop_two

summary_table_gender_purchasing = pd.DataFrame({"Purchase Count": gender_count,
                                  "Average Purchase Price": average_price,
                                  "Total Purchase Value": total_price,
                                  "Avg Total Purchase per Person": per_person,
                                 })
summary_table_gender_purchasing

drop_four = purchase_data_df.drop_duplicates("SN")
bins = [0, 10, 14, 19, 24, 29, 34, 39, 100]
group_labels = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]
group_numbers = pd.cut(drop_four["Age"], bins, labels = group_labels)
group_totals = group_numbers.value_counts().sort_index()
age_pct = group_totals/player_count * 100

summary_table_age_demo = pd.DataFrame({"Total Count": group_totals,
                                    "Percentage of Players": age_pct})
summary_table_age_demo

purchase_numbers = pd.cut(purchase_data_df["Age"], bins, labels = group_labels)
purchase_plus = purchase_numbers.value_counts().sort_index()
purchase_data_df["Age Group"] = pd.cut(purchase_data_df["Age"], bins, labels = group_labels)

purchase_age = purchase_data_df.groupby(["Age Group"])
total_sales = purchase_age["Price"].sum()
average_sales = total_sales/purchase_plus
per_player = total_sales/group_totals

summary_table_age_purchase = pd.DataFrame({"Purchase Count": purchase_plus, 
                                   "Average Purchase Price": average_sales,
                                   "Total Purchase Value": total_sales,
                                   "Avg Total Purchase per Person": per_player})
summary_table_age_purchase

top_spenders_df = purchase_data_df[["SN", "Price", "Item Name"]]
total_spending = top_spenders_df.groupby("SN").sum()
total_spending.sort_values(by = "Price", ascending = False, inplace = True)

names = list(total_spending.index.values)
top_names = [names[0],names[1],names[2],names[3],names[4]]

total_money_values_1 = total_spending.iloc[0,0]
total_money_values_2 = total_spending.iloc[1,0]
total_money_values_3 = total_spending.iloc[2,0]
total_money_values_4 = total_spending.iloc[3,0]
total_money_values_5 = total_spending.iloc[4,0]
top_buyers = [total_spending.iloc[0,0], total_spending.iloc[1,0], total_spending.iloc[2,0], total_spending.iloc[3,0],
                      total_spending.iloc[4,0]]

top_purchases_1 = top_spenders_df[top_spenders_df["SN"] == names[0]].count()[0]
top_purchases_2 = top_spenders_df[top_spenders_df["SN"] == names[1]].count()[0]
top_purchases_3 = top_spenders_df[top_spenders_df["SN"] == names[2]].count()[0]
top_purchases_4 = top_spenders_df[top_spenders_df["SN"] == names[3]].count()[0]
top_purchases_5 = top_spenders_df[top_spenders_df["SN"] == names[4]].count()[0]
top_purchase_counts = [top_purchases_1, top_purchases_2, top_purchases_3, top_purchases_4,
                       top_purchases_5]

average_price_1 = total_money_values_1/top_purchases_1
average_price_2 = total_money_values_2/top_purchases_2
average_price_3 = total_money_values_3/top_purchases_3
average_price_4 = total_money_values_4/top_purchases_4
average_price_5 = total_money_values_5/top_purchases_5
average_prices = [average_price_1, average_price_2, average_price_3, average_price_4, average_price_5]

summary_table_spenders = pd.DataFrame({"SN": top_names,
                                       "Purchase Count": top_purchase_counts,
                                       "Average Purchase Price": average_prices,
                                       "Total Purchase Value": top_buyers,})
summary_table_spenders

top_sellers_df = purchase_data_df[["Item ID", "Item Name", "Price"]]
hot_items = top_sellers_df.groupby("Item ID").count()
hot_items.sort_values(by = "Item Name", ascending = False, inplace = True)
top_sellers_df = top_sellers_df.drop_duplicates(["Item ID", "Item Name"])
item_ids = [hot_items.index[0], hot_items.index[1], hot_items.index[2], hot_items.index[3], hot_items.index[4]]

name_1 = top_sellers_df.loc[top_sellers_df["Item ID"] == item_ids[0], "Item Name"].item()
name_2 = top_sellers_df.loc[top_sellers_df["Item ID"] == item_ids[1], "Item Name"].item()
name_3 = top_sellers_df.loc[top_sellers_df["Item ID"] == item_ids[2], "Item Name"].item()
name_4 = top_sellers_df.loc[top_sellers_df["Item ID"] == item_ids[3], "Item Name"].item()
name_5 = top_sellers_df.loc[top_sellers_df["Item ID"] == item_ids[4], "Item Name"].item()
hot_item_names = [name_1, name_2, name_3, name_4, name_5]
item_counts = [hot_items.iloc[0,0], hot_items.iloc[1,0], hot_items.iloc[2,0], hot_items.iloc[3,0], hot_items.iloc[4,0]]

price_1 = top_sellers_df.loc[top_sellers_df["Item Name"] == hot_item_names[0], "Price"].item()
price_2 = top_sellers_df.loc[top_sellers_df["Item Name"] == hot_item_names[1], "Price"].item()
price_3 = top_sellers_df.loc[top_sellers_df["Item Name"] == hot_item_names[2], "Price"].item()
price_4 = top_sellers_df.loc[top_sellers_df["Item Name"] == hot_item_names[3], "Price"].item()
price_5 = top_sellers_df.loc[top_sellers_df["Item Name"] == hot_item_names[4], "Price"].item()
item_prices = [price_1,price_2,price_3,price_4,price_5]
total_sale = [hot_items.iloc[0,0]*price_1, hot_items.iloc[1,0]*price_2, hot_items.iloc[2,0]*price_3, 
                hot_items.iloc[3,0]*price_4, hot_items.iloc[4,0]*price_5]

summary_table_popular_items = pd.DataFrame({"Item ID": item_ids,
                                            "Item Name": hot_item_names,
                                            "Purchase Count": item_counts,
                                            "Item Price": item_prices,
                                            "Total Purchase Value": total_sale})
summary_table_popular_items

money_makers_df = purchase_data_df[["Item ID", "Item Name", "Price"]]
profitable_items = money_makers_df.groupby("Item ID").sum()
profitable_items.sort_values(by = "Price", ascending = False, inplace = True)
money_makers_df = money_makers_df.drop_duplicates(["Item ID", "Price"])
item_numbers = [profitable_items.index[0], profitable_items.index[1], profitable_items.index[2], profitable_items.index[3], profitable_items.index[4]]

name_1 = money_makers_df.loc[money_makers_df["Item ID"] == item_numbers[0], "Item Name"].item()
name_2 = money_makers_df.loc[money_makers_df["Item ID"] == item_numbers[1], "Item Name"].item()
name_3 = money_makers_df.loc[money_makers_df["Item ID"] == item_numbers[2], "Item Name"].item()
name_4 = money_makers_df.loc[money_makers_df["Item ID"] == item_numbers[3], "Item Name"].item()
name_5 = money_makers_df.loc[money_makers_df["Item ID"] == item_numbers[4], "Item Name"].item()
profit_names = [name_1, name_2, name_3, name_4, name_5]
profit_values = [profitable_items.iloc[0,0],profitable_items.iloc[1,0],profitable_items.iloc[2,0],profitable_items.iloc[3,0],profitable_items.iloc[4,0]]

price_1 = money_makers_df.loc[money_makers_df["Item ID"] == item_numbers[0], "Price"].item()
price_2 = money_makers_df.loc[money_makers_df["Item ID"] == item_numbers[1], "Price"].item()
price_3 = money_makers_df.loc[money_makers_df["Item ID"] == item_numbers[2], "Price"].item()
price_4 = money_makers_df.loc[money_makers_df["Item ID"] == item_numbers[3], "Price"].item()
price_5 = money_makers_df.loc[money_makers_df["Item ID"] == item_numbers[4], "Price"].item()
profit_prices = [price_1,price_2,price_3,price_4,price_5]
money_makers_df_two = purchase_data_df[["Item ID", "Item Name", "Price"]].groupby("Item Name").count()

count_1 = money_makers_df_two.loc[money_makers_df_two.index == profit_names[0], "Item ID"].item()
count_2 = money_makers_df_two.loc[money_makers_df_two.index == profit_names[1], "Item ID"].item()
count_3 = money_makers_df_two.loc[money_makers_df_two.index == profit_names[2], "Item ID"].item()
count_4 = money_makers_df_two.loc[money_makers_df_two.index == profit_names[3], "Item ID"].item()
count_5 = money_makers_df_two.loc[money_makers_df_two.index == profit_names[4], "Item ID"].item()
counts = [count_1, count_2, count_3, count_4, count_5]

summary_table_profitable = pd.DataFrame({"Item ID": item_numbers,
                                         "Item Name": profit_names,
                                         "Purchase Count": counts,
                                         "Item Price": profit_prices,
                                         "Total Purchase Value": profit_values})
summary_table_profitable
