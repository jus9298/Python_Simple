

import pandas as pd
from db.movie_dao import get_reviews
from datetime import datetime


reviews = get_reviews()
for item in reviews:
    print(item)

df_save = pd.DataFrame(reviews)
print(df_save)

now = datetime.now().strftime("%Y%m%d")
df_save.to_excel(f"./review_{now}.xlsx", index=False)