##############
#            #
#    VEBY    #
#   JARVIS   #
#            #
##############



import queue
import vosk
import json
import worlds

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from skills import *



q = queue.Queue()

model = vosk.Model(r"F:\jarvis\ModelVosk")

device = sd.default.device
samplerate = int(sd.query_devices(device[0], "input")["default_samplerate"])


def callback(indata, frames, time, status):
    q.put(bytes(indata))


def recognize(data, vectorizer, clf):
    trg = worlds.TRIGGER_BOT.intersection(data.split())
    if not trg:
        return

    data.replace(list(trg)[0], "")
    text_vector = vectorizer.transform([data]).toarray()[0]
    answer = clf.predict([text_vector])[0]

    func_name = answer.split()[0]
    if func_name == "setValumeZvyk":
        speaker()
        setValumeZvyk(data)
    else:
        speaker()
        exec(func_name + "()")

def main():
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(list(worlds.data_set.keys()))

    clf = LogisticRegression()
    clf.fit(vectors, list(worlds.data_set.values()))

    del worlds.data_set

    with sd.RawInputStream(samplerate=samplerate, blocksize = 8000, device=device,
                            dtype="int16", channels=1, callback=callback):
        
        
        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                data = json.loads(rec.Result())["text"]
                # print(data)
                recognize(data, vectorizer, clf)


if __name__ == "__main__":
    main()