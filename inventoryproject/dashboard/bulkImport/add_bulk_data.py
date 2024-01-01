from faker import Faker
import random
import pandas as pd
import os


fake = Faker()

current_dir = os.getcwd()
relative_filepath = os.path.join('data', 'stock_data.csv')
data_filepath = current_dir + '/' + relative_filepath

print(data_filepath)


dealer_list = []
for _ in range(15):
    dealer_list.append(fake.name())


fake_names = []
dealer_names = []
quantity = []
quantity_list = [5, 7, 8, 9,12, 34, 45, 40,18, 17, 13]
for _ in range(200):
    fake_names.append(fake.name())
    dealer_names.append(random.choice(dealer_list))
    quantity.append(random.choice(quantity_list))




fake_df = pd.DataFrame({"Product Name": fake_names,
                        "Product Quantity": quantity,
                        "Dealer Name": dealer_names})



fake_df.to_csv(data_filepath, 
               index_label=False,
               index=False)
