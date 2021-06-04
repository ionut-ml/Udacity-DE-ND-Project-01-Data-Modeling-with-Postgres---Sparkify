# Udacity Data Engineer Nano-Degree Project 01: Data Modeling with Postgres - Sparkify

## Database Purpose

A fictional music streaming app Sparkify wants to understand user preferences and what they are listening to by analyzing the data collected by their app. 

Currently the startup has its information on songs metadata and user activity stored in JSON files in separate directories. However, this is difficult to query and analyize. Therefore, the goal is to create a easy to query database for the analytics team, thus catered to certain queries, in particular to be optimized for song play analysis. Because of this we will not be pursueing a 3NF form for the database, but a more *query-friendly* star schema.


## Database Schema

As stated above, because we are required to create a database optimized for queries, in particular song play analysis, we decided on the classic star schema which is easy to understand and use, and write queries against for end users. 

To this end, the **Fact table** will be called `songplays` with the following columns: `songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent`.

The **Dimension tables** will be the following (with their respective columns):

* `users` - Users of the app. Columns: `user_id, first_name, last_name, gender, level`
* `songs` - Songs that are available. Columns: `song_id, title, artist_id, year, duration`
* `artists` - Artists of the songs. Columns: `artist_id, name, location, latitude, longitude`
* `time` - Timestamps for the songplays, with additional info in time units. Columns: start_time, hour, day, week, month, year, weekday

## ETL Pipeline

The ETL pipeline starts by extracting the information on song metadata from its directory. It does this by walking the directory and its subdirectory and collecting a list of files. Then, it loops through the file list and creates a dataframe from each one and creates 2 subsets: one with the columns for `songs` and one for `artists`. This would be the transformation part. Then it loads the rows in their respective tables in the database using a `INSERT` SQL statement predefined for each table.

In the second part of the ETL pipeline, the python script walks the user activity logs and collects a list of files, then reads each one into a pandas DataFrame and processes the data for the remaining tables. 

First, it selects a subset with just the datetime columns, filtered by the "NextSong" action. It transforms the the timestamp column from milliseconds into actual datetime, then extracts the hour, day, week of year, month, year, and weekday from it. Finally, it loads the data into the `time` table.

For the `users` table, the pipeline simply creates a subset whith the relevant columns and then inserts the rows in the DB table.

Finally, for the `songplays` table, we extract the relevant columns and because we hove no information on song_id and artists_id, we join the songs and artists table to get them, and filter the results by a given based on the title, artist name, and duration of a song.