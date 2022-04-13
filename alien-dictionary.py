class Solution:
    def isAlienSorted(self, words, order): #List[str], order: str) -> bool:
        # words
        # order

        if len(words) == 1:
          return True
        aliens = {}
        for i in range(len(order)):
          aliens[order[i]] = i

        # aliens maps
        # aliens[h] = 0
        # aliens[l] = 1
        # same as words.index(h) = 0
        # words.index(l) = 1

        for i in range(1, len(words)):
          curr = words[i]
          prev = words[i-1]
          for letter in range(max(len(curr), len(prev))):
              if aliens[prev[letter]] < aliens[curr[letter]]:
                  break
              elif aliens[prev[letter]] > aliens[curr[letter]]:
                  return False
              elif aliens[prev[letter]] == aliens[curr[letter]]:
                # Edge Case: the word is shorter than the one after it
                  if prev[letter+1:] and not curr[letter+1:]:
                      return False
                # Edge Case: the word is longer than the one after it.
                  elif curr[letter+1:] and not prev[letter+1:]:
                      break
                # Edge case: both words are the same. This is OK.
                  elif not curr[letter+1:] and not prev[letter+1:]:
                      break
                  continue
        return True

              
