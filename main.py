from show_movie import ShowMovie
class Main:
    def execute(self,choice):
        if choice==1:
            print("************Show Movie ticket************")
            show_movie.showTicket()
        if choice==2:
            show_movie.ticket_buy()
            print("**************Booked moviw Ticket************* \n")
        if choice==3:
            print("**************Statictics**************")
            show_movie.statictics()    
        if choice==4:
            print("**************Show booked movie Ticket..****************")
            show_movie.user_info()
        if choice==0:
            print("*********Thank you for Connecting to Us..*************")    
        

if __name__=="__main__":
    row=int(input("Enter the raw: "))
    column=int(input("Enter Column for seats to each raw: "))

    show_movie=ShowMovie(row,column)
    
    main=Main()
    
    while True:
        choice=int(input("Enter your Choice: \n1.Show Moview Ticket \n2.Booked Movie Ticket \n3.Statictics \n4.Shoe Movie Booed ticket \nEnter Choice: "))
        main.execute(choice)
