# raspi-gpt2-bot
Raspberry Pi enabled GPT2 bot plugin for Wordpress and Twitter

#usage
```
./run_gpt_wordpress.sh 'WORDPRESS_DOMAIN' 'WORDPRESS_USER' 'WORDPRESS_USER_PWD'
```

#Install on Raspberry 4
- Recommended to be ONLY run on a Raspberry Pi as the old version of Tensorflow
  is very insecure
- 4GB RAM should be enough for the 345M model
- ONLY Tensorflow 1.1.13 works on Rapsberry Pi, use AT YOUR OWN RISK,
  as such an old Tensorflow introduces a miriad security vulerabilities.
- Twitter support is experimental and running it live using prod credentials will
  likely result in suspension of your Twitter API write priviliges. Tweet less often. 