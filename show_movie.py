class ShowMovie:
    def __init__(self,raw,column):
        self.raw=raw
        self.column=column
        self.user_details={}

    def showTicket(self):
        for i in range(self.raw):
            for j in range(self.column):
               if i==0:
                   if j==0:
                       print(' ',end=' ')
                   else:
                       print(j,end=' ')   
               elif j==0:
                   print(i,end=' ')
               else:
                   print("S",end=' ')    
                      
                          
            print()


    def ticket_buy(self):
        raw=int(input("Enter the raw number."))
        column=int(input("Enter the column number."))

        ticket_prize=10
        seat_no=str(raw) + str(column)
        option=int(input(f'your opt raw is {raw} and column is {column},so prize of your seat is {ticket_prize}. if you still wish to book the ticket please enter \n1.Yes \n2. No '))

        if option==1:
            name=input("Enter your name: ")
            gender=input("Enter your gender")
            age=int(input("Enter your Age"))
            phone_no=int(input("Enter your Phone_no please"))
            self.user_details[seat_no]=[name,gender,age,phone_no]
            print("Booked Successfully..")
        else:
            print("No problem, Thankyou for connecting with Book my show!!")







    def statictics(self):
        
        total_seats=self.raw*self.column
    
        ticket_perchased=len(self.user_details)
        persentage_sold=((self.user_details)/(total_seats))*100
        prize_list=[]
        for k,v in self.user_details.items():
            prize_list.append(v[3])
        currunt_income=sum(prize_list)
        if total_seats <=60:
            total_income=total_seats*10
        else:
            front_prize=10
            back_prize=8
            total_income=front_prize*back_prize
        print(f"Total Income from the tickets {total_income}")


    def user_info(self):
        raw=int(input("Enter the raws: "))   
        column=int(input("Enter the column: "))

        seat_no=raw*column
        user_details=self.user_details.get(seat_no,None)
        if user_details:
            print(f"Name of user: {user_details[0]}") 
            print(f"Gender of user: {user_details[1]}") 
            print(f"Age of user: {user_details[2]}") 
            print(f"Phone of user: {user_details[3]}") 


        else:
            print("Seat is not Booked.") 

    def is_seat_booked(self,raw,column):
        seat_no=raw*column
        if seat_no in self.user_details.keys():
            return True
        return False           
          
         




# obj=ShowMovie(7,8)
# obj.showTicket()



















# def palindrone(num):
#     sum=0
#     while num>0:
#         rem=num%10
#         sum=sum*10+rem
#         num=num//10
#     return sum
# num=int(input("Enter number: "))
# temp=num
# a=palindrone(num)
# #print(a)
# if a==temp:
#     print(f"{num} is palindrome number")
# else:
#     print(f"{num} is not palindrone number.")    


# def armstrong(num):
#     sum=0
#     while num>0:
#         rem=num%10
#         sum=sum+rem*rem*rem
#         num=num//10
#     return sum
# num=int(input("Enter number: "))
# temp=num
# a=armstrong(num)
# print(a)
# if a==temp:
#     print(f"{num} is armstrong number")
# else:
#     print(f"{num} is not armstrong number.")    


# 153=1+125+27=153


# def reverse(num):
#     rev=0
#     while num>0:
#         rem=num%10
#         rev=rev*10+rem
#         num=num//10
#     return rev
# num=int(input("Enter number: "))
# rev=reverse(num)
# print(f"Reverse number is {rev}")



# str="kiran pagar"
# print(str[::-1])

# def sqr(lst):
#     return lst**2
# lst=[1,2,3,4,5]
# a=list(map(sqr,lst))
# print(a)