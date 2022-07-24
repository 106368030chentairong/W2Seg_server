from ckip_transformers.nlp import CkipWordSegmenter, CkipPosTagger, CkipNerChunker

class w2seq():
    def __init__(self):
        self.ws_driver = None
        self.pos_driver = None
        self.ner_driver = None
        self.tmp = None
    def setup(self):
        # Initialize drivers
        self.ws_driver  = CkipWordSegmenter(model="albert-base")
        self.pos_driver = CkipPosTagger(model="albert-base")
        #self.ner_driver = CkipNerChunker(model="albert-base")
        # Use GPU:0
        #ws_driver = CkipWordSegmenter(device=0)
    def filter_word(self, ws, pos):
        self.tmp = []
        ner_in = ["COMMACATEGORY" , "Nd","Ng","SHI","VH","DE", "P" ,"PARENTHESISCATEGORY", "PERIODCATEGORY", "Dfa", "D", "WHITESPACE"]
        for index, pos in enumerate(pos[0]):
            if pos not in ner_in:
                self.tmp.append(ws[0][index])

    def run(self, word):
        # Run pipeline
        ws  = self.ws_driver(word)
        pos = self.pos_driver(ws)
        self.filter_word(ws, pos) 
        #ner = self.ner_driver(word)
        return self.tmp
