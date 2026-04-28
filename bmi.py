def calculate_bmi(height,weight):
   print ("height=" +height)
   print ("weight=" +weight)
   bmi = float(weight) / (float(height)*float(height)) 
   print("bmi=" +str(bmi))
   if (bmi < 18.5):
     print("under weight")
   elif(bmi>=18.5 and bmi<=25):
      print("normal weight")
   elif (bmi>25):
      print("over weight")  
calculate_bmi(weight="57",height="1.73")   