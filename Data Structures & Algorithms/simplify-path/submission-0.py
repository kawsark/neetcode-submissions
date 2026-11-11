# Meta: '{"felt":"medium", "time": 25, "help": "none" }'
class Solution:
    def simplifyPath(self, path: str) -> str:
        path_st = ['']
        parts = path.split("/")

        for part in parts:
            if part == "..": 
                if len(path_st) > 1:
                    path_st.pop()
                else:
                    pass
            elif part == "." or len(part) == 0:
                pass
            else:
                path_st.append(part)

        if len(path_st) == 1:
            path_st.append('')
        
        return "/".join(path_st)

        