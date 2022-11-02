"""
Clean the data  and get string 'a e i o u'
"""

data = "aNtEriOur\n\t>>"

new_data = data.lower()

garbage_word = 'aeiou'
output_string = ''
print(data)

for char in new_data:
    if (char in garbage_word):
        output_string += f'{char} '


print(f'Our Output is => {output_string}')
