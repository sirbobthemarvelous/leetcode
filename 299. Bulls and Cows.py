class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_dict = {}
        guess_dict = {}
        bulls = 0
        cows = 0

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                if secret[i] in guess_dict and guess_dict[secret[i]] >0:
                    cows += 1
                    guess_dict[secret[i]] -= 1
                else:
                    secret_dict[secret[i]] = secret_dict.get(secret[i], 0) +1
                if guess[i] in secret_dict and secret_dict[guess[i]] >0:
                    cows += 1
                    secret_dict[guess[i]] -= 1
                else:
                    guess_dict[guess[i]] = guess_dict.get(guess[i], 0) + 1

        return str(bulls) + "A" + str(cows) + "B"
        