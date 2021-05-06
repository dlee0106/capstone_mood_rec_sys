# Song Recommendation Engine by Mood

Authors: Donna Lee 

## Data Overview 

I wanted to create a recommendation engine that took in user input for song and mood to generate song reommendations. I used a comprehensive dataset with 500K+ songs and their audio features as well as mood labels from 150 mood playlists from Spotify. 

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

For my initial model, I chose three foundational moods: happy, angry and sad. I had 150 mood playlists and in order for a song to be categorized as one of the three moods, it had to have appeared in two or more of these playlists. 

This threshold gave me a training dataset of around 2,000 songs with playlist labels. 

![image](https://user-images.githubusercontent.com/76017120/117242575-884fd400-ae03-11eb-9dcc-3bbd8074297d.png)

There wasn't much of a class weight imbalance. The models used balanced class weight anyways. 

![image](https://user-images.githubusercontent.com/76017120/117242634-a289b200-ae03-11eb-8c30-067cf44fa09e.png)

The popularity of each mood category was also very similar. 



## Model Selection and Tuning

I ran two models - _KNN_ and _Random Forest_ and optimized towards a F1 Score because both precision and recall were important for this.  


| Model         | F1 Score    |
| -----------   | ----------- |
| Random Forest |   0.8126    |
|  KNN          |   0.7533    |


The **Random Forest** model had the highest F1 score so I used that when predicting the moods of the songs with missing labels.

![image](https://user-images.githubusercontent.com/76017120/117242777-eb416b00-ae03-11eb-8977-f5b0013d6274.png)

The model was pretty good at predicting all three moods. The most common mistake was sad songs getting categorized as happy songs. 

## Predictions 

![image](https://user-images.githubusercontent.com/76017120/117242893-2a6fbc00-ae04-11eb-8ea7-797eb2454d0b.png)

These were some of the predictions! 

There was a huge class imbalance in the predictions. There were 200K+ songs predicted for each happy and song category but only 37K for the angry category. This is likely due to the overlap of song features between angry and happy songs. 

## Future steps
In some of the labeling, songs that had a slower tempo but positive lyrics were categorized as sad songs. This led to some issues with the predictions. Future steps include fine tuning the labeling and creating the recommendation engine. 

## Resources
Kaggle Dataset - https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks?select=data_w_genres.csv 

Get a Playlist Spotify API - https://api.spotify.com/v1/playlists/{playlist_id}
  
Audio Features Spotify API - https://api.spotify.com/v1/audio-features
