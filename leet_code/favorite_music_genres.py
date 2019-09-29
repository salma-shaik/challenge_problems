'''

Favorite Genres
Given a map Map<String, List<String>> userMap, where the key is a username and the value is a list of user's songs.
Also given a map Map<String, List<String>> genreMap, where the key is a genre and the value is a list of songs belonging
to this genre.
The task is to return a map Map<String, List<String>>, where the key is a username and the value is a list of the user's
favorite genres.
Favorite genre is a genre with the most song.

Example :
Input:

userMap = {
   "David": ["song1", "song2", "song3", "song4", "song8"],
   "Emma":  ["song5", "song6", "song7"]
},
genreMap = {
   "Rock":    ["song1", "song3"],
   "Dubstep": ["song7"],
   "Techno":  ["song2", "song4"],
   "Pop":     ["song5", "song6"],
   "Jazz":    ["song8", "song9"]
}
Output:
{
   "David": ["Rock", "Techno"],
   "Emma":  ["Pop"]
}
Explanation:
David has 2 Rock, 2 Techno and 1 Jazz song. So he has 2 favorite genres.
Emma has 2 Pop and 1 Dubstep song. Pop is Emma's favorite genre.

'''

userMap = {"David": ["song1", "song2", "song3", "song4", "song8", "song9"],
           "Emma":  ["song5", "song6", "song7", "song8", "song9"]
           }


genreMap = {"Rock":    ["song1", "song3"],
            "Dubstep": ["song7"],
            "Techno":  ["song2", "song4"],
            "Pop":     ["song5", "song6"],
            "Jazz":    ["song8", "song9"]
            }


# take an empty dict to store user vs genres list
userGenres = {}

# for every user songs list
for userSongs in userMap.items():
    # take an empty list to hold genres for songs of a given user
    userGenreVals = []
    # for each song in a given user's song list
    for song in userSongs[1]:
        # for each genre in the genreMap entries
        for genre in genreMap.items():
            # check each song in a given user's songs list, check it against each genre entry
            # if a song is in a genre's (genre=key) values that means a song from this particular genre is in the current user's songs list
            if song in genre[1]:
                # append that particular genre to the current user.
                userGenreVals.append(genre[0])
    # once all the genres for current user's songs are obtained, add that entry as 'user': genres list in the userGenre dict
        userGenres[userSongs[0]] = userGenreVals

# placeholder dict to hold each genre type count for current user
userGenreCount = {}

# need to iterate over the userGenres to get the count of each genre type for every user
for uGen in userGenres.items():
    genreCount = {}
    # for each genre in current user's genre list
    for gen in uGen[1]:
        genreCount[gen] = genreCount.get(gen, 0) + 1

    # get the max value
    max_value = max(genreCount.values())

    # get keys with values same as the max value and them as a list agianst current user 
    userGenreCount[uGen[0]] = list({key for key, value in genreCount.items() if value == max_value})

print(userGenreCount)