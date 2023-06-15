*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***                  StartingX     StartingY     StartingMoveCount     Direction     EndingX     EndingY     EndingMoveCount
From NW corner move West, Bounce    0             0             0                     WEST          0           0           1
From NW corner move South, OK       0             0             1                     SOUTH         0           1           2
From NW corner move East, OK        0             0             15                    EAST          1           0           16
From NE corner move West, OK        9             0             15                    WEST          8           0           16
From NE corner move East, Bounce    9             0             4                     EAST          9           0           5
From NE corner move South, OK       9             0             8                     SOUTH         9           1           9
From SW corner move West, Bounce    0             9             7                     WEST          0           9           8
From SW corner move East, OK        0             9             11                    EAST          1           9           12
From SW corner move North, OK       0             9             9                     NORTH         0           8           10
From SE corner move South, Bounce   9             9             1926472               SOUTH         9           9           1926473

*** Keywords ***
Move character
    [Arguments]    ${startingX}    ${startingY}    ${startingMoveCount}    ${direction}    ${endingX}    ${endingY}    ${endingMoveCount}
    Initialize character xposition with  ${startingX}
    Initialize character yposition with  ${startingY}
    Initialize character moveCount with  ${startingMoveCount}
    Move in direction                    ${direction}
    Character xposition should be        ${endingX}
    Character yposition should be        ${endingY}
    Character moveCount should be        ${endingMoveCount}