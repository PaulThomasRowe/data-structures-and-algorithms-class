class Solution:
    def rNote(self, rNote: str, magazine: str) -> bool:
        availableCharacters = {}
        for i in range(0, len(magazine)):
            character = magazine[i]
            existingValue = availableCharacters[character]
            if existingValue == None:
                availableCharacters[character] = 0
            else:
                availableCharacters[character] = existingValue + 1
        for i in range(0, len(rNote)):
            character = rNote[i]
            existingValue = availableCharacters[character]
            if existingValue == None:
                return false
            elif existingValue <= 0:
                return false
            else:
                existingValue = existingValue - 1
                availableCharacters[character] = existingValue
        return true
