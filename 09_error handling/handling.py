file=open('youtube.txt','w')
try:
    file.write('This is me Abhay')
finally:
    file.close()

    # or
with open('youtube.txt','w') as file:
    file.write('Just learning python with chai aur code')

#isme close krne ki jarurat nahi padti 