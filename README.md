# Instructions

1) Copy `config/settings.example.py` to `config/settings.py`

2) Download your Thing's certificates (private, cert, and CA) and put them in config

3) Run `main.py`

# To copy certs to a Raspberry Pi using SCP

```
export SCP_LOCATION="pi@192.168.86.29:~/ambient-sensor/config"
scp config/settings.py $SCP_LOCATION
scp config/*certificate.pem.crt $SCP_LOCATION
scp config/*private.pem.key $SCP_LOCATION
scp config/*Authority*.pem $SCP_LOCATION
```

# Resize example

https://github.com/jquast/blessed/blob/master/bin/on_resize.py
