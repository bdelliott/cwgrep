import argparse

from cwgrep import client


def main():
    """CLI entry point"""
    parser = argparse.ArgumentParser(
        description='Tool for searching CloudWatch logs')
    parser.add_argument('-p', '--profile', help='AWS CLI Profile name')

    args = parser.parse_args()

    c = client.Client(profile_name=args.profile)
    c.filter_logs()
