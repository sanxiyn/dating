def clean(text):
    text = text.replace(u'\N{NO-BREAK SPACE}', ' ')
    text = text.replace(u'\N{LEFT SINGLE QUOTATION MARK}', "'")
    return text
