#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[9]:


df_links=pd.read_csv('links.csv')
df_links.head()


# In[5]:


df_movies=pd.read_csv('movies.csv')
df_movies.head()


# In[12]:


df_movies.shape


# In[8]:


df_tags=pd.read_csv('tags.csv')
df_tags.head()


# In[13]:


df_tags.shape


# In[10]:


df_ratings=pd.read_csv('ratings.csv')
df_ratings.head()


# In[17]:


df = pd.read_csv("ratings.csv")

# Count the number of unique userIds
unique_user_ids = df["userId"].nunique()

# Print the result
print(f"There are {unique_user_ids} unique userIds in ratings.csv")


# In[18]:


df = pd.read_csv("ratings.csv")

# Count the number of ratings for each movie
movie_ratings = df.groupby("movieId").count()["rating"]

# Find the movie with the maximum number of ratings
max_rated_movie_id = movie_ratings.idxmax()

# Read the movies CSV file into a pandas dataframe
movies_df = pd.read_csv("movies.csv")

# Get the title of the movie with the maximum number of ratings
max_rated_movie_title = movies_df[movies_df["movieId"] == max_rated_movie_id]["title"].values[0]

# Print the result
print(f"The movie with the maximum number of ratings is '{max_rated_movie_title}'")


# In[ ]:





# In[19]:


df = pd.read_csv("ratings.csv")

# Read the movies CSV file into a pandas dataframe
movies_df = pd.read_csv("movies.csv")

# Get the movieId of "Terminator 2: Judgment Day (1991)"
movie_id = movies_df[movies_df["title"] == "Terminator 2: Judgment Day (1991)"]["movieId"].values[0]

# Filter the ratings dataframe to only include ratings for "Terminator 2: Judgment Day (1991)"
t2_ratings = df[df["movieId"] == movie_id]

# Calculate the average rating
average_rating = t2_ratings["rating"].mean()

# Print the result
print(f"The average user rating for 'Terminator 2: Judgment Day (1991)' is {average_rating:.2f}")


# In[20]:


# Read the CSV file into a pandas dataframe
df = pd.read_csv("ratings.csv")

# Read the movies CSV file into a pandas dataframe
movies_df = pd.read_csv("movies.csv")

# Get the movieId of "Fight Club (1999)"
movie_id = movies_df[movies_df["title"] == "Fight Club (1999)"]["movieId"].values[0]

# Filter the ratings dataframe to only include ratings for "Fight Club (1999)"
fc_ratings = df[df["movieId"] == movie_id]

# Plot the histogram of ratings
plt.hist(fc_ratings["rating"], bins=10, edgecolor="black")

# Set the title and labels
plt.title("User Ratings Distribution for 'Fight Club (1999)'")
plt.xlabel("Rating")
plt.ylabel("Number of Users")

# Show the plot
plt.show()


# In[ ]:





# In[21]:


# Read the CSV file into a pandas dataframe
df = pd.read_csv("ratings.csv")

# Read the movies CSV file into a pandas dataframe
movies_df = pd.read_csv("movies.csv")

# Merge the two dataframes on the movieId column
merged_df = pd.merge(df, movies_df, on="movieId")

# Calculate the mean rating for each movie
mean_ratings = merged_df.groupby("title")["rating"].mean()

# Find the movie with the highest mean rating
most_popular_movie = mean_ratings.idxmax()

# Print the result
print(f"The most popular movie based on average user ratings is '{most_popular_movie}'")


# In[22]:


df = pd.read_csv("ratings.csv")

# Read the movies CSV file into a pandas dataframe
movies_df = pd.read_csv("movies.csv")

# Merge the two dataframes on the movieId column
merged_df = pd.merge(df, movies_df, on="movieId")

# Group the merged dataframe by movie title and count the number of ratings
ratings_count = merged_df.groupby("title").size()

# Sort the movies by the number of ratings in descending order and get the top 5
top_5_movies = ratings_count.sort_values(ascending=False).head(5)

# Print the result
print("The top 5 popular movies based on the number of user ratings are:")
for i, movie in enumerate(top_5_movies.index):
    print(f"{i+1}. {movie}")


# In[23]:


df = pd.read_csv("ratings.csv")

# Read the movies CSV file into a pandas dataframe
movies_df = pd.read_csv("movies.csv")

# Merge the two dataframes on the movieId column
merged_df = pd.merge(df, movies_df, on="movieId")

# Group the merged dataframe by movie title and count the number of ratings
ratings_count = merged_df.groupby("title").size()

# Sort the movies by the number of ratings in descending order and get the top 3
top_3_movies = ratings_count.sort_values(ascending=False).head(3)

# Print the result
print(f"The third most popular Sci-Fi movie based on the number of user ratings is '{top_3_movies.index[2]}'")


# In[ ]:


data = {'Column1': [1, 'apple', 'orange', 4],
        'Column2': [5, 'grape', 'banana', 8]}
df = pd.DataFrame(data)

# Convert 'Column1' to string type
df['Column1'] = df['Column1'].astype(str)

# Now you can use .str accessor on 'Column1'
filtered_df = df[df['Column1'].str.contains('apple')]

print(filtered_df)


# In[ ]:


#2
scifi_movies = dataset4[dataset4['imdbId'].str.contains('tmdbld', case=False)]

# Find the movieId with the highest IMDB rating among Sci-Fi movies
highest_rated_scifi_movie_id = scifi_movies.loc[scifi_movies['imdbId'].idxmax(), 'movieId']

print("MovieId of the Sci-Fi movie with the highest IMDB rating:", highest_rated_scifi_movie_id)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




