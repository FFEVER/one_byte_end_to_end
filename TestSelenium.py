from selenium import webdriver
import time
# create a new Firefox session
def main():
    driver = webdriver.Chrome('/Users/natpawee/chromedriver')
    driver.get("http://127.0.0.1:8000/polls/")
    time.sleep(2)  # Let the user actually see something!
    #driver.find_element_by_xpath("//a[@href='/polls/1/']").click()

    html_list = driver.find_element_by_xpath("//ul")
    items = html_list.find_elements_by_tag_name("li")
    size_question = len(items)
    round_question=0
    array_poll=[]
    for item in items:
        array_poll.append(item.text)
    for item in array_poll:
        print(item)
        round_question+=1
        print("enter question"+str(round_question))
        driver.find_element_by_link_text(item).click()
        time.sleep(2)
        number_choice =  driver.find_elements_by_css_selector("input[type='radio'][name='choice")
        for i in range (len(number_choice)):
            print("select choice : "+str(i+1))
            choice_id = str("choice"+str((i+1)))
            str_1 = str("input[type='radio'][id='")
            str_3 = str("']")
            complete_str = str_1+choice_id+str_3
            driver.find_elements_by_css_selector(complete_str)[0].click()
            driver.find_elements_by_css_selector("input[type='submit'][value='Vote']")[0].click()
            print("complete vote")
            time.sleep(2)
            if((i+1)<len(number_choice)):
                print("vote again")
                driver.find_element_by_link_text('Vote again?').click()
                time.sleep(1)
            else:
                break
        if round_question<size_question:
            print("enter another poll")
            driver.get("http://127.0.0.1:8000/polls/")
            time.sleep(2)
        else:
            driver.quit()




if __name__=='__main__':
    main()