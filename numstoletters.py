tens={30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety'}
zero_twenty=('zero','one','two','three','four','five','six','seven','eight','nine',
             'ten','eleven','twelve','thirteen','forteen','fifteen','sixteen',
             'seventeen','eighteen','nineteen','twenty')
def nums_to_words(n):
    if any(not x.isdigit() for x in str(n)):
        return ' '

    if n <= 20:
        return zero_twenty[n]
    elif n < 100 and n%10==0:
        return tens[n]
    elif n < 100:
        return nums_to_words(n-(n//10)) + ' ' + nums_to_words(n % 10)
    elif n < 1000 and n % 100 ==0:
        return nums_to_words(n//100) + 'hundred '
    elif n < 1000:
        return nums_to_words(n//100) + 'hundred ' + nums_to_words(n%100)
    elif n < 10000 and n % 1000 ==0:
        return nums_to_words(n//1000) + 'thousand '
    elif n < 10000:
        return nums_to_words(n//1000) + "thousand " + nums_to_words(n%1000)

    return ''
print (nums_to_words(2406))