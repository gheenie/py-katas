def sentence_to_camel_case(sentence, should_capitalise):
    if sentence == '':
        return ''
    
    words = sentence.split(' ')

    camel_cased_words = list( map(lambda word: word.lower().capitalize(), words) )

    camel_cased_sentence = ''.join(camel_cased_words)

    if not should_capitalise:
        camel_cased_sentence = camel_cased_sentence[0].lower() + camel_cased_sentence[1:]
    
    return camel_cased_sentence
