def make_album(artist_name, album_title, number_of_tracks=''):
    if not number_of_tracks:
        album = {'Artist': artist_name, 'Album': album_title}
        return album
    elif number_of_tracks:
        album = {'Artist': artist_name, 'Album': album_title, 'Tracks': str(number_of_tracks)}
        return album


album_collection = []
active = True

while active:
    artist_name = input("Enter artist's name: ")
    if artist_name == 'q':
        break
    album_name = input("Enter album's name: ")
    if album_name == 'q':
        break
    album = make_album(artist_name, album_name)
    album_collection.append(album)

print()

while album_collection:
    current_album = album_collection.pop()
    print("Artista: " + current_album['Artist'])
    print("Album: " + current_album['Album'])
    print()
    if current_album == []:
        break