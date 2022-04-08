*** Settings ***
Library  SeleniumLibrary


*** Variables ***
${url}  http://127.0.0.1:5000/

*** Keywords ***
user login
    sleep  2s
    input text  name:logusername  admin
    sleep  1s
    input text  name:logpassword  12345
    sleep  1s
    click button  xpath=/html/body/div/div/dic/form/table/tbody/tr[3]/td[2]/button

patient register
    input text  name:patname  Harish
    input text  name:mobile  8596748576
    input text  name:age  23
    input text  name:address  Bangalore
    input text  name:place  Bangalore
    input text  name:pincode  563364
    input text  name:dob  11-01-2000
    input text  name:pwd  12345
    input text  name:cfnpwd  12345
    sleep  3s
    click button  xpath=/html/body/div/div/dic/form/table/tbody/tr[11]/td[2]/button

patient update
    input text  name:patname  Shoban
    input text  name:mobile  8722749566
    input text  name:age  22
    input text  name:address  Bangalore
    input text  name:place  Bangalore
    input text  name:pincode  563162
    input text  name:dob  11-01-2000
    input text  name:pwd  123
    input text  name:cfnpwd  123
    sleep  3s
    click button  xpath=/html/body/div/div/div/form/table/tbody/tr[11]/td[2]/button