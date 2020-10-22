
# M6 #7

# the list in the module assignment is only 19 names, I have added the 20th

famous_list = ''' \
Marilyn Monroe (1926 – 1962) American actress, singer, model
Abraham Lincoln (1809 – 1865) US President during American civil war
Nelson Mandela (1918 – 2013)  South African President anti-apartheid campaigner
John F. Kennedy (1917 – 1963) US President 1961 – 1963
Martin Luther King (1929 – 1968)  American civil rights campaigner
Queen Elizabeth II (1926 – ) British monarch since 1954
Winston Churchill (1874 – 1965) British Prime Minister during WWII
Donald Trump (1946 – ) Businessman, US President.
Bill Gates (1955 – ) American businessman, founder of Microsoft
Muhammad Ali (1942 – 2016) American Boxer and civil rights campaigner
Mahatma Gandhi (1869 – 1948) Leader of Indian independence movement
Mother Teresa (1910 – 1997) Macedonian Catholic missionary nun
Christopher Columbus (1451 – 1506) Italian explorer
Charles Darwin (1809 – 1882) British scientist, theory of evolution
Elvis Presley (1935 – 1977) American musician
Albert Einstein (1879 – 1955) German scientist, theory of relativity
Paul McCartney (1942 – ) British musician, member of Beatles
Queen Victoria ( 1819 – 1901) British monarch 1837 – 1901
Pope Francis (1936 – ) First pope from the Americas
Jawaharlal Nehru (1889 – 1964) Indian Prime Minister 1947 – 1964
'''

while True:
    name = input('Please Enter the name of the famous individual? ')
    # sneaky, sneaky, you have to capitalize appropriately before doing
    # the search, look at the example output in the assignment...
    name = name.title()

    # print(name)           # debug

    index = famous_list.find(name)

    # print(index)          # debug
    if index > -1:
        print('Yup, ', name, ' did make the Top 20 cut!')
    else:
        print('Sorry, ', name, ' did not make the Top 20 cut!')
