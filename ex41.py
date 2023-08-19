import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
	"class %%%(%%%):": 
	 "Make a class named %%% that is-a %%%",
	"class %%%(object):\n\tdef __init__(self,***)":
	 "class %%% has-a __init__ that takes self and *** params.",
	"class %%%(object): \n\tdef ***(self,@@@)":
	 "class %%% has-a function *** that takes self and @@@ params.",
	"*** = %%%()":
	 "Set *** to an instance of class %%%",
	"***.***(@@@)":
	 "From *** get the *** function, call it with params self, @@@.",
	"***.*** = '***'":
	 "From *** get the *** attribute and set it to '***'.",	 	
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASE_FIRST = True
else:
	PHRASE_FIRST = False
	
# load up the words from the website
for word in urlopen(WORD_URL).readlines():
	WORDS.append(str(word.strip(), encoding="utf-8"))
	
#class_names is a list comprehension which returns a list of capitalized WORDS, the length of the list corresponds to the # of occurences of "%%%" in snippet. other_names does the same but for ***.
def convert(snippet, phrase):
	class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
	other_names = random.sample(WORDS, snippet.count("***"))
	results = []
	param_names = []

	#creates a param_names as string of random words for each occurence of '@@@' in a snippet
	for i in range(0, snippet.count("@@@")):
		param_count = random.randint(1,3)
		param_names.append(', '.join(random.sample(WORDS, param_count)))
		
		
	for sentence in snippet, phrase:
		#this is how you duplicate a list or string
		result = sentence[:]
		
		#fake class names, remember the number of elements in class_names corresponds to the number of occurneces of '%%%' in a snippet
		for word in class_names:
			result = result.replace("%%%", word, 1)
		
		#fake other words, remember the number of elements in other_names corresponds to the number of occurences of '***' in a snippet
		for word in other_names:
			result = result.replace("***", word, 1)
			
		#fake parameter lists, remember the number of elements in param_names corresponds to the # of occurences of "@@@" in a snippet
		for word in param_names:
			result = result.replace("@@@", word, 1) 
		
		results.append(result)
		
	return results 
	
	
# keep going until they hit CTRL-D
try:
	while True:
		snippets = list(PHRASES.keys())
		random.shuffle(snippets)
		#phrase is the answer!
		for snippet in snippets:
			phrase = PHRASES[snippet]
			question, answer = convert(snippet,phrase)	
			if PHRASE_FIRST:
				question, answer = answer, question
			
			print(question)
			
			input("> ")
			print(f"ANSWER: {answer}\n\n")
except EOFError:
	print("\nBYE")		
	
