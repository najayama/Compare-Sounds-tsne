def cui_input(input_str, converter=str, errmsg=""):
    """
    print input_str , get input from stdin and convert str by converter.
    if ValueError, try again.
    """
    
    while True:
        try:
            inp = converter(input(input_str))
        except ValueError:
            print(errmsg, end="")
        else:
            return inp
        
        