#Legyen adott egy kifejezés, melyben számok, zárójelek, illetve operátorok szerepelnek. Minket most csak a zárójelek érdekelnek. Háromféle zárójel szerepelhet a kifejezésben: "{}", "()", "[]". Ha egy zárójelet megnyitunk, akkor a típusának megfelelő párral be is kell zárni. A zárójelek hatásköre nem keresztezheti egymást. A feladat: egy kifejezésről döntsük el a zárójelek alapján, hogy helyes-e vagy sem (a számokkal és az operátorokkal most ne foglalkozzunk).

def Zarojeles(kifejezes):
    zarojelek = []
    for i in kifejezes:
        if i == "{" or i == "(" or i == "[":
            zarojelek.append(i)
        elif i == "}" or i == ")" or i == "]":
            if len(zarojelek) == 0:
                return False
            elif i == "}" and zarojelek[-1] == "{":
                zarojelek.pop()
            elif i == ")" and zarojelek[-1] == "(":
                zarojelek.pop()
            elif i == "]" and zarojelek[-1] == "[":
                zarojelek.pop()
            else:
                return False
    if len(zarojelek) == 0:
        return True
    else:
        return False

def main():
    print(Zarojeles("((5+3)*2+1)"))
    print(Zarojeles("{[(3+1)+2]+}"))
    print(Zarojeles("(3+{1-1)}"))
    print(Zarojeles("[1+1]+(2*2)-{3/3}"))
    print(Zarojeles("(({[(((1)-2)+3)-3]/3}-3)"))

if __name__ == "__main__":
    main()