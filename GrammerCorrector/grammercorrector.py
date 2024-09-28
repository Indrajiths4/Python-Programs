import spacy
import language_tool_python
nlp = spacy.load("en_core_web_sm")
tool = language_tool_python.LanguageTool('en-US')
def correct_sentence(sentence):
    matches = tool.check(sentence)
    corrected_sentence = tool.correct(sentence)
    return corrected_sentence, matches
input_sentence = "I is going to india."
corrected_sentence, errors = correct_sentence(input_sentence)
print(f"Original Sentence: {input_sentence}")
print(f"Corrected Sentence: {corrected_sentence}")
print(f"Errors Found: {len(errors)}")
for error in errors:
    print(f"- {error}")
