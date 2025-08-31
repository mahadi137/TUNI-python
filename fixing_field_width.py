"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""

def main():                                   
    for i in range(1, 11):                    
        for j in range(1, 11):                
            if j < 11:                        
                print(f"{i*j:4.0f}", end="")  
            else:                             
                print(f"{i*j:2.0f}", end="")  
        print()                               
                                              
if __name__ == "__main__":                    
    main()                                    
