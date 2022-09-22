# vitrocam
Vitrocam automation scripts 

Paper: https://www.biorxiv.org/content/10.1101/2022.06.16.496351v1

Instructions:
1. Download the folder temhubvib onto your Pi Desktop. 
2. On `/home/pi/Desktop`, create a folder called `grid_images`. 
3. In a terminal, change directories to temhubvib, e.g. with `cd /home/pi/Desktop/temhubvib`. 
4. Run `./vitrocam.py`. 
5. Here are the options: 
    a. "Preview" will capture a still image with the same capture conditions as the video. This is useful for, e.g., checking your grid before plunging. 
    b. "Live" will turn on the camera for 1 minute with the same capture conditions as the video. This is useful for adjusting focus and position of the camera, lighting, etc. 
    c. "Capture" will wait for blotting to occur, then automatically trigger the camera to record a short video and extract the frames into `~/Desktop/grid_images`
