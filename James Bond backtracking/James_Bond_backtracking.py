import requests
import json
class word_ditection:
    def getting_dict_word(self,):
        self.req=requests.get("https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json")
        self.words_dic= self.req.json()
        self.words_list=list(self.words_dic.keys())
    def checking_dict_word(self,word):
        if word in self.words_list:
            return True
        else:
            return False
    def back_tracking_word_split(self,sc,comoleted_sc):
        len_sc=len(sc)
        for i in range(1, len_sc + 1):
            sub_sc = sc[:i]
            if self.checking_dict_word(sub_sc):
                if i == len_sc:
                    comoleted_sc=comoleted_sc+ sub_sc
                    print(comoleted_sc)
                self.back_tracking_word_split(sc[i:],comoleted_sc+sub_sc+" ")


if __name__ == "__main__":
    sentence_code=input()
    sentence_code=sentence_code.lower()
    w=word_ditection()
    w.getting_dict_word()
    w.back_tracking_word_split(sentence_code,"")
