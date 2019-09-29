'''

You are on a flight and wanna watch two movies during this flight.
You are given int[] movie_duration which includes all the movie durations.
You are also given the duration of the flight which is d in minutes.
Now, you need to pick two movies and the total duration of the two movies is less than or equal to (d - 30min).
Find the pair of movies with the longest total duration. If multiple found, return the pair with the longest movie.

e.g.
Input
movie_duration: [90, 85, 75, 60, 120, 150, 125]
d: 250

Output from aonecode.com
[90, 125]
90min + 125min = 215 is the maximum number within 220 (250min - 30min)

'''


def find_longest_movie(m_dur, f_dur):
    max_dur = f_dur - 30

    # variable to always hold the max value
    movie_dur = 0

    # variable to hold the max duration movie pairs
    movies_pair = []

    for i in range(len(m_dur) - 1):
        j = i+1

        while j < len(m_dur):

            # get the duration of current pair of movies
            current_movies_dur = m_dur[i]+m_dur[j]

            # checking if total duration of the two movies is less than or equal to (d - 30min)
            if current_movies_dur <= max_dur:
                # if movie dur > current max movie dur, assign the current values to placeholders
                if current_movies_dur > movie_dur:
                    movie_dur = current_movies_dur
                    movies_pair = [m_dur[i], m_dur[j]]
                # if current movie dur is equal to the existing movie_dur value
                elif current_movies_dur == movie_dur:
                    # then check which one has the longest duration movie.
                    # If current movies pair has longest duration, assign it to movies_pair placeholder
                    if max(movies_pair) < max([m_dur[i],m_dur[j]]):
                        movies_pair = [m_dur[i],m_dur[j]]

            j += 1


    return movies_pair


movies = find_longest_movie([90, 85, 75, 60, 120, 150, 125, 100], 250)
print(movies)