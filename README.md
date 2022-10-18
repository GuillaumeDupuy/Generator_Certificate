# Certificate Generator

<h2> Make your Template : </h2>

- If you want change the template, copy your template of certificate in the *img* directory.
  <br>
  - Make sure you name it Template.jpeg if you don't then you have to change **im = Image.open(r'Template.jpg')** to **im = Image.open(r'name of your template with extension')**
  <br>
- If you want change the fonts, copy your fonts in the *Fonts* directory. You can [Downlaod your front here](https://www.1001fonts.com/signature-fonts.html?page=2)
  <br>
  - Which font do you change if you want to change font used for attendees name you should change **fon = ImageFont.truetype("GothamBold.ttf", 60)** to **fon = ImageFont.truetype("font you want to use", size of font)**
  - And if you want to change font used for Signatures you should change **fox = ImageFont.truetype("PWSignaturetwo.ttf", 50)** to **fox = ImageFont.truetype("font you want to use", size of font)**

<hr>

<h2>Run the Projet</h2>

<h3>Dependencies Installation : </h3>

```sh
pip install setup/requirements.txt
```

<h3>Run code : </h3>

```sh
python Certificate_Generator.py
```

<hr>

<h1>Certificate Generator Input Template : </h1></>

<a href="#">
  <div align="center">
    <img src="img/Template.jpg" width='800'/>
  </div>
</a>

<hr>

<h1>Certificate Generator Output Result :</h1>

<a href="#">
  <div align="center">
    <img src="/certificates/certificate_DUPUY Guillaume.jpeg" width='800'/>
  </div>
</a>