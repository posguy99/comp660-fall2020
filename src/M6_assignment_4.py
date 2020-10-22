
# M6 #4

def add_html_tags(tag, words):
    '''
    Given a tag and words to enclose within the tag
    return the result string
    tag == the tag to enclose with
    words == the words to enclose
    '''
    return '<' + tag + '>' + words + '</' + tag + '>'


print(add_html_tags('p', 'This is my first page.'))
print(add_html_tags('h2', 'A secondary header.'))
print(add_html_tags('p', 'Some more text.'))
