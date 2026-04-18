## save the heavy data into a text file

my_data=["hello world" for i in range(100)]

with open("Text_File.txt",'w') as f:
    for data in my_data:
        f.write(data + "\n")

## read The data from a text file

with open("Text_File.txt",'r') as f:
    while True:
        data=f.readline()
        if not data:
            break
        else:
            print(data)


## reading the DATA Chunk by Chunk

with open("Text_File.txt",'r') as f:
    chunk_size=50
    while True:
        data=f.read(chunk_size)
        if not data:
            break
        else:
            print(data)