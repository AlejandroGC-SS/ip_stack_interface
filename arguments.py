import argparse

class Arguments:
    """List of incoming arguments that can be provided by the terminal"""
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "--ip_address",
            type=str,
            help="IP address to be queries in the GeoIP API",
            required=True
        )
        args = parser.parse_args()
        self.ip_address = args.ip_address
