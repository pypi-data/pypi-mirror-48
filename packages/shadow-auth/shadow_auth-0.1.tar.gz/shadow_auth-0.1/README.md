
<p align="center">
    <h1 align="center">Linux Shadow Authentication</h1>
    <br>
    <p align="center">Python module to validate the credentials of a Linux user using the /etc/shadow file.</p>
</p>

Usage
------------
Once installed you can import the module in your programs

```python
import shadow_auth

if shadow_auth.validate_with_password("username", "1234"):
    # What to do if the user is valid
    pass
    
if shadow_auth.validate_with_hash("username", "$1$TrOIigLp$FJg1nUqEQPt4OerLOWzr/1"):
    # What to do if the user is valid
    pass

#Get the algorithm and Salt for a User    
password_info = shadow_auth.get_password_info("username")
# password_info = {
#   "algorithm" = "1",
#   "salt" = "TrOIigLp"
# }

#Generate an MD5 hash
new_md5_hash = shadow_auth.generate_openssl_hash(
    algorithm=shadow_auth.Algorithm.MD5,
    salt="TrOIigLp",
    text="abcd12345",    
)
# new_md5_hash = "$1$TrOIigLp$FJg1nUqEQPt4OerLOWzr/1"

#Generate an SHA-256 hash
new_sha_256_hash = shadow_auth.generate_openssl_hash(
    algorithm=shadow_auth.Algorithm.MD5,
    salt="TrOIigLp",
    text="abcd12345",    
)
# new_sha_256_hash = "$5$TrOIigLp$6usEDvu0NgyuQ/IqQyvSBoP0x2RiNOz5izrMViHwXv2"

#Generate an SHA-512 hash
new_sha_512_hash = shadow_auth.generate_openssl_hash(
    algorithm=shadow_auth.Algorithm.MD5,
    salt="TrOIigLp",
    text="abcd12345",    
)
# new_sha_512_hash = "$6$TrOIigLp$IU0KwZfzVkuLLy/9vMFH1RgOmqE3LAGk0K9/15WOGStkeaN2IWYkY0jzCWHMUcSnnewnt9bOUwD2vStgko79v/"

``` 


Requirements
------------
For this project you need to have **Python >= 3.5** and the following list of programs installed in your Linux System:
* cat
* grep
* openssl
* passwd

Usually these programs come preinstalled in various linux distributions, but in case you need to install them you can use the following commands:

#### For CentOS, RHEL, Fedora
~~~
sudo yum install coreutils grep openssl passwd
~~~
#### For Debian, Ubuntu, Linux Mint
~~~
sudo apt install coreutils grep openssl passwd
~~~
Linux Permissions
------------
For this module to work your user requires access to the shadow group.
To do so you can execute the following command:

~~~
sudo usermod -a -G shadow <username>
~~~

If you are logged as the user that is going to be added to the group you might have to log out and log in again,
or reboot, in order for the changes to have effect.


Installation
------------
~~~
pip3 install linux-shadow-auth
~~~
