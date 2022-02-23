# from selenium import webdriver
#
# option = webdriver.ChromeOptions()
# option.add_argument("-incognito")
# #option.add_argument("--headless")
# #option.add_argument("disable-gpu")
#
# browser = webdriver.Chrome(executable_path="C:\\Users\\KIIT\\Downloads\\chromedriver.exe", options=option)
# browser.get('https://docs.google.com/forms/d/e/1FAIpQLScobnmCWbWVeqweoiNXlfXpVrKDGrnpiPjwSpK0ezq-I63ouA/viewform')
#
# textboxes = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
# radio_buttons = browser.find_elements_by_class_name("appsMaterialWizToggleRadiogroupOffRadio")
# submit=browser.find_element_by_class_name("appsMaterialWizButtonPaperbuttonContent")
# textboxes[0].send_keys("helloworld@gmail.com")
# radio_buttons[2].click()
# submit.click()

N = int(input())
x = 0 #counter
y=[] # save all inputs
pos = 1 # 1F
for x in range(N):
    y.append(int(input()))
sum=0 # add up all movmenets
#python-like loop
for value in y:
    #loop into y array
    sum= sum+ abs(value-pos) #sum all the movements
    pos = value #update position
print(sum)
pos=1
sum2=0
#C language-like loop
for i in range(len(y)):
    sum2 = sum2 + abs(y[i] - pos)
    pos = y[i]
print(sum2)