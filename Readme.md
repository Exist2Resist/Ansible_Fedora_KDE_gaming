## Assumptions

This playbook is created to run on Intel and Nvidia systems with secure boot. It should also run on AMD CPU/Nvidia systems, having said that I am not interested in AMDip. There is a reason Nvidia has a 95% GPU market share as of March 2026. You need to be logged in to a X11 and not Wayland session, hence Fedora KDE. Wayland sucks and it doesn't render applications properly, doesn't matter if you're on Nvidia or AMD GPUs. If you think otherwise you are clearly NOT a power user. Albeit Wayland sucks even more on Nvidia than AMD GPUs.

A lot of windows/games fail to render properly in Wayland hence the existence of xWayland, gamescope and the likes; this is the dumbest thing ever too; 
"Hey lets create a modern x window system, oh wait we need X11 compatability because it sucks! "Effectively I have no interest in Wayland maybe when it stops being a buggy, laggy sack of potatoes.

**TLDR:**
X11, Intel CPU, and Nvidia GPU. Secure boot is optional.<br><br>

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
