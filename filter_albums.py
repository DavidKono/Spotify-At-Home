import re

keywords = [
    'greatest hits', 'best of', 'anthology', 'collection', 'essential', 'definitive',
    'retrospective', 'chronicles', 'gold', 'platinum', 'box set', 'singles', 'classics',
    'live', 'in concert', 'complete', 'tour', 'unplugged', 'sessions', 'concert', 'encore',
    'deluxe', 'extended', 'special', 'edition', 'remastered', 'reissue', 'expanded',
    'bonus', 'disc', 'remix'
]

#take in list of album names and ensures that basic things like greatest hits are excluded
def checkAlbumHasKeyword(title):
    title_lower = title.lower()
    return any(re.search(rf'\b{kw}\b', title_lower) for kw in keywords)

# assume remasters/anniversaries same as originals 
# user can replace with their preferred version
# no simple way to "always" get the original, so just install whichever first
def checkAlbumIsOriginal(artist_album):
    



#yt music sometimes only has remasters of albums, to to avoid not downloading the only copy, we also compare albums names to see if albums might might be longer named versions of other albums ie unoriginal remasters
# def checkAlbumIsNotInDir():

# also just make sure album does not already exist in collection??



# in albums remove if has keyword
# check that album is not a longer version of another album
# check we dont have album already downloaded



# append existing albums to list