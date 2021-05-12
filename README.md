# Song Recommendation Engine by Mood

Authors: Donna Lee 

## Data Overview 

I wanted to create a recommendation engine that took in user input for song and mood to generate song reommendations. 

For my main dataset, I got a dataset from Kaggle (which was obtained through the Spotify API) which contains more than 500K songs and their audio features. 

The first step was to label the songs into three different moods. For a subset of the data, I grabbed labels from user created Spotify playlists. For this MVP, I decided to go with three fundamental moods; happy, sad and angry. 

I got 50 playlists per mood and used that as my labels for the songs that appeared in the playlists. That list of songs with labels came out to be around 8K songs. I used that data to train two classification models, Random Forest and KNN. 

Using my best model I predicted the mood of the remaining 500K songs in my main dataset from Kaggle. 

With all songs labeled with moods, I used a Euclidean distance recommendation system to take a user inputted song and desired mood to generate the top ten songs that are similar in sound and labeled as that specific mood. 

Comprehensive tracks information can be downloaded here:  https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks?select=data_w_genres.csv 

Each song had the following attributes: 
* Acousticness
* Danceability
* Duration 
* Energy
* Instrumentalness
* Liveness
* Loudness
* Speechiness
* Tempo
* Key
* Mode
* Release Date

## EDA

With 150 playlists, in order for a song to be categorized as one of the three moods, it had to have appeared in two or more of these playlists. 

This threshold gave me a training dataset of around 2,000 songs with playlist labels. 

![image](https://user-images.githubusercontent.com/76017120/117242575-884fd400-ae03-11eb-9dcc-3bbd8074297d.png)

There wasn't much of a class weight imbalance. The models used balanced class weight anyways. 

![image](https://user-images.githubusercontent.com/76017120/117242634-a289b200-ae03-11eb-8c30-067cf44fa09e.png)


Take a look at my most important features for my classification model, I noticed that happy and angry songs were very similar in audio makeup. This explains why the model wasn't very good at predicting angry songs!

![image](https://user-images.githubusercontent.com/76017120/118056194-7a480900-b357-11eb-8137-c99a31455c3c.png)



## Model Selection and Tuning

I ran two models - _KNN_ and _Random Forest_ and optimized towards a F1 Score because both precision and recall were important for this.  


| Model         | F1 Score    |
| -----------   | ----------- |
| Random Forest |   0.8162    |
|  KNN          |   0.7853    |


The **Random Forest** model had the highest F1 score so I used that when predicting the moods of the songs with missing labels.

![image](https://user-images.githubusercontent.com/76017120/117242777-eb416b00-ae03-11eb-8977-f5b0013d6274.png)

The **KNN** model wasn't far behind with the predictions. 
![image](https://user-images.githubusercontent.com/76017120/118056353-c98e3980-b357-11eb-8584-18370db0c6ec.png)


## Predictions 

![image](https://user-images.githubusercontent.com/76017120/117242893-2a6fbc00-ae04-11eb-8ea7-797eb2454d0b.png)

These were some of the mood predictions! 

There was a huge class imbalance in the predictions. There were 200K+ songs predicted for each happy and song category but only 37K for the angry category. This is likely due to the overlap of song features between angry and happy songs. 


Below are some predictions for the recommendation engine for the song "We Belong Together" by Mariah Carey. 
![image](https://user-images.githubusercontent.com/76017120/118056558-2ab60d00-b358-11eb-8e88-d5200fb1b6a6.png)
Angry Recommendations 


![image](https://user-images.githubusercontent.com/76017120/118056571-31dd1b00-b358-11eb-8802-78fae4d66975.png)
Sad Recommendations


![image](https://user-images.githubusercontent.com/76017120/118056581-36a1cf00-b358-11eb-9857-dc05319c50bd.png)
Happy Recommendations


## Future steps
In some of the labeling, songs that had a slower tempo but positive lyrics were categorized as sad songs. This led to some issues with the predictions. Future steps include using NLP to analyze the lyrics for better predictions on the mood of a song and gathering more labels for older songs. Older songs were underrepresented in the training set which may have further skewed the predictions. 

## Resources
Kaggle Dataset - https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks?select=data_w_genres.csv 

Get a Playlist Spotify API - https://api.spotify.com/v1/playlists/{playlist_id}
  
Audio Features Spotify API - https://api.spotify.com/v1/audio-features
