def calculate_bmi(height,weight):
   print ("height=" +str(height))
   print ("weight=" +str(weight))
   bmi = weight / (height*height) 
   print("bmi=" +str(bmi))
   if (bmi < 18.5):
     print("under weight")
   elif(bmi>=18.5 and bmi<=25):
      print("normal weight")
   elif (bmi>25):
      print("over weight")  
calculate_bmi(weight=57,height=1.323)   