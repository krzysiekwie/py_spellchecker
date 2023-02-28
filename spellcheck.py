from enchant.checker import SpellChecker
en_chkr = SpellChecker("en_US")
pl_chkr = SpellChecker("pl_PL")

def check_spelling(lang, text_to_check):
    errors = []
    for line in text_to_check:
        lang.set_text(line)
        for err in lang:
            errors.append(err.word)

    errors = list(set(errors))
    errors.sort()
    for err in errors:
        print(f"ERROR: {err}")


with open("./sample_sources.txt", encoding="utf-8") as f:
    source_text = f.readlines()
with open("./sample_targets.txt", encoding="utf-8") as f:
    target_text = f.readlines()

# check_spelling(en_chkr, source_text)
check_spelling(pl_chkr, target_text)


