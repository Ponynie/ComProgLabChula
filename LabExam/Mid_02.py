Choice = input("Population or Sample: ") #ตอบ "Population" หรือ "Sample"
Data = 0
Data_Sq = 0
a = 0
b = 0
i = 1
while a + b < 160 :
    while a + b < 160 and i%2 != 0 :
        a = float(input())
        a_Sq = a**2
        Data = Data + a
        Data_Sq = Data_Sq + a_Sq
        i = i + 1
    while a + b < 160 and i%2 == 0 :
        b = float(input())
        b_Sq = b**2
        Data = Data + b
        Data_Sq = Data_Sq + b_Sq
        i = i + 1
n = i - 1 
mean = Data / n
if Choice == "Population" :
    Standard = ( ( Data_Sq / n ) - ( mean**2 ) )**(0.5)
elif Choice == "Sample" :
    Standard =  ( ( Data_Sq / (n - 1) ) - ( mean**2 )*( n / (n - 1)) )**(0.5)
print(f'Mean is {mean} and Standard Deviation is {Standard}')
