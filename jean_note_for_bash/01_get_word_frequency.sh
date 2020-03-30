#!/bin/bah

echo "[Jean]: On utiliser -o -E '\w+\ input file pour print all words"
echo "[Jean]: grep -o -E '\w+' words.txt "
echo "------------------"
grep -o -E '\w+' words.txt
echo "------------------"
echo
echo

echo "[Jean]: Ensuite, on fais sort !"
echo "[Jean]: grep -o -E '\w+' words.txt | sort"
echo "------------------"
grep -o -E '\w+' words.txt | sort
echo "------------------"
echo
echo


echo "[Jean]: ensuite, we calculate the counts  for each unique words par uniq -c "
echo "[Jean]: grep -o -E '\w+' words.txt | sort | uniq -c "
echo "------------------"
grep -o -E '\w+' words.txt | sort | uniq -c 
echo "------------------"
echo
echo

echo "[Jean]: ensuite, on fais sort encore par sort -nr "
echo "------------------"
grep -o -E '\w+' words.txt | sort | uniq -c | sort -nr 
echo "------------------"
echo
echo


echo "[Jean]: ensuite, use function , awk to print , \$2 position is name \$1 position is cnts"
echo "[Jean]: grep -o -E '\w+' words.txt | sort | uniq -c | sort -nr | awk '{print \$2 \" \" \$1}'"
grep -o -E '\w+' words.txt | sort | uniq -c | sort -nr | awk '{print $2 " " $1}'


