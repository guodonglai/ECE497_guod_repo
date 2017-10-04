#This is a ReadMe.md File
1. Boneserver uses socket.emit to send the matrix data from the bone to the browser. Then the 'matrix' function in matrixLED.js was called to display the initial image on the browser.
After that, the connect function in matrixLED.js was called to make a connection between bone and the browser. The browser send one 8 bit value at a time to boneserver whenever the LED grid was clicked
to actually change the LED on bone. The browser also changes its webpage matrix whenever a click was made. 
2. When LED is clicked, it checks its current data value disp[2*i](green bit) and disp[2*i+1](red bit) to determine its previous status. Based on previous values, then determine 
next color.Toggle the corresponding bit and then send the data back to boneserver. Also, the browser grid class will be altered too.  
3. .on entry turn on green color. I have also added two more entrys: red and orange to change the color.
4. Firstly, it checks its current data value disp[2*i](green bit) and disp[2*i+1](red bit) to determine its previous status. If blank, go green. If green, go orange. If orange, go red. 
If red, go blank.Then it toggles the corresponding bit by doing xor 0x1<<j with itself. Finally, the matrixLED.js send that one bit with specified index at a time to change the LED on bone. 
5. Already changed matrixLED.html to modify the title into my own name.
