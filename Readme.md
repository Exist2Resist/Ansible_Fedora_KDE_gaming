# Info

This Ansible play is used to setup Fedora KDE for a gaming scenario. It installs drivers and sets the OS up for gaming. It installs the XBOX wireless dongle driver and performs various OS tweaks to give the system the best performance.

## Assumptions

This playbook is created to run on Intel and Nvidia systems with secure boot. It should also run on AMD systems, having said that I am not interested in AMD so this is not written for one. You need to be logged in to a X11 and not Wayland session, hence Fedora KDE. Wayland sucks and it doesn't render applications properly, doesn't matter if you're on Nvidia or AMD GPUs. If you think otherwise you are clearly NOT a power user. Albeit Wayland sucks even more on Nvidia than AMD GPUs.

A lot of windows/games fail to render properly in Wayland hence the existence of xWayland, gamescope and the likes; this is the dumbest thing ever too someone at some point must have said; 
"Hey lets create a modern x window system... oh wait we need X11 compatibility because Wayland sucks!" Effectively I have no interest in Wayland, maybe when it stops being a buggy, laggy sack of potatoes I will drive it again. I also don't like any kind of HDR, so wayland is not that important to me. VRR is supported in X11 out of the box provided you are using a Display Port cable, this is the only feature I care about for gaming. X11 runs games better and smoother. I don't really care that the code base for X11 is a mess, unlike Wayland it just works and this is my experience gaming on Linux.

**TLDR:**
X11, Intel CPU, and Nvidia GPU. Secure boot is optional.

# Drivers

This script installs the XONE copr repo and driver for Microsoft wireless dongle

# Ansible for Fedora customization

Install ansible and prerequisites:
```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py --user
python3 -m pip install --user ansible
python3 -m pip install ansible-lint
ansible-galaxy collection install community.general
```

Upgrade ansible:
```bash
python3 -m pip install --upgrade --user ansible
```

Install collections:
```bash
ansible-galaxy collection install community.general
```

To specify a password for sudo, run ansible-playbook with `--ask-become-pass` (`-K` for short). If you run a playbook utilizing become and the playbook seems to hang, most likely it is stuck at the privilege escalation prompt. Stop it with `CTRL-c`, then execute the playbook with `-K` and the appropriate password.

## Running the play

Ansible play test run: 
```
ansible-playbook main.yaml --check -K
```

Actual play run: 
```
ansible-playbook main.yaml -K
```
