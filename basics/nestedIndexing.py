albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]

# Add your code below this comment.
for album_name, album_artist, album_year, songs_list in albums:
    if album_name == "Bad Company":
        for index, song_name in songs_list:
            if song_name == "The Way I Choose":
                print(song_name)
    elif album_name == "Nightflight":
        print(album_year)
    elif album_name == "More Mayhem":
        for index, song_name in songs_list:
            if song_name == "Kentish Town Waltz":
                print(index)

for album_name, album_artist, album_year, songs_list in albums:
    if album_name == "Nightflight":
        for song in songs_list:
            index, song_name = song
            if song_name == "Keeping a Rendezvous":
                print(song)
