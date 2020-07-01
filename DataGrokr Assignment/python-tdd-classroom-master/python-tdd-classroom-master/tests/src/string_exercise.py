class StringExercise:

    def __init__(self):
        pass   # Do some initial setup in this constructor method, if needed

    def reverse_string(self, input_str):
        """
        Reverses order of characters in string input_str.
        """
        text=input_str[::-1]
        return text

    def is_english_vowel(self, character):
        """
        Returns True if character is an english vowel
        and False otherwise.
        """
        flag=False
        if(character=='a'or character=='e'or character=='i'or character=='o'or character=='u'
           or character=='A'or character=='E'or character=='I'or character=='O'or character=='U'):
            flag=True
        return flag

    def find_longest_word(self, sentence):
        """
        Returns the longest word in string sentence.
        In case there are several, return the first.
        """
        splitword=sentence.split(" ")
        longestword=" "
        n=len(splitword)
        for i in range(0,n):
            if(len(splitword[i])>len(longestword)):
                longestword=splitword[i]
        return longestword
            

    def get_word_lengths(self, text):
        """
        Returns a list of integers representing
        the word lengths in string text.
        """
        n=len(text)
        ans_list=[]
        ans=0
        for i in range(0,n):
            if(text[i]!=' '):
                ans=ans+1
            else:
                ans_list.append(ans)
                ans=0
        ans_list.append(ans)
        return ans_list
