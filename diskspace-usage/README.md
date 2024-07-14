# Diskspace Usage

Write a script to monitor the disk space usage (`/dev/sda2`) on a server and  [*]send an email notification if it exceeds a certain threshold.

If the disk space usage exceeds `90%`, send out an alert with:

- Server name
- Current disk usage percentage

If the disk space usage is at or below `90%`, your script should print out: "Disk usage is below 90%"

---

Output of `df -h`

```bash
Filesystem      Size  Used Avail Use% Mounted on
tmpfs           3.2G  2.5M  3.2G   1% /run
/dev/sda2       468G  186G  258G  42% /
tmpfs            16G  141M   16G   1% /dev/shm
tmpfs           5.0M   12K  5.0M   1% /run/lock
efivarfs        128K  102K   22K  83% /sys/firmware/efi/efivars
/dev/sda1       1.1G  6.2M  1.1G   1% /boot/efi
tmpfs           3.2G  180K  3.2G   1% /run/user/1000
```

`[*] TODO`
