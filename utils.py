import functools

# promedio de energia por genero
def get_gen_average_energy(song_dict):
    gen = {}
    # collect non-duplicated values
    for value in song_dict:
        gen[value["playlist_genre"]] = 0
    # a list with all genres
    gen = [genero for genero in gen]
    # dictionary that accumulates how many genres appears
    ac_gen = {genero:0 for genero in gen}
    # dictionary that accumulates energies
    cont_gen = {genero:0 for genero in gen}
    for song in song_dict:
        genero = song["playlist_genre"]
        ac_gen[genero] = ac_gen[genero] + 1
        cont_gen[genero] = cont_gen[genero] + float(song["energy"])

    # for genero in gen:
    #     for song in song_dict:
    #         if song["playlist_genre"] == genero:
    #             ac_gen[genero] = ac_gen[genero]+1
    #             cont_gen[genero] = cont_gen[genero] + float(song["energy"])

    # print(ac_gen)
    # print(cont_gen)
    # get the average enery for each genre
    song_avrg_energy = { genero:cont_gen[genero]/ac_gen[genero] for genero in gen }
    return song_avrg_energy    

# popularidad promedio por artista
def get_popularity_artist(song_dict):
    artists=set() # delete duplicates
    for song in song_dict:
        artists.add(song["track_artist"])
    cont_popul = {artist:0 for artist in artists} # count repeated artists
    ac_popul = {artist:0 for artist in artists} # accumulate popularities

    for song in song_dict:
        artist = song["track_artist"]
        ac_popul[artist] = ac_popul[artist] + 1
        cont_popul[artist] = cont_popul[artist] + float(song["track_popularity"]) 

    # average for each artist
    avrg_popularity = {artist:cont_popul[artist]/ac_popul[artist] for artist in artists}

    # get the 5 artist with the greatest average popularity
    used = []
    avrg_popularity_2 = {}
    for i in range(0,6):
        mayor = 0
        art = ""
        for artist in avrg_popularity:
            if not artist in used and avrg_popularity[artist] > mayor:
                mayor = avrg_popularity[artist]
                art = artist
        used.append(art)
        avrg_popularity_2[art] = mayor
    return avrg_popularity_2

def get_album_artist(song_dict):
    artists = set() # avoid duplicates
    for song in song_dict:
        artists.add(song["track_artist"])
    album_artist = {artist:set() for artist in artists}
    # get albums
    for song in song_dict:  
        artist = song["track_artist"]
        album_artist[artist].add(song["track_album_name"])
    return album_artist

def get_most_listened_artist(song_dict, n_most_listened):
    artists = set()
    for song in song_dict:
        artists.add(song["track_artist"])

    most_listened_artist = {artist:0 for artist in artists}
    for song in song_dict:
        artist = song["track_artist"]
        most_listened_artist[artist] = most_listened_artist[artist] + 1

    used = []
    n_most_listened_artist = {}
    ac = 0
    for i in range(0,n_most_listened):
        mayor=0
        art=""
        for artist in most_listened_artist:
            if not artist in used and most_listened_artist[artist] > mayor:
                mayor = most_listened_artist[artist]
                art = artist
        used.append(art)
        n_most_listened_artist[art] = mayor
        ac = ac + mayor

    for artist in n_most_listened_artist:
        n_most_listened_artist[artist] = 100*n_most_listened_artist[artist]/ac

    return n_most_listened_artist, ac
