def main():
    for i in range(1, 106):
        printing_number = True
        
        if i % 11 == 0:
            print('Bong')
            continue

        if i % 3 == 0:
            printing_number = False
            print('Fizz', end='')
        if i % 5 == 0:
            printing_number = False
            print('Buzz', end='')
        if i % 7 == 0:
            printing_number = False
            print('Bang', end='')
        
        if printing_number:
            print(i, end='')
        
        print()

if __name__ == "__main__": main()