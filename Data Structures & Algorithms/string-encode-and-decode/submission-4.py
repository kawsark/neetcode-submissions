class Solution:

    word_sep = chr(0)
    chr_sep = chr(1)

    def encode(self, strs: List[str]) -> str:
        # Empty array
        if len(strs) == 0:
            return "[]"

        enc = ""
        
        for i in range(len(strs)):
            s = strs[i]
            ch = list(s)
            if len(ch) == 0:
                enc += ""
            else:
                for j in range(len(ch)):
                    c = ch[j]
                    enc += str(ord(c))
                    if (j+1) < len(ch):
                        enc += self.chr_sep

            if (i+1) < len(strs):
                enc += self.word_sep
        
        print(f"Sent ->{enc}<- len: {str(len(enc))}")

        return enc


    def decode(self, s: str) -> List[str]:
        print(f"Received ->{s}<- len: {str(len(s))}")

        res = []
        if s == "[]":
            return res

        else:
            sp = s.split(self.word_sep)
            for d in sp:
                r = ""
                dec = d.split(self.chr_sep)
                for c in dec:
                    if len(c) > 0:
                        print(f"{c}:{chr(int(c))}")
                        r += chr(int(c))
                    else:
                        r += ""

                res.append(r)
        
        return res
            

