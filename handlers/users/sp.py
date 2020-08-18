from datetime import datetime

import tekore as tk

conf = tk.config_from_environment(return_refresh=True)
token = tk.refresh_user_token(*conf[:2], conf[3])
sp = tk.Spotify(token, max_limits_on=True, chunked_on=True)


def list_playlists():
    listl = list()
    for artist in sp.followed_playlists().items:
        listl.append(artist.id)
    return listl


def list_artists():
    list_artists = list()
    for artist in sp.all_items(sp.followed_artists()):
        list_artists.append(artist.id)

    return list_artists


def list_tracks_uri(playlist):
    return [item.track.uri for item in sp.all_items(sp.playlist_items(playlist))]


def list_tracks_id(playlist):
    return [item.track.id for item in sp.all_items(sp.playlist_items(playlist))]


def add_tracks(uri, uri2):
    track_list = list_tracks_uri(uri)
    track_list.reverse()
    sp.playlist_add(uri2, track_list)
    return 'Успешно добавлены треки'


def delete_tracks(id_1, id_2):
    track_list = list_tracks_uri(id_1)
    sp.playlist_remove(id_2, track_list)
    return 'Успешно удалены треки'


def favorite_tracks():
    return [item.track.id for item in sp.all_items(sp.saved_tracks())]


def add_to_favorite_tracks(uri):
    list_songs = list_tracks_id(uri)
    list_songs.reverse()
    sp.saved_tracks_add(list_songs)
    return 'Всё добавлено'


def delete_favorite_tracks():
    list_songs = favorite_tracks()
    sp.saved_tracks_delete(list_songs)
    return 'Всё удалено'

def add_new_release(ids_artists):
    songs = list()
    check_playlist = list()
    now = (datetime.today().strftime("%Y-%m-%d"))
    # now = '2020-08-07'
    # Для каждого айди исполнителя из списка исполнителей
    for artist in ids_artists:
        # Находим все альбомы исполнителя
        albums = sp.artist_albums(artist)
        for album in albums.items:
            if str(album.album_group) != 'appears_on' and album.release_date == now:
                us = sp.album_tracks(album.uri[14:])
                for i in us.items:
                    songs.append(i.uri)

    for artist in sp.followed_playlists().items:
        check_playlist.append(artist.name)
    if songs and not (check_playlist.count(now)):
        id_album = sp.playlist_create('om8u6cmy29znuq8xq9n0snlei', now, True).id
        sp.playlist_add(id_album, songs)
        return (f'Добавлено {len(songs)} новых треков')
    else:
        return ('Нет новых треков')