for making wav to mp3 do something like that

sudo apt-get install mpg321 # also there is mpg123 for mp3 to wav sudo mpg123 -w a.wav a.mp3 

sudo mpg321 -w "......mp3" ".....wav" 

everything written and works in terminal can be a bash code in .sh files (do not forget to add sudo or call it with sudo) 

make sudo chmod +x (or 777)  .sh

then call  ./..sh file
