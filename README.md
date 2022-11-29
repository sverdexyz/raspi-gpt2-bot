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
conda create --name tensorflow-twitter python=3.5 jupyter -y
 conda install --name tensorflow-twitter tensorflow=1.13.1
 conda config --append channels conda-forge
 ```

### Compile tensorflow via Bazel
```
git clone https://github.com/koenvervloesem/bazel-on-arm.git
cd bazel-on-arm/
sudo make requirements
#old version of tensorflow requires old bazel version
./scripts/build_bazel.sh 0.21.0
sudo make install
 bazel version
```
And finally compile tensorflow version 1.13.1
https://www.tensorflow.org/lite/guide/build_arm
https://github.com/tensorflow/build/tree/master/raspberry_pi_builds
```
git clone https://github.com/tensorflow/tensorflow.git tensorflow_src
cd tensorflow_src/
git checkout v1.13.1
sudo tensorflow/tools/ci_build/ci_build.sh PI-PYTHON3 tensorflow/tools/ci_build/pi/build_raspberry_pi.sh 
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