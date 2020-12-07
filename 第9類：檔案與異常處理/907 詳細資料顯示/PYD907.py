f_name = input()
fp = open(f_name, "r+")

line_count = word_count = char_count = 0

for line in fp:
    line_count += 1
    sp_line = line.split(' ')
    word_count += len(sp_line)
    for i in sp_line:
        char_count += len(i)
fp.close()

print(line_count,' line(s)')
print(word_count,'word(s)')
print(char_count,'char(s)')
"""
_ line(s)
_ word(s)
_ character(s)     
"""