*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Valid Password
    Input Credentials  matti  matti123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  uusisalsa1
    Output Should Contain  Username is already taken

Register With Too Short Username And Valid Password
    Input Credentials  ab  matti123
    Output Should Contain  Invalid username

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  matti1!  matti123
    Output Should Contain  Invalid username

Register With Valid Username And Too Short Password
    Input Credentials  matti  mats1
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  matti  mattisalasana
    Output Should Contain  Password must contain something other than letters

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123
