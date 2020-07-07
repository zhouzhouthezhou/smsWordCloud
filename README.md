# smsWordCloud
Word Cloud generator for SMS

# Dependancies
* python3
* matplotlib
* pandas
* wordcloud

# Usage
Download the [SMS Backup & Restore](https://play.google.com/store/apps/details?id=com.riteshsahu.SMSBackupRestore&hl=en_US) app to your android phone.

In the side menu select "Back up now"

Make sure messages is selected but call logs are not

Under advanced options select "Selected conversations only" and pick the target conversation (single) you wish to analyze

Under backup location save the backup to whatever location is easiest to send the resulting file to your computer. I just saved to my phone and plugged my phone into my computer to transfer the file.

Move the file to the same directory as the analyze.py script and run the following command:
`python analyze.py [file name] [your name] [recipiant's name]`
