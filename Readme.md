# WARNING!

This is the new version of the script which aims to replace RPMfusion nvidia drivers with drivers from an Nvidia repo.
Be warned this script has not been tested and is a work in progress.

# Installation

A demo installation is available on Youtube.<br>
https://youtu.be/fRCUcSbjNZo

# Info

This Ansible play is used to setup Fedora KDE for a gaming scenario. It installs drivers and sets the OS up for gaming. It installs the XBOX wireless dongle driver and performs various OS tweaks to give the system the best performance.

## Assumptions

This playbook is created to run on Intel and Nvidia systems with secure boot. It should also run on AMD systems, having said that I am not interested in AMD so this is not written for one. You need to be logged in to a X11 and not Wayland session, hence Fedora KDE. Wayland sucks and it doesn't render applications properly, doesn't matter if you're on Nvidia or AMD GPUs. If you think otherwise you are clearly NOT a power user. Albeit Wayland sucks even more on Nvidia than AMD GPUs. Install the OS with secure boot enabled. 

A lot of windows/games fail to render properly in Wayland hence the existence of xWayland, gamescope and the likes; this is the dumbest thing ever too someone at some point must have said; 
"Hey lets create a modern x window system... oh wait we need X11 compatibility because Wayland sucks!" Effectively I have no interest in Wayland, maybe when it stops being a buggy, laggy sack of potatoes I will drive it again. I also don't like any kind of HDR, so wayland is not that important to me. VRR is supported in X11 out of the box provided you are using a Display Port cable, this is the only feature I care about for gaming. X11 runs games better and smoother. I don't really care that the code base for X11 is a mess, unlike Wayland it just works and this is my experience gaming on Linux.

**TLDR:**
This script requires the followin X11, Intel CPU, and Nvidia GPU, and Secure boot.

## Black screen during installation

Sometimes when booting into the graphical installer you will encounter a continuous black screen and the installer will never load.
During the grub selection screen move the up down arrows on the keyboard to stop the grub timer, then highlight the option to install and press `e` on the keyboard. Move down to the line that starts with `linux` and at the end of it add `nomodeset` then press `ctrl + x` on the keyboard to boot. This should fix the graphical installer black screen/not booting. 

## Mok enrollment

The default mok enrollment password is `Secret` and this is set in the `vars/vars.yaml` file. 

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

To specify a password for sudo, run ansible-playbook with `--ask-become-pass` (`-K` for short). If you run a playbook utilizing become and the playbook seems to hang, most likely it is stuck at the privilege escalation prompt. Stop it with `CTRL-c`, then execute the playbook with `-K` and the appropriate password.

## Testing a playbook

Using a `--check` command can test a playbook without making changes. Mind you this is not a good representation of what the playbook will do. 

```bash
ansible-playbook my_playbook.yaml --check -K
```

## Running the playbooks

Open a shell terminal and do the following
```bash
git clone https://github.com/Exist2Resist/Ansible_Fedora_KDE_gaming.git
cd Ansible_Fedora_KDE_gaming
```

You need to be logged into a Wayland session after a fresh install, which by default you are, and run the x11 installation first.
You can check what session you are logged into by running the following in a Terminal shell: `echo $XDG_SESSION_TYPE`, if it is `Wayland` run the following.
```bash
ansible-playbook fedora_x11_install.yaml -K
```

Logout of the Wayland session and log into a x11 session then run one of these. 

The system will reboot after running part 1 hence it is split in to 2 plays.
Then we will run the actual playbooks, there  are two parts.
```bash
ansible-playbook fedora_kde_part1.yaml -K
# The system will reboot between these two plays, run part2 after that. 
ansible-playbook fedora_kde_part2.yaml -K
```
