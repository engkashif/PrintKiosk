f = open('med_batch18.txt', 'a')
for i in range(18000,19000):
    roll=str(i)
    roll_lined=roll+"\n"
    f.write(roll_lined)
f.close()
