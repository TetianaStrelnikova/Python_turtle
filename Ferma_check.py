#Fermat’s Last Theorem says that there are no positive integers a, b, and c such that an + bn = cn for any values of n greater than 2.
#1. Write a function named check_fermat that takes four parameters — a, b, c and n —and checks to see if Fermat’s theorem holds. If n is greater than 2 and an + bn = cn the program should print, “Holy smokes, Fermat was wrong!” Otherwise the program should print, “No, that doesn’t work.”
#2. Write a function that prompts the user to input values for a, b, c and n, converts them to integers, and uses check_fermat to check whether they violate Fermat’s theorem
# For any integer n > 2, the equation an + bn = cn has no positive integer solutions

def check_fermat (a,b,c,n):
  if n>2 and (a**n + b**n) == c**n:
    print("Holy smokes, Fermat was wrong!")
  else: 
    print("No, that doesn’t work.")

check_fermat(int(input("Let's check, maybe Fermat was wrong? Enter a ")),int(input("Enter b ")),int(input("Enter c ")),int(input("Enter n ")))