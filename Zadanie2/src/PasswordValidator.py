class PasswordValidator:
    def ValidPassword(self,psw):
        numCounter = 0
        bigLetterCounter = 0
        strnumbers = ["1","2","3","4","5","6","7","8","9","0"]
        specialCharacters = ["!","@","#","$","%","^","&","*","(",")","-","+","?","_","=",",","<",">","/"]
        specialCharacterCounter = 0
        if type(psw) is str:
            for i in psw:
                if i in strnumbers:
                    numCounter+=1
                if i.isupper():
                    bigLetterCounter+=1
                if i in specialCharacters:
                    specialCharacterCounter+=1
            if numCounter>=3 and bigLetterCounter >=1 and specialCharacterCounter>=1:
                return True
            else:
                return False
        else:
            raise Exception("Bad password type!")