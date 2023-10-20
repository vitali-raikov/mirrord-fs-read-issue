# Reproducing mirrord FS issues

1. Create a `kind` cluster, I ran it with a latest version and still experienced problem
2. Apply k8s manifest `kubectl apply -f nginx-deployment`
3. Run a mirrord exec `mirrord exec -f .mirrord/mirrord.json python3 read.py`

My behaviour:

```
➜  mirrord-fs-read-issue git:(main) ✗ mirrord exec -f .mirrord/mirrord.json python3 read.py
When targeting multi-pod deployments, mirrord impersonates the first pod in the deployment.
Support for multi-pod impersonation requires the mirrord operator, which is part of mirrord for Teams.
To try it out, join the waitlist with `mirrord waitlist <email address>`, or at this link: https://metalbear.co/#waitlist-form
⠁ mirrord exec
    ✓ Running on latest (3.72.1)!
    ✓ ready to launch process
      ✓ layer extracted
      ✓ no operator detected
      ✓ agent pod created
      ✓ pod is ready                                                                                                                                                                                                                           Traceback (most recent call last):
  File "/Users/vitali/Projects/mirrord-fs-read-issue/read.py", line 3, in <module>
    print(os.listdir("/etc/"))
          ^^^^^^^^^^^^^^^^^^^
OSError: [Errno 22] Invalid argument: '/etc/'
```

Expected behaviour

* Get a list of files and directories in /etc directory, in this example, /etc directory has

```
root@nginx-cbdccf466-q559m:/etc# ls
adduser.conf		calendar	deluser.conf  gai.conf	host.conf  issue.net	 libaudit.conf	mke2fs.conf    os-release  profile    rc3.d  resolv.conf  shadow   staff-group-for-usr-local  timezone
alternatives		cron.daily	dpkg	      group	hostname   kernel	 localtime	motd	       pam.conf    profile.d  rc4.d  rmt	  shadow-  subgid		      ucf.conf
apt			debconf.conf	environment   group-	hosts	   ld.so.cache	 login.defs	nginx	       pam.d	   rc0.d      rc5.d  securetty	  shells   subuid		      update-motd.d
bash.bashrc		debian_version	fonts	      gshadow	init.d	   ld.so.conf	 logrotate.d	nsswitch.conf  passwd	   rc1.d      rc6.d  security	  skel	   systemd
bindresvport.blacklist	default		fstab	      gshadow-	issue	   ld.so.conf.d  machine-id	opt	       passwd-	   rc2.d      rcS.d  selinux	  ssl	   terminfo
```
