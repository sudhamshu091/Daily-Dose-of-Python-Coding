def filenotfound_exception(file):
    try:
        open_file = open(file, 'r')
        print(open_file.readline())
    except FileNotFoundError as error:
        print("Error occured,can't read file", error)
    finally:
        try:
            print("Closing the file....")
            open_file.close()
            print("Closed file",file)
        except:
            pass
if __name__ == '__main__':
    filenotfound_exception('new.txt')
