# raspi-gpt2-bot
Raspberry Pi enabled GPT2 bot plugin for Wordpress and Twitter

## usage
```
./run_gpt_wordpress.sh 'WORDPRESS_DOMAIN' 'WORDPRESS_USER' 'WORDPRESS_USER_PWD'
```

## Get Twitter credentials
https://developer.twitter.com/en/portal/products/elevated

## Install on Raspberry 4
- Recommended to be ONLY run on a Raspberry Pi as the old version of Tensorflow
  is very insecure
- Choose 32bit Raspberry Lite version, NOT 64 bit at this point
- 4GB RAM should be enough for the 345M model
- ONLY Tensorflow 1.1.13 works on Rapsberry Pi, use AT YOUR OWN RISK,
  as such an old Tensorflow introduces a miriad security vulerabilities.
- Twitter support is experimental and running it live using prod credentials will
  likely result in suspension of your Twitter API write priviliges. Tweet less often.

## Python and Tensorflow
- https://www.alauda.ro/2019/01/how-to-install-python-3-7-on-raspberry-pi/
### Python 3.5
```
sudo apt-get autoremove python*
```
Ensure system is up to date:
```
sudo apt-get update
```
Install the dependencies needed for building the distribution:

    build-essential
    tk-dev
    libncurses5-dev
    libncursesw5-dev
    libreadline6-dev
    libdb5.3-dev
    libgdbm-dev
    libsqlite3-dev
    libssl-dev
    libbz2-dev
    libexpat1-dev
    liblzma-dev
    zlib1g-dev
    libffi-dev
```
sudo apt-get install -y build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev
```
Get the python src distribution:
```
wget https://www.python.org/ftp/python/3.5.0/Python-3.5.0.tar.xz
tar xf Python-3.5.0.tar.xz
cd Python-3.5.0
```
Configure and compile (this might take an awful lot of time, depdning on your Raspberry’s performances):
```
./configure -prefix=/usr/local/opt/python-3.5.0
make -j 4
```
Install:

```
sudo make altinstall
```

```
sudo ln -s /usr/local/opt/python-3.5.0/bin/pydoc3.5 /usr/bin/pydoc3.5
sudo ln -s /usr/local/opt/python-3.5.0/bin/python3.5 /usr/bin/python3.5
sudo ln -s /usr/local/opt/python-3.5.0/bin/python3.5m /usr/bin/python3.5m
sudo ln -s /usr/local/opt/python-3.5.0/bin/pyvenv-3.5 /usr/bin/pyvenv-3.5
sudo ln -s /usr/local/opt/python-3.5.0/bin/pip3.5 /usr/bin/pip3.5
alias python='/usr/bin/python3.5'
alias python3=’/usr/bin/python3.5′
ls /usr/bin/python*
cd ..
sudo rm -r Python-3.5.0
rm Python-3.5.0.tar.xz
. ~/.bashrc

python -V
```
### Tensorflow
- https://www.teknotut.com/en/install-tensorflow-and-keras-on-the-raspberry-pi/



## Posting to Twitter and Nostr
Fill in the provided Nostr and Twitter credentials. For Twitter you need "Elevated" Write-enabled
developer API keys and you need to apply for them and give reasons.

https://developer.twitter.com/en/portal/products/elevated

Once you have credentials post as follows:

```
python3.9 twostr twitter.json nostr.json "This is my first EVER tweet posted to Twitter and Nostr"
```