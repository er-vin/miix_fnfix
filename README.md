# miix_fnfix

Tiny script allowing to force fnlock mode on the Lenovo MIIX keyboard

Two files are provided:
 * miix_fnfix.py a python3 script depending on pyusb which forces the fnlock
   mode on the keyboard;
 * 99-miix.rules a UDEV rules to install in /etc/udev/rules.d to have fnlock
   applied on startup and when the keyboard is plugged (it assumes
   miix_fnfix.py is copied to the /root/ directory and executable, if that's
   not the case adjust the rule file)

