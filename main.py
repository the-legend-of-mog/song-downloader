from ytmusicapi import YTMusic 
from r import check 
import os 
import spotipy, music_tag, requests 
from spotipy.oauth2 import SpotifyClientCredentials 
ytmusic = YTMusic() 
def c(n):
  return len(n['name']) 
def t(n):
  return n['total_tracks'] 
def tn(n): 
  return n.title 
def metadataify(f, album, trackno, artists, title, name, th): 
  print(title) 
  f['album'] = album 
  f['tracknumber'] = trackno 
  try: 
    del f['artist'] 
  except: 
    pass 
  for p in artists: 
    f.append('artist', p['name']) 
    print(p['name']) 
  with open('t.png', 'rb') as img_in: 
    f['artwork'] = img_in.read() 
    f.save()
  if not os.path.exists(f'{th.title()}/' + f'{album}'):
    os.mkdir(f'{th.title()}/' + f'{f["album"]}') 
    os.rename(f'{name}', f"{th}/{album}/{title}.mp3") spotify =
  spotipy.Spotify( client_credentials_manager=SpotifyClientCredentials()) 
  #ar is the list of artist to download the score is just there as a placeholder                                                         
  ar = ['the score'] 
  for th in ar: 
    a = ytmusic.search(f'{th}', filter='songs', limit=100000) 
    print(f"parsing {len(a)} songs") 
    try: 
      qq = ytmusic.search(f'{th}', filter='songs', limit=1) 
      xxqqz = a[0]['artists'][0]['id'] b = ytmusic.get_artist(xxqqz) 
      r = b['albums']['results'] 
      for i in r: 
        x = ytmusic.get_album(i['browseId']) 
        a.extend(x['tracks']) 
      try: 
        rr = b['singles']['results'] 
        q = [] 
        for z in rr:
          a.append(ytmusic.get_album(z['browseId'])) 
      except: 
        pass 
    except: 
      pass 
    dl = check(a, th) 
    dl.sort(key=tn) 
    for i in dl: 
      i.sorts() 
    print(f'found {len(dl)} songs by {th}') 
      a = 1 
      if not os.path.exists(th.title()): 
        os.mkdir(th.title()) 
    for i in dl: 
      q = i.download() 
      print(q, f'{a}/{len(dl)}')
      a += 1 
      sus = ['acoustic', 'version', 'remix', ' mix ', 'restrung', 'mix)'] 
      results = spotify.search(f'{th}', limit=1, offset=0, type='artist') 
      z = results['artists']['items'][0]['uri'] 
      x = spotify.artist_albums(z, album_type='single,album', limit=50) x['items'].sort(key=c, reverse=True) 
      albums_n = '' 
      albums = [] 
      for i in x['items']: 
        if 'live' not in i['name'].lower() and 'tour' not in i['name'].lower(): 
          if i['name'] not in albums_n: 
            albums.append(i) 
            albums_n += f' {i["name"].replace("&","")} ' 
            albums.sort(key=t, reverse=True) 
      for i in albums: 
        x = spotify.album_tracks(i['uri']) 
        print(f"compiling {i['name']}") print('\n') 
        re = requests.get(i['images'][0]['url'], stream=False) 
        fp = open('t.png', 'wb') 
        fp.write(re.content) 
        fp.close()
        print('\n\n') 
      for z in x['items']:
        try: 
          name = f'{th.title()}/' + f'{z["name"]}.mp3'.replace( '\\', '-').casefold().capitalize().replace('with', 'feat.') 
          f = music_tag.load_file(name) album = i['name'].replace('/', '|') if 'instrumental' in z['name'].lower(): 
          album = 'Instrumentals' 
          for u in sus: if u in z['name'].lower(): 
            album = 'Remixes' 
            trackno = z['track_number'] 
            artists = z['artists'] 
            title = z['name'].replace('/', '|') 
            metadataify(f, album, trackno, artists, title, name, th.title()) 
        except Exception as e: 
          print(e) 
        for i in os.listdir(th.title()): 
          if '.mp3' in i: 
            if not os.path.exists(f'{th.title()}/Singles'): 
              os.mkdir(f'{th.title()}/Singles') 
              os.rename(f'{th.title()}/{i}',f'{th.title()}/Singles/{i}') 
          sus = ['acoustic', 'version', 'remix', ' mix ', 'restrung', 'mix)'] 
          for i in os.scandir(th.title()): 
            try: a = i.name 
              print(a, len(os.listdir(f"{th.title()}/{a}"))) 
              for ii in os.listdir(i): 
                if len(os.listdir(f"{th.title()}/{a}")) == 1: 
                  f = music_tag.load_file(f"{th.title()}/{str(a)}/{ii}") 
                  album = 'Singles' 
                  for jj in sus: if jj in ii: 
                    album = 'Remixes' 
                  f['album'] = album 
                  f.save() 
                  if not os.path.exists(f'{th.title()}/{album}'): 
                    os.mkdir(f'{th.title()}/{album}') 
                    os.rename(f"{th.title()}/{str(a)}/{ii}", f"{th.title()}/{album}/{ii}.mp3") 
                    if len(os.listdir(f"{th.title()}/{a}")) == 0: 
                      os.rmdir(f"{th.title()}/{a}") 
            except Exception as a: 
              print(a) 
            try: 
              for i in os.listdir (f'{th.title()}/Singles'): 
                try: name = f'{th.title()}/Singles/{i}' 
                  f = music_tag.load_file(name) 
                  results = spotify.search(f'{th.title()} {i}',limit=1,offset=0,type='track')
                  res = spotify.track(results['tracks']['items'][0]['uri']) 
                  re=requests.get(res['album']['images'][0]['url'],stream=False) 
                  fp = open('t.png', 'wb' ) 
                  fp.write(re.content) 
                  fp.close() 
                  album = 'Singles' 
                  trackno = res['track_number'] 
                  artists = res['artists'] 
                  title = res['name'] 
                  metadataify(f,album,trackno,artists,title,name,th.title()) 
              except Exception as e: 
                print(e) 
            except: 
              pass
