def make_album(artist_name, album_title, number_of_tracks=''):
    if not number_of_tracks:
        album = {'Artist': artist_name, 'Album': album_title}
        return album
    elif number_of_tracks:
        album = {'Artist': artist_name, 'Album': album_title, 'Tracks': str(number_of_tracks)}
        return album


first = make_album('Rush', 'Counterparts')
second = make_album('Yes', 'Fragile')
third = make_album('King Crimson', 'Discipline')
fourth = make_album('Genesis', 'The lamb lies down on Broadway', '23')

print(first, second, third, fourth)
