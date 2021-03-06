# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS TIME"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (songplay_id SERIAL
                                        , start_time timestamp NOT NULL 
                                        , user_id text
                                        , level text
                                        , song_id text
                                        , artist_id text
                                        , session_id int
                                        , location text
                                        , user_agent text
                                        , PRIMARY KEY (songplay_id))
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (user_id text
                                    , first_name text
                                    , last_name text
                                    , gender text
                                    , level text
                                    , PRIMARY KEY (user_id)
                                    , CONSTRAINT user_id_fk (user_id) REFERENCES songplays(user_id)
)
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (song_id text
                                    , title text
                                    , artist_id text NOT NULL
                                    , year int
                                    , duration float
                                    , PRIMARY KEY (song_id)
                                    , CONSTRAINT song_id_fk (song_id) REFERENCES songplays(song_id)
)
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (artist_id text
                                    , name text
                                    , location text
                                    , latitude float
                                    , longitude float
                                    , PRIMARY KEY (artist_id)
                                    , CONSTRAINT artist_id_fk (artist_id) REFERENCES songplays(artist_id)
)
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (start_time timestamp
                                    , hour int
                                    , day int
                                    , week int
                                    , month int
                                    , year int
                                    , weekday int
                                    , PRIMARY KEY (start_time)
                                    , CONSTRAINT start_time_fk (start_time) REFERENCES songplays(start_time)
)
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (start_time
                        , user_id
                        , level
                        , song_id
                        , artist_id
                        , session_id
                        , location
                        , user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
INSERT INTO users (user_id
                    , first_name
                    , last_name
                    , gender
                    , level) VALUES (%s, %s, %s, %s, %s) ON CONFLICT(user_id) DO UPDATE SET level = excluded.level;
""")

song_table_insert = ("""
INSERT INTO songs (song_id
                    , title
                    , artist_id
                    , year
                    , duration) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (song_id) DO NOTHING;
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id
                        , name
                        , location
                        , latitude
                        , longitude) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (artist_id) DO NOTHING;
""")


time_table_insert = ("""
INSERT INTO time (start_time
                    , hour
                    , day
                    , week
                    , month
                    , year
                    , weekday) VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT (start_time) DO NOTHING;
""")

# FIND SONGS

song_select = ("""
SELECT song_id, a.artist_id
FROM songs s
LEFT JOIN artists a ON (s.artist_id = a.artist_id)
WHERE s.title = %s
        AND a.name = %s
        AND s.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]