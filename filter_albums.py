import re

keywords = [
    'greatest hits', 'best of', 'anthology', 'collection', 'essential', 'definitive',
    'retrospective', 'chronicles', 'gold', 'platinum', 'box set', 'singles', 'classics',
    'live', 'in concert', 'complete', 'tour', 'unplugged', 'sessions', 'concert', 'encore',
    'deluxe', 'extended', 'special', 'edition', 'remastered', 'reissue', 'expanded',
    'bonus', 'disc', 'anniversary', 'remix'
]

#take in list of album names and ensures that basic things like greatest hits are excluded
def checkAlbumDuplicate(title):
    title_lower = title.lower()
    return any(re.search(rf'\b{kw}\b', title_lower) for kw in keywords)

#yt music sometimes only has remasters of albums, to to avoid not downloading the only copy, we also compare albums names to see if albums might might be longer named versions of other albums ie unoriginal remasters
def filterAlbums():

# also just make sure album does not already exist in collection??