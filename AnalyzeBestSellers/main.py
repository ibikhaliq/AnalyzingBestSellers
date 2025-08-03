import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages


df = pd.read_csv('bestsellers.csv') #imports a csv file of the best-selling books

# gets the first 5 rows of the spreadsheet
print(df.head())

# gets the shape of the spreadsheet
print(df.shape)

#gets the column names of the spreadsheet
print(df.columns)

#gets summary statistics for each column
print(df.describe())

df.drop_duplicates(inplace= True) #drops duplicates
df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True) #renames columns to make them easier to work with.

df["Price"] = df["Price"].astype(float) #sets price as type float

authcounts = df["Author"].value_counts() #gets number of times an author's name has appeared
print(authcounts)

avgratingbygenre = df.groupby("Genre")["Rating"].mean() # average rating of each genre
print(avgratingbygenre)

# Export top selling authors to a CSV file
authcounts.head(10).to_csv("top_authors.csv")

# Export average rating by genre to a CSV file
avgratingbygenre.to_csv("avg_rating_by_genre.csv")

with PdfPages("analyzingbestsellers.pdf") as pdf:
    #making a bar graph about the top 10 Authors by Number of Books

    authcounts.head(10).plot(kind='bar', title='Top 10 Authors by Number of Books')

    plt.xlabel('Author') #x axis

    plt.ylabel('Number of Books') #y axis

    plt.xticks(rotation=45) # labels on x axis rotated by 45 degrees

    plt.tight_layout() #ensures nothing gets cut off



    pdf.savefig() # saves graph in pdf
    plt.show()  # show graph
    plt.close()

#  pie graph showing the distribution of genre; autopct = formatting for decimals, one digit before and after decimal
    df["Genre"].value_counts().plot(kind='pie', autopct='%1.1f%%', title='Genre Distribution')

    plt.ylabel("")  # Hide y-label

    plt.tight_layout() #ensures nothing gets cut off
    pdf.savefig()
    plt.show() #show graph

    plt.close()

    #makes a boxplot for rating distribution by genre
    sns.boxplot(x='Genre', y='Rating', data=df)

    plt.title('Rating Distribution by Genre')
    pdf.savefig()
    plt.show()

    plt.close()

#plot to show average rating over the years
    avg_rating_by_year = df.groupby("Publication Year")["Rating"].mean() #average rating of each year

    avg_rating_by_year.plot(kind='line', marker='*', title='Average Rating Over Years') #line graph for average rating over the years

    plt.xlabel('Publication Year') #x axis

    plt.ylabel('Average Rating') # y axis

    plt.grid(True) #adds horizontal and vertical grid line to the plot

    plt.tight_layout() #ensures nothing gets cutoff
    pdf.savefig()
    plt.show()

    plt.close()







