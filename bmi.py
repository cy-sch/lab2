def calculate_bmi(height,weight):
   print ("height=" +height)
   print ("weight=" +weight)
   bmi = float(weight) / (float(height)*float(height)) 
   print("bmi=" +str(bmi))
   if (bmi < 18.5):
     print("under weight")
     return -1
   elif(bmi>=18.5 and bmi<=25):
      print("normal weight")
      return 0
   elif (bmi>25):
      print("over weight")  
      return 1
calculate_bmi(weight="57",height="1.73")   