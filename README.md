# Generative-AI Hackathon -- Character.XYZ :

-    The AI model generates avatar faces using a custom stable diffusion model
-    Deploy the model to Hugging Face
-    Test the output using Postman

# Expected :
 - ### Code implementation  :

    -    def generate_avatar_face(image_path):<br>
         -    Parameters:<br>
                   -    image_path (str): The path to the input image.<br>
         -    Returns:<br>
                  -   avatar_face (PIL.Image): The generated avatar face.<br>

-  ### Test :<br>
    - Using Postman:
        -      Base URL     : https://example.com/api/
        -      Request      : POST /avatar-face
        -      Content-Type : png/jpeg

#  Actual :
 - ### Code Implementation  :

    -    def generate_avatar_face(prompt, negative_prompt, num_samples, num_inference_steps, guidance_scale, strength, image_url):<br>
         -    Parameters:<br>
                 -    image_path    (str)     : The path to the input image . [Mandatory]<br>
                 -    prompt        (str)     : Description of image . [Optional]<br>
                 -    negative_prompt(str)    : The description which shouldn't be in image . [Optional]<br>
                 -    num_samples   (num)     : Number of output images to be produced . [Optional]<br>
                 -    num_inference_steps(num): Number of steps to process the image . [Optional]<br>
                 -    guidance_scale(num)     : Describes the freedom of model to follow the prompt . [Optional]<br>
                 -    strength      (num)     : Describes the noise percentage to be added to original image . [Optional]<br>
          -   Returns:<br>
                 -   avatar_face (.png[Image]): The generated avatar face.<br>


 - ###  Deployment & Testing :
      -    Using Gradio :
              -     Gradio takes care of
                      -  1.Deployment on Hugging-Face
                      -  2.API Testing
                      -  3.Front-End Web UI
                      -  4.So, No need of postman-testing

