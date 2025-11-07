def translatedrom(n):
    if not 1 <= n <= 3999:
        return "invalid Enter number 1–3999 buddy"
    
    vals = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    syms = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    
    roman = ''
    for i in range(len(vals)):
        while n >= vals[i]:
            roman += syms[i]
            n -= vals[i]
    return roman

num = int(input("Enter number (1-3999): "))
print(translatedrom(num))
