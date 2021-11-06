languages = {
    'C++' : 'The C++ language has an object oriented structure which is used in large projects.',
    'Java' : 'The Java language is a multi platform language that’s particularly helpful in networking.',
    'Go' : 'A statically typed, compiled programming language designed at Google.',
    'Python' : "Python is an interpreted high-level general-purpose programming language.",
    'HTML' : 'The HyperText Markup Language, or HTML is the standard markup language for documents designed to be displayed in a web browser.'
}
lang_order = ['Go', 'Java', 'Python', 'C++', 'HTML'] #making a list for the desired order when printing (3-2-4-1-5)
dict_order = {key: languages[key] for key in lang_order} #declaring the list containing the order as a dictionary

for key in dict_order:
    print(key) #prints the key only withput the value
    print(dict_order[key]) #prints the values inside he responding key
    print() #prints an extra space after the last key's values are printed
