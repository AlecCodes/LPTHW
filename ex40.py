class Song(object):
	
	def __init__(self, lyrics):
		self.lyrics = lyrics
	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)

happy_bday = Song(["Happy birthday to you","I dont wanna get sued","So I'll stop right there"])



bulls_on_parade = Song(["They rally around tha family","With pockets full of shells"])

da_beat = ["Gimmie da beat boys and free my soul","I wanna get lost in the rock n roll", "And drift away..."]

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

dabeat = Song(da_beat)
dabeat.sing_me_a_song()
