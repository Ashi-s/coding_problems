int[] ints =  {-1, 8, 6, 0, 7, 3, 8, 9, -1, 6, 1};
max = 1;
arrLen = len(ints);
for i in range(arrLen):
    a = i;
    counter = 1;
    while (ints[a] > -1 && ints[a] < arrLen && counter < arrLen):
        a = ints[a];
        counter++;

    if (counter > max):
        max = counter;
return max;