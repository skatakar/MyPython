#####################################
##reverse string
####################################

#code
##str1 = "test"
##str2=''
##x= len(str1)
##for nu in range((x-1)-0,-1,-1):
##    str2 = str2+str1[nu]    
##print str2

##########
##output
##>>> 
##====================== RESTART: C:/Python27/reverse.py ======================
##tset
##>>> 

###################################################
#replace third l in "hello world"
###################################################
#code
##text = "Hello World"
##print text
##list_text = list(text)
##print list_text
##count=0
##for i in range(len(list_text)):
##    if list_text[i]=="l":
##        count = count+1
##        if count ==3:
##            list_text[i] = "t"
##
##print list_text
##text = ''.join(list_text)
##print text
##
##
##output    
##Hello World
##['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
##['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 't', 'd']
##Hello Wortd

###########################
##Count how many times its present
###########################

#code
##
##text = "hello world"
##list_text = list(text)
##uniq_list= []
##for c in list_text:
##    if c not in uniq_list:
##        uniq_list.append(c)
##
##print uniq_list
##for c in uniq_list:
##    print c, list_text.count(c)

##output:
##>>> 
##====================== RESTART: C:/Python27/reverse.py ======================
##['h', 'e', 'l', 'o', ' ', 'w', 'r', 'd']
##h 1
##e 1
##l 3
##o 2
##  1
##w 1
##r 1
##d 1
##>>> 
