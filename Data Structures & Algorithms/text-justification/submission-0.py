class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        cur = 0
        output = []

        while cur < len(words):

            # Each line must contain 1 word, so add cur word
            cur_line_words = [words[cur]]
            chars = len(words[cur])
            init_spaces = 1

            # Then try and add more words to this line
            while True:
                remaining = maxWidth - chars - init_spaces
                if cur + 1 < len(words) and len(words[cur + 1]) <= remaining:
                    cur += 1
                    cur_line_words.append(words[cur])
                    chars += len(words[cur])
                    init_spaces += 1
                else:
                    break
            
            cur += 1

            if len(cur_line_words) == 1:
                cur_line = cur_line_words[0] + " " * (maxWidth - chars)

            elif cur == len(words):
                joined_chars = " ".join(cur_line_words)
                cur_line = joined_chars + " " * (maxWidth - len(joined_chars))

            else:
                gaps = init_spaces - 1
                min_gap_space = (maxWidth - chars) // gaps
                spaces_to_distribute = (maxWidth - chars) % gaps

                gap_sizes = [min_gap_space] * gaps
                for i in range(spaces_to_distribute):
                    gap_sizes[i] += 1
                
                cur_line = ""
                for i in range(len(gap_sizes)):
                    cur_line += cur_line_words[i] + " " * gap_sizes[i]
                cur_line += cur_line_words[-1]
                
            output.append(cur_line)
        
        return output