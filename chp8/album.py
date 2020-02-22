# Write a function called make_album() that builds a dictionary describing a music album.
# The function should take in an artist name and an album title,
# and it shold return a dictionary containing these two pieces of information.

# Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album.
def make_album(artist_name, album_title, num_songs = None):
	"""Return a dictionary of artist name and album"""
	artist_and_album = {
		'artist': artist_name,
		'album': album_title
		}
	if num_songs:
		artist_and_album['num_songs'] = num_songs
	return artist_and_album

# Use the function to make three dictionaries representing different albums.
# Print each retrn value to show that the dictionaries are storing the album information correctly

best_albums = make_album('smashing pumpkins', 'siamese dream')
print(best_albums)

best_albums = make_album('soundgarden', 'superunknown')
print(best_albums)

best_albums = make_album('pearl jam', 'ten')
print(best_albums)

best_albums = make_album('stone temple pilots', 'purple', '13')
print(best_albums)


# If the calling line includes a value for the number of songs, add that value to the album's directory.
# Make at least one new funtion call that includes the number of songs on an album.