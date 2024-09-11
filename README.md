# Hair cut

This projet is under MIT License, do whatever you want with this. You just have to use it in a venv
*Why am I updating this*

## Installation

**Windows**

```bat
git clone https://github.com/Dulinniel/hair-cut.git
cd hair-cut
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```
**Linux**

Look, I'm a good girl I updated Linux installation process

```bash
git clone https://github.com/Dulinniel/hair-cut.git
cd hair-cut
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

In the venv, run the following command :

```bash
flask --app hair run
```

And with that, you could use this *wonderful* application ( that's a lie, this is useless )

Oh and, the content of `coiffeurs.json` come from [here](https://www.data.gouv.fr/fr/datasets/coordonnees-des-enseignes-de-coiffure-comportant-des-jeux-de-mots-cocasses-dans-leur-appellation/)

## Todo

- [ ] Add a working search bar
- [ ] Add filters
- [ ] Sort the results in alphabetical order
- [ ] Give the page a real CSS
- [ ] Give each hair sylist a single page with more info about it
- [ ] Find a purpose to this shit