def fraction(value, index):
    array = [4,5,2,0]           #list of numbers
    index_val = array[index]    # if index is > array length, Indexerror occurs
    value/index_val             # if index value is 0 ,ZeroDivisionError occurs
    return value/index_val
if __name__ == "__main__":
    index = 1
    value = 54
    try:
        res = fraction(value, index)
        print("Fraction answer is",res)
    except IndexError:
        print("Index ",index,"is out of range for the length of array entered as input,please recheck your input")
    except ZeroDivisionError:
        print("Dividing by Zero error,either the indexed element is zero or entered array length is zero")
    except Exception as exception:
        print("Some other error which I have not handled in this program")
        raise exception
