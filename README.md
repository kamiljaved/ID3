
<h1 align="center">
  <br>
  ID3 Decision-Tree Maker
  <br>
</h1>

<h4 align="center">A Python console app for creating Decision-Trees.</h4>

<p align="center">

  <a href="https://www.python.org/">
		<img src="http://ForTheBadge.com/images/badges/made-with-python.svg" alt=" Made with Python.">
  </a>

</p>

<p align="center">
  <a href="#about">About</a> •
  <a href="#how-to-use">How To Use</a>
</p>

<hr>

## About

This is a console-based Python App to create Decision-Trees for Data & Attributes provided in a JSON file, using the ID3 algorithm. Uses OOP for implementation of Tree Nodes. 
<p> It offers Gain-Information and Gain-Ratio methods for the ID3 algorithm</p>
The implementation uses:

* Python
* JSON
* OOP Concepts
* Machine Learning Concepts

## How To Use

Make sure [Python](https://www.python.org/) is installed on your system. 
To clone this application, you'll need [Git](https://git-scm.com). From your command line:

```powershell
# Clone this repository (or download from github page)
$ git clone https://github.com/kamiljaved98/ID3

# Go into the repository
$ cd ID3

# run the app
python(3) main.py -a <AttributeFile> -d <DataFile> (Optional: -t [calc. Test-Set Accuracy] -r [use Gain-Ratio])

# example command
python main.py -a ./tests/PlayTennis/attributes.json -d ./tests/PlayTennis/data.json

```


---

> [kamiljaved.pythonanywhere.com](https://kamiljaved.pythonanywhere.com/) &nbsp;&middot;&nbsp;
> GitHub [@kamiljaved](https://github.com/kamiljaved)
