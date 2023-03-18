# INFO :

-   ## App.py :
     -    ### It is a python script file
          -     which loads the trained stable-difussuion model
          -     accepts **image, prompt, and other parameters** which are needed to generate image.
          -     it is done through using **GRADIO Web UI**
        
     -   ### GRADIO Web UI :
          -     A Python Library
          -     deploys AI model to **Hugging-Face**
          -     Launches a Web UI on local host and creates a link by which other system can access this model
          -     Receives input via the Web UI 
          -     Outputs the result to the Web UI
          -     It also enables to customize the Web UI just like designing a website
        
     -   ## **NOTE**  :
          -     The model should be uploaded to app.py directory's before executing it.
          -     The Gradio Web UI eliminates the need of postman api because it takes care of both
               
                                                                                             -  1.API
                               
                                                                                             -  2.Front-End
-  ## Requriments.txt :
      - It contains all needed python libraries and dependencies to be downloaded in order for successful execution of app.py
      - It has also the versions of the libraries mentioned

-  ## NOTE :

    - Both the above files are mandatory to be uploaded to hugging face for sucessful deployment
