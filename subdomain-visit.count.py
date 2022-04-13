class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        lookup = dict()
        for pair in cpdomains:
          count, full = pair.split(" ")
          splitted = full.split('.')
          for i in range(len(splitted)): # 2 or 3
            subdomain = '.'.join(splitted[i:])
            if subdomain not in lookup: 
              lookup[subdomain] = 0
            lookup[subdomain] += int(count)
        print(lookup)
        array = []
        for pair in lookup:
            string_builder = str(lookup[pair]) + " " + pair
            array += [string_builder]

        return array
        
