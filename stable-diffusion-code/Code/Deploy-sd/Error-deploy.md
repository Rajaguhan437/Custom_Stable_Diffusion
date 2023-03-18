 # Stable-Diffusion Model Deployment--ERROR :

 -          The Stable-diffusion model needs NVIDIA GPU To execute.

 -          But the free-version of hugging face doesn't provide GPU support

 -          Just 2 CPUs with 16 GB RAM But no GPU
      
      
![Hugging-Face Cloud Details](<Screenshot%20(111).png>) 


-          The logs from hugging-face deployment console too mentions the same.

-          pzztw 2023-03-18T02:49:14.174Z RuntimeError: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx


![Hugging-Face Cloud Details](<Screenshot%20(110).png>) 


-          So, Because of this my model is unable to be deployed.
