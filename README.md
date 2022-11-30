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
- https://www.yeti.co/blog/setting-up-a-raspberry-pi-with-raspbian-and-pyenv-running-python-35
- https://stackoverflow.com/questions/39371772/how-to-install-anaconda-on-raspberry-pi-3-model-b
- https://towardsdatascience.com/3-ways-to-install-tensorflow-2-on-raspberry-pi-fe1fa2da9104?gi=1247108a5f5c
- https://github.com/microsoft/CameraTraps/issues/232
### Conda
```
wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-armv7l.sh
/bin/bash Miniconda3-latest-Linux-armv7l.sh
 source ~/.bashrc
## Install our specific version fo tensorflow
conda config --add channels rpi
 conda install python=3.5
 conda install python=3.6
 ```

### Get tensorflow
Get old tensorflow from among these libraries, depending on your python version
https://www.piwheels.org/simple/tensorflow/



```
sudo apt-get install gcc python3-dev musl-dev g++
conda create --name wheel python=3.5 jupyter tweepy -y
conda install --name wheel numpy
conda activate wheel
wget https://www.piwheels.org/simple/tensorflow/tensorflow-1.14.0-cp35-none-linux_armv7l.whl#sha256=cba22b6d9a3e7a92c07e142bd5256c9773fd20c18090cb1d222357d3b3028655
 pip3.6 install  tensorflow-1.14.0-cp36-none-linux_armv7l.whl 
 conda install tweepy=3.7.0


#update setuptools and grpcio as it causes trouble
pip3 install --upgrade pip
python3 -m pip install --upgrade setuptools


pip3 install --no-cache-dir  --force-reinstall -Iv grpcio==1.24.0 tweepy==3.7.0
pip3 install --no-cache-dir  --force-reinstall -Iv  keras_applications
pip install gpt2-client
```
## Twitter posting
```
python3.5 twitter_post.py twitter.json alex_friends.txt
```

## Posting to Twitter and Nostr
Fill in the provided Nostr and Twitter credentials. For Twitter you need "Elevated" Write-enabled
developer API keys and you need to apply for them and give reasons.

https://developer.twitter.com/en/portal/products/elevated

Once you have credentials post as follows:

```
python3.9 twostr twitter.json nostr.json "This is my first EVER tweet posted to Twitter and Nostr"
```