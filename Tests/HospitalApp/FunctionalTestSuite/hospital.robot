*** Settings ***
Resource  ../../../Resources/hospitalkeywords.robot

*** Test Cases ***
Link opening test case
    [Documentation]  Link opening
    [Tags]  patient
    open browser  ${url}  chrome
    maximize browser window

login test case
    [Documentation]  Providing inputs
    [Tags]  Patient
    user login

register test case
    [Documentation]  Registering a patient
    [Tags]  patient
    patient register
    click element  xpath=/html/body/nav/div/div/ul/li[2]/a
    sleep  3s

Search patient test case
    [Documentation]  Searching a patient
    [Tags]  patient
    click element  xpath=/html/body/nav/div/div/ul/li[3]/a
    sleep  1s
    input text  name:mobile  8596748596
    sleep  2s
    click button  xpath=/html/body/div/div[1]/div/form/table/tbody/tr[3]/td[2]/button
    sleep  2s

Update patient test case
    [Documentation]  Update a patient
    [Tags]  patient
    click element  xpath=/html/body/nav/div/div/ul/li[4]/a
    sleep  2s
    input text  name:mobile  8722749566
    sleep  3s
    click button  xpath:/html/body/div/div/div/form/table/tbody/tr[3]/td[2]/button
    sleep  2s
    patient update
    sleep  2s

Delete patient test case
    [Documentation]  delete patient
    [Tags]  patient
    click element  xpath=/html/body/nav/div/div/ul/li[5]/a
    sleep  1s
    input text  name:mobile  8722749569
    sleep  1s
    click button  xpath=/html/body/div/div/div/form/table/tbody/tr[3]/td[2]/button
    sleep  1s
    click element  xpath=/html/body/nav/div/div/ul/li[2]/a
    sleep  3s
    click element  xpath=/html/body/nav/div/div/ul/li[6]/a
    sleep  3s
    close browser