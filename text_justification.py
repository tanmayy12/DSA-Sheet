class Solution:
    def fullJustify(self, words, maxWidth):
        res = []
        i = 0
        
        while i < len(words):
            line_length = 0
            line_words = []
            
            # Greedily pack words
            while i < len(words) and line_length + len(words[i]) + len(line_words) <= maxWidth:
                line_length += len(words[i])
                line_words.append(words[i])
                i += 1
            
            total_spaces = maxWidth - line_length
            
            # If last line OR single word → left justify
            if i == len(words) or len(line_words) == 1:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            
            else:
                gaps = len(line_words) - 1
                space_per_gap = total_spaces // gaps
                extra_spaces = total_spaces % gaps
                
                line = ""
                for j in range(gaps):
                    line += line_words[j]
                    # Extra spaces go to left first
                    spaces = space_per_gap + (1 if j < extra_spaces else 0)
                    line += " " * spaces
                
                line += line_words[-1]  # last word
            
            res.append(line)
        
        return res
