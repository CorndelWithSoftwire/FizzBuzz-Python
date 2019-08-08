def main():
    for i in range(1, 144):
        outputs = []

        if i % 11 == 0:
            outputs.append('Bong')

        if i % 3 == 0 and 'Bong' not in outputs:
            outputs.append('Fizz')
        if i % 5 == 0 and 'Bong' not in outputs:
            outputs.append('Buzz')
        if i % 7 == 0 and 'Bong' not in outputs:
            outputs.append('Bang')
            
        if i % 13 == 0:
            index = ([i for i, j in enumerate(outputs) if j[0] == 'B'] or [len(outputs)])[0]
            outputs.insert(index, 'Fezz')

        if not outputs:
            outputs.append(str(i))

        print(str(i) + ': ' + ''.join(outputs))

if __name__ == "__main__": main()