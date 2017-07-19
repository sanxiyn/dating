import unicodedata

import regex

cyrillic = regex.compile(r'\p{Cyrillic}+$', regex.UNICODE)

def clean(text):
    text = text.replace(u'\N{NO-BREAK SPACE}', ' ')
    text = text.replace(u'\N{LEFT SINGLE QUOTATION MARK}', "'")
    return text

def transliterate(text):
    if cyrillic.match(text): return text.translate(cyrillic_table)
    return text

def make_table(table):
    result = {}
    for name in table:
        character = unicodedata.lookup(name)
        result[ord(character)] = unicode(table[name])
    return result

# ISO 9
cyrillic_table = make_table({
    'CYRILLIC CAPITAL LETTER A': 'A',
    'CYRILLIC CAPITAL LETTER VE': 'V',
    'CYRILLIC CAPITAL LETTER DE': 'D',
    'CYRILLIC CAPITAL LETTER IE': 'E',
    'CYRILLIC CAPITAL LETTER I': 'I',
    'CYRILLIC CAPITAL LETTER KA': 'K',
    'CYRILLIC CAPITAL LETTER EL': 'L',
    'CYRILLIC CAPITAL LETTER EM': 'M',
    'CYRILLIC CAPITAL LETTER EN': 'N',
    'CYRILLIC CAPITAL LETTER O': 'O',
    'CYRILLIC CAPITAL LETTER PE': 'P',
    'CYRILLIC CAPITAL LETTER ER': 'R',
    'CYRILLIC CAPITAL LETTER ES': 'S',
    'CYRILLIC CAPITAL LETTER TE': 'T',
    'CYRILLIC SMALL LETTER A': 'a',
    'CYRILLIC SMALL LETTER VE': 'v',
    'CYRILLIC SMALL LETTER DE': 'd',
    'CYRILLIC SMALL LETTER IE': 'e',
    'CYRILLIC SMALL LETTER I': 'i',
    'CYRILLIC SMALL LETTER KA': 'k',
    'CYRILLIC SMALL LETTER EL': 'l',
    'CYRILLIC SMALL LETTER EM': 'm',
    'CYRILLIC SMALL LETTER EN': 'n',
    'CYRILLIC SMALL LETTER O': 'o',
    'CYRILLIC SMALL LETTER PE': 'p',
    'CYRILLIC SMALL LETTER ER': 'r',
    'CYRILLIC SMALL LETTER ES': 's',
    'CYRILLIC SMALL LETTER TE': 't',
})
