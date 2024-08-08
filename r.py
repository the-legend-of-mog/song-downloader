import re 
from ytmusicapi import YTMusic 
from pydub import AudioSegment
import os, music_tag 
from pytube import YouTube 
ytmusic = YTMusic() 

def custfunct(n): 
  try: 
    yt = YouTube(f'https://www.youtube.com/watch?v={id}') 
    return yt.length 
  except:
    return 999999999999 
class song: 
  def __init__(self, title, links, artists): 
    self.title = title 
    self.links = links 
    self.artists = artists 
    def sorts(self): 
      self.links.sort(key=custfunct, reverse=True) 
    def download(self): 
      try: 
        title = f'{self.title.casefold().capitalize()}.mp3' 
        if f'{self.title.casefold().capitalize()}.mp3' not in os.listdir(self.artists.title()):
          id = self.links[0] self.title.replace('\\', '-') 
          yt = YouTube(f'https://www.youtube.com/watch?v={id}') 
          at = yt.streams.filter(file_extension='mp4').filter(only_audio=True) 
          if yt.length < 2030: 
            at = [i for i in at] 
            at = at.pop() 
            stream = yt.streams.get_by_itag(at.itag) 
            stream.download(filename='temp.mp4') 
            m = AudioSegment.from_file("temp.mp4", "mp4")
            m.export(f"{title}", format="mp3") 
            f = music_tag.load_file(f"{title}")
            f['album_artist'] = f"{self.artists}"
            f['title'] = title.replace('.mp3', '') 
            f.save() 
            os.rename(f'{title}', f'{self.artists.title()}/{title}')
            os.remove('temp.mp4') 
            return f'downloaded {title} by {self.artists}'
        else: 
          return f'already downloaded {title} by {self.artists}' 
      except Exception as e: 
        print(e) 
        print('failed') 
        try: 
          os.remove('temp.mp4') 
        except: 
            pass 
    def __str__(self): 
      return f"({self.title} \n {self.artists})" 
    def check(a, th):
        dl = []
        for i in a:
          try: t = i['artists'][0]['name']
            if th.lower() == t.lower() and 'remix' not in i['title'].lower() and 'mix)' not in i['title'].lower(): 
              if i['title'].count('(') > 0: b = i['title'].rpartition('(') 
                if len( re.findall('[\|[\)\s|\|\|\(|\\{\[]([Ll][Ii][Vv][eE]|[Cc][Oo][Mm][Mm][Ee][Nn][Tt][Aa][Rr][Yy])[\s|\)|\}|\]\\\/\)\(]',f'({b[2]})')) > 0:
                  pass 
              else: 
                a = next((obj for obj in dl if obj.title == i['title']), None) 
                if a == None: 
                  try: 
                    a = song(i['title'], [i['videoId']], th.title()) dl.append(a) 
                  except: a = song(i['title'], [i['tracks'][0]['videoId']],th.title()) dl.append(a) else: try: a.links.append(i['videoId']) except: a.links.append(i['tracks'][0]['videoId'])
                else: 
                  a = next((obj for obj in dl if obj.title == i['title']), None) 
                if a == None: 
                  try: 
                    a = song(i['title'], [i['videoId']], th.title()) dl.append(a) 
                  except: a = song(i['title'], [i['tracks'][0]['videoId']],th.title()) dl.append(a)
                else:
                  try: 
                    a.links.append(i['videoId']) 
                  except: 
                    a.links.append(i['tracks'][0]['videoId']) 
              except: 
                pass 
    return dl
