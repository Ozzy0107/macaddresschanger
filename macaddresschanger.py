import subprocess
import argparse
import textwrap
import sys

class MacChanger:
    def __init__(self,args):
        self.args = args

    def changeMac(self):

        try:
            print(f"Changing MAC address for {self.args.interface}\n.Setting the new value {self.args.address}")
            subprocess.call(["ifdown", self.args.interface])
            subprocess.call(["ifconfig", self.args.interface, "hw", "ether", self.args.address])
            subprocess.call(["ifup", self.args.interface])
        except Exception as e:
            print(f"Error {e}")
            sys.exit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description = 'MAC Address changer',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(
            '''
            Example: python macaddresschanger.py -i eth0 -m 00:11:22:33:44:22
            '''
        ))
    parser.add_argument('-i', '--interface', help='Interface to change the MAC Address')
    parser.add_argument('-m', '--address', help='New MAC Address')

    args = parser.parse_args()

    if not (args.address and args.interface):
        parser.print_help()
        sys.exit()

    macChanger = MacChanger(args)
    macChanger.changeMac()