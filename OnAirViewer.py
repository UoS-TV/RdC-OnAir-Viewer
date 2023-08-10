import os

rundownID = input("Please enter Rundown ID: ")
# print("Rundown ID: ", rundownID)

url = 'https://rundowncreator.com/surrey/OnAirTimerDisplay.php?RundownID='+rundownID

print("Opening ", url)

os.system('"C:/Program Files (x86)/Google/Chrome/Application/chrome.exe" --window-position=1920,0 --kiosk --user-data-dir=c:/onairviewer --app='+url)