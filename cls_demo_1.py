def make_oneline(string):
    return string.replace('\n ', ' ').replace('\n', ' ').strip()

demo = """
But I must explain to you how all this mistaken idea of denouncing pleasure 
and praising pain was born and I will give you a complete account of the 
system, and expound the actual teachings of the great explorer of the truth, 
the master-builder of human happiness. No one rejects, dislikes, or avoids 
pleasure itself, because it is pleasure, but because those who do not know 
how to pursue pleasure rationally encounter consequences that are extremely 
painful. Nor again is there anyone who loves or pursues or desires to obtain 
pain of itself, because it is pain, but because occasionally circumstances 
occur in which toil and pain can procure him some great pleasure. To take a 
trivial example, which of us ever undertakes laborious physical exercise, 
except to obtain some advantage from it? But who has any right to find fault 
with a man who chooses to enjoy a pleasure that has no annoying 
consequences, or one who avoids a pain that produces no resultant pleasure?
"""

def symbols_count(txt):
    """Build mapping counting number of entries of each symbol."""
    syms = set(txt)
    res = dict()
    for sym in sorted(syms):
        res[sym] = txt.count(sym)
    return res
    # or
    # return {sym: txt.count(sym) for sym in sorted(set(txt))}

class Text:
    def __init__(self, obj=''):
        self.str = str(obj)
        self.oneline = make_oneline(self.str)

    def __repr__(self):
        lim = self.oneline[:16]
        ext = '...' if len(self.oneline) > 16 else ''
        return f'{type(self).__name__}({repr(lim)}{ext})'

    def __str__(self):
        return self.str

    def symbols_count(self):
        """Build mapping counting number of entries of each symbol."""
        return {sym: self.oneline.count(sym)
                for sym in sorted(set(self.oneline))}


def get_word_count(txt):
    """Count the number of words in the text."""
    words = txt.split()
    return len(words)

def get_unique_words(txt):
    """Get a set of unique words in the text."""
    words = txt.split()
    return set(words)


text_obj = Text(demo)
print(f"Original text:\n{text_obj}\n")
print(f"One-lined text:\n{text_obj.oneline}\n")


print(f"Word count: {get_word_count(text_obj.oneline)}\n")

unique_words = get_unique_words(text_obj.oneline)
print(f"Number of unique words: {len(unique_words)}")
print(f"Unique words: {', '.join(unique_words)}\n")


symbol_counts = text_obj.symbols_count()
print("Symbol counts:")
for sym, count in symbol_counts.items():
    print(f"{sym}: {count}")
