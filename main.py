import readfile
import utils
import charts

def run():
    data = readfile.read_data("./spotify_songs.csv")
    # print(type(data))
    # energy average for each artist
    song_avrg_energy = utils.get_gen_average_energy(data)
    print("Promedio de energia según el género:")
    for genero in song_avrg_energy:
        print(genero, round(song_avrg_energy[genero], 2), sep=": ")
    values = [round(value,2) for value in song_avrg_energy.values()]
    charts.generate_bar_chart(song_avrg_energy.keys(), values)

    # 5 artists with greatest popularity
    avrg_popularity = utils.get_popularity_artist(data)
    print("\n5 artistas con mayor popularidad:")
    for artist in avrg_popularity:
        print(artist, round(avrg_popularity[artist], 2), sep=": ")
    values = [round(value,2) for value in avrg_popularity.values()]
    charts.generate_bar_chart(avrg_popularity.keys(), values)

    # albums for each artist
    album_artist = utils.get_album_artist(data)
    artist = input("\nIngrese el nombre del artista para mostrar sus albunes: ")    
    try:
        albums = [album for album in album_artist[artist]]
        print(f"\nListando albunes de {artist}:")
        for album in albums:
            print(album)
    except KeyError:
        print("Valor incorrecto")

    # most listened artists
    n = 5
    most_listened_artist, total = utils.get_most_listened_artist(data, n)
    # print(most_listened_artist, total)
    print(f"\nTotal de canciones para los {n} artistas mas escuchados: {total}")
    for artist in most_listened_artist:
        print(f"{artist}: {round(most_listened_artist[artist], 2)}%")
        #print(artist, round(most_listened_artist[artist], 2), sep=": ")
    charts.generate_pie_chart(most_listened_artist.keys(), most_listened_artist.values())

if __name__ == "__main__":
    run()