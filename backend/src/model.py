from transformers import AutoModelWithLMHead, AutoTokenizer, pipeline

 
class TransformerTranslator(object):
    def __init__(self,  max_length=5000, model=None, tokenizer=None,):
        self.max_length = max_length
        self.model = AutoModelWithLMHead.from_pretrained("Helsinki-NLP/opus-mt-en-et")
        self.tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-et")
        self.pipe = pipeline("translation_en_to_et", model=self.model, tokenizer=self.tokenizer)

    def translate(self, input): 
        translated_text = self.pipe(input, max_length=self.max_length)[0]['translation_text']
        return translated_text





