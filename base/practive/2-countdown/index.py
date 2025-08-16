def countdown_timer():
    import time
    
    print("\n------ COUNTDOWN TIMER")
    
    try:
        seconds = int(input("Nhap so giay dem nguoc : "))
        
        if seconds < 0:
            print("So giay phai lon hon 0")
            return
        
        print(f"Den nguoc tu {seconds}s")
        
        for i in range(seconds, -1, -1):
            print(f"{i} giay", end="\r")
            time.sleep(1)
        
        print("\nEnd")
        
    except ValueError:
        print("Value Error")
    
countdown_timer()