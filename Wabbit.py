def Wabbit():
  print("A little girl goes into a pet show and asks for a WABBIT.")
  print("The shop keeper looks down at her, smiles and says:")
  answer  = input("Would you like a lovely FLUFFY LITTLE WHITE rabbit? yes/no : ")
  if (answer.lower() == "no"):
    answer_2 = input("Maybe a cutesy WOOTESLY LITTLE BROWN rabbit?? yes/no : ")
    if(answer_2.lower() == "yes"): #nested conditionals
      print("Actually")
      print("says the little girl")
      print("I don't think my python would notice.")
    else:
      answer_3 = input("Maybe a FUNNY CUTE GREY rabbit?? yes/no : ")
      if(answer_3.lower() == "yes"):
        print("Actually")
        print("says the little girl")
        print("I don't think my python would notice.")
      else:
        answer_4 = input("Maybe a MAJIC BLACK rabbit?? yes/no : ")
        if(answer_4.lower() == "yes"):
          print("Actually")
          print("says the little girl")
          print("I don't think my python would notice.")
        else:
          answer_5 = input("Maybe a FUNNY CUTE GREY rabbit?? yes/no : ")
          if(answer_5.lower() == "yes"):
              print("Actually")
              print("says the little girl")
              print("I don't think my python would notice.")
          else:
            answer_6 = input("Maybe a AMAZING CHOKOLATE rabbit?? yes/no : ")
            if(answer_6.lower() == "yes"):
              print("Actually")
              print("says the little girl")
              print("I don't think my python would notice.")
            else:
              answer_7 = input("Please answer YES, I don't know other rabbits?? yes/no : ")
              if(answer_7.lower() == "yes"):#Deeply nested conditionals
                print("Actually")
                print("says the little girl")
                print("I don't think my python would notice.")
              else:
                Wabbit()
              
  elif( answer.lower() == "yes"):#chained conditional
    print("Actually")
    print("says the little girl")
    print("I don't think my python would notice.")
  else:
    Wabbit()
  
Wabbit()  