from ckip_transformers.nlp import CkipWordSegmenter, CkipPosTagger, CkipNerChunker

class w2seq():
    def __init__(self):
        self.ws_driver = None
        self.pos_driver = None
        self.ner_driver = None

    def setup(self):
        # Initialize drivers
        self.ws_driver  = CkipWordSegmenter(model="bert-base")
        #self.pos_driver = CkipPosTagger(model="bert-base")
        #self.ner_driver = CkipNerChunker(model="bert-base")
        # Use GPU:0
        #ws_driver = CkipWordSegmenter(device=0)
    def run(self, word):
        # Run pipeline
        ws  = self.ws_driver(word)
        #pos = self.ws_driver(ws)
        #ner = self.ws_driver(word)
        return ws
