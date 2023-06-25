def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    num_males= int(input("How many males are there? "))
    num_females= int(input("How many females are there? "))
    
   
    int_total= num_males+num_females
    
    m_perc= (num_males/int_total)*100
    f_perc= (num_females/int_total)*100
    print(f'The number of males is \t {num_males}')
    print(f'The number of females \t {num_females}')
    print(f'The total number of students is \t {int_total}')
    print(f'The percentage of females is \t {f_perc:.2f}')
    print(f'The percentage of males is \t {m_perc:.2f}')
      
    



    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc 


if __name__ == '__main__':
    main()
