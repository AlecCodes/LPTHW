import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
	line = language_file.readline()
	
	if line:
		print_line(line, encoding, errors)
		return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
	next_lang = line.strip()
	raw_bytes = next_lang.encode(encoding, errors=errors)
	cooked_string = raw_bytes.decode(encoding, errors=errors)
	
	print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)


#decode() converts raw bytes into unicode string
#encode() does the opposite
#What is encode(), strict, and error mean?
print('😊️音作為輸入方式。漢語拼音簡稱拼音是根據普通話/國語的發音，用英文子母作聲母和韻母組合而成。')
